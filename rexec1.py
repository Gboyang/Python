#!/usr/bin/env python
# -*- coding: utf-8 -*-
import paramiko
import uuid


class SSHConnection(object):

    def __init__(self, host='172.16.5.100', port=22, username='root', pwd='123'):
        self.host = host
        self.port = port
        self.username = username
        self.pwd = pwd
        self.__k = None

    def create_file(self):
        file_name = str(uuid.uuid4())
        with open(file_name, 'w') as f:
            f.write('sb')
        return file_name

    def run(self):
        self.connect()
        self.upload('1.py')
        self.rename('1.py', '2.py')
        self.close()

    def connect(self):
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=self.username, password=self.pwd)
        self.__transport = transport

    def close(self):
        self.__transport.close()

    def upload(self, target_path):
        # 连接，上传
        file_name = self.create_file()

        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        # 将location.py 上传至服务器 /tmp/test.py
        sftp.put(file_name, target_path)

    def rename(self, old_path, new_path):
        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        # 执行命令
        cmd = "mv %s %s" % (old_path, new_path,)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        # 获取命令结果
        result = stdout.read()

    def cmd(self, command):
        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(command)
        # 获取命令结果
        result = stdout.read()
        return result


ha = SSHConnection()
ha.run()