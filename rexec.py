#!/usr/bin/env python
# -*- coding: utf-8 -*-
import paramiko


class PasswordRemote:
    def __init__(self):
        self.ip = '10.0.0.50'
        self.Port = 22
        self.Pass = '123456'
        self.User = 'root'

    def min(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(hostname=self.ip,
                        port=self.Port,
                        username=self.User,
                        password=self.Pass)
        except TimeoutError:
            return '你连接的主机%s连接失败请确认他是否还活着' % self.ip
        except paramiko.ssh_exception.AuthenticationException:
            return '请检查你的用户名密码是否正确，用户密码认证失败'
        while True:
            order = input('请输入你要执行的命令：').strip()
            if order.upper() == 'Q' or order.upper() == 'QUIT':
                ssh.close()
                exit()
            stdin, stdout, stderr = ssh.exec_command(order)
            print(stdout.read().decode('utf-8'))
            print(stderr.read().decode('utf-8'))


if __name__ == '__main__':
    Pr = PasswordRemote()
    Pr.min()
