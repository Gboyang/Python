#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def my_copy_file(sourcedir, targetdir):
    '''
    :param sourcedir: 源文件夹
    :param targetdir: 目标文件夹
    :return:
    '''
    for dirpath, dirnames, filenames in os.walk(sourcedir):

        print('源文件夹：{}\n源文件夹内的文件夹列表：{}\n源文件夹内的文件列表：{}'.format(dirpath, dirnames, filenames))

        if len(dirnames) == 0:

            for filename in filenames:

                source_file = os.path.join(dirpath, filename)

                target_file = os.path.join(targetdir, filename)

                print('{}<=====>{}'.format(source_file, target_file))


if __name__ == '__main__':

    sourcedir = r'C:\Users\Gboyang\Desktop\test1'

    targetdir = r'C:\Users\Gboyang\Desktop\test'

    my_copy_file(sourcedir, targetdir)
