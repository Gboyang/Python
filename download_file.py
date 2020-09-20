#!/usr/bin/env python
# -*- coding: utf-8 -*-
import paramiko
import os
from stat import S_ISDIR as isdir


def down_from_remote(sftp_obj, remote_dir_name, local_dir_name):

    remote_file = sftp_obj.stat(remote_dir_name)

    if isdir(remote_file.st_mode):

        check_local_dir(local_dir_name)

        print('开始下载文件夹：' + remote_dir_name)

        for remote_file_name in sftp.listdir(remote_dir_name):

            sub_remote = os.path.join(remote_dir_name, remote_file_name)

            sub_remote = sub_remote.replace('\\', '/')

            sub_local = os.path.join(local_dir_name, remote_file_name)

            sub_local = sub_local.replace('\\', '/')

            down_from_remote(sftp_obj, sub_remote, sub_local)

    else:

        print('开始下载文件：' + remote_dir_name)

        sftp.get(remote_dir_name, local_dir_name)


def check_local_dir(local_dir_name):

    if not os.path.exists(local_dir_name):

        os.makedirs(local_dir_name)


if __name__ == "__main__":
    ip_addr = '172.17.2.18'
    user = 'root'
    passwd = '123456'
    port = 22
    # 远程文件路径（需要绝对路径）
    remote_dir = '/root/'
    # 本地文件存放路径（绝对路径或者相对路径都可以）
    local_dir = 'file_download/'

    t = paramiko.Transport((ip_addr, port))
    t.connect(username=user, password=passwd)
    sftp = paramiko.SFTPClient.from_transport(t)
    down_from_remote(sftp, remote_dir, local_dir)
    t.close()