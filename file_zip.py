#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zipfile
import os


def create_zip(path):

    zip_f = zipfile.ZipFile(os.path.basename(path) + '.zip','w')

    for filepath, dirs, file in os.walk(path, topdown=False):

        for name in dirs:

            zip_f.write(os.path.join(filepath,name))

        for name in file:

            zip_f.write(os.path.join(filepath,name))

    zip_f.close()


def uncompress_zip(path):
    """解压缩一个文件"""
    print('正在解压文件中……')

    zfile = zipfile.ZipFile(path, "r")

    zfile.extractall()


if __name__ == '__main__':
    path_file = input('输入压缩解压文件：').strip()

    if path_file.endswith('zip'):

        uncompress_zip(path_file)

        print('解压完成')

    else:

        create_zip(path_file)