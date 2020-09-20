#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import socket
import struct
import json


def upload(sk):
    sk.send(b'upload')
    file_path = input('请输入你要上传的文件：').strip()
    if os.path.isfile(file_path):
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)
        dic = {'filename': file_name, 'filesize': file_size}
        str_dic = json.dumps(dic).encode('utf-8')
        str_dir_len = struct.pack('i', len(str_dic))
        sk.send(str_dir_len)
        sk.send(str_dic)
        with open(file_path, 'rb') as f:
            while file_size > 0:
                content = f.read(1024)
                sk.send(content)
                file_size -= len(content)
        ret = sk.recv(1024)
        print(ret.decode('utf-8'))
    else:
        print('文件不存在！')


def download(sk):
    sk.send(b"download")
    list_len = sk.recv(4)
    count_len = struct.unpack('i', list_len)[0]
    bytes_count = sk.recv(count_len)
    count = json.loads(bytes_count)
    for i in count:
        print(i)
    filename = input("请输入你要下载的文件名：").strip()
    str_name = filename.encode('utf-8')
    sk.send(str_name)
    head = sk.recv(4)
    head_num = struct.unpack('i', head)[0]
    by_dic = sk.recv(head_num)
    dic = json.loads(by_dic)
    with open(dic['filename'], 'wb') as f:
        while dic['filesize'] > 0:
            cont = sk.recv(1024)
            f.write(cont)
            dic['filesize'] -= len(cont)
        ret = sk.recv(1024)
        print(ret.decode('utf-8'))


if __name__ == '__main__':
    sk = socket.socket()
    sk.connect(('127.0.0.1', 9000))
    choice_list = [('下载文件', download), ('上传文件', upload)]
    for num, item in enumerate(choice_list, 1):
        print(num, item[0])
    option = int(input("请输入你的选择："))
    choice_list[option - 1][1](sk)

