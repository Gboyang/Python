#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import struct
import json
import socketserver
import sys


class Myserver(socketserver.BaseRequestHandler):
    def __init__(self, *args, **kwargs):

        self.env = sys.platform

        self.dir_path = self.is_dir()

        super(Myserver, self).__init__(*args, **kwargs)

    def is_dir(self):
        '''
            创建目录
        '''
        file_dir = os.path.join(os.getcwd(), 'User_lib')

        if not os.path.exists(file_dir):

            os.mkdir(file_dir)

            return file_dir

        return file_dir

    def file_upload(self):
        '''
            上传文件
        '''
        head = self.request.recv(4)

        head_num = struct.unpack('i', head)[0]

        str_dic = self.request.recv(head_num)

        dic = json.loads(str_dic)

        if self.env == 'win32':

            filename = os.path.join(self.dir_path, dic['filename']).replace('\\', '/')

        else:

            filename = os.path.join(self.dir_path, dic['filename'])

        with open(filename, 'wb') as f:

            while dic['filesize'] > 0:

                cont = self.request.recv(1024)

                f.write(cont)

                dic['filesize'] -= len(cont)

        self.request.send('上次成功!'.encode('utf-8'))

    def file_download(self):
        '''
            下载文件
        '''
        lib_file = os.listdir(self.dir_path)

        self.dic_str(lib_file)

        down_file_name = self.request.recv(1024).decode('utf-8')

        for i in lib_file:

            if down_file_name == i:

                filesize = os.path.getsize(os.path.join(self.dir_path, down_file_name))

                filename = down_file_name

                dic = {'filename': filename, 'filesize': filesize}

                self.dic_str(dic)

                with open(os.path.join(self.dir_path, down_file_name), 'rb') as f:

                    while filesize > 0:

                        content = f.read(1024)

                        self.request.send(content)

                        filesize -= len(content)

                self.request.send('下载成功'.encode('utf-8'))

    def dic_str(self, dic_list):

        str_dic = json.dumps(dic_list).encode('utf-8')

        num = struct.pack('i', len(str_dic))

        self.request.send(num)

        self.request.send(str_dic)
        
    def handle(self) -> None:

        ret = self.request.recv(1024).decode('utf-8')

        func = getattr(self, ret)

        func()


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9000), Myserver)

    server.serve_forever()