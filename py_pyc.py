#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import py_compile
import compileall


def __file(files):
    '''
        单个文件转换
    '''
    pyc_path = py_compile.compile(files)

    print('生成pyc路径: 当前位置：%s' % pyc_path)

    user_input = input('是否删除源文件：').strip()

    if user_input.lower() == 'yes' or user_input.lower() == 'y':

        os.remove(files)

    if user_input.lower() == 'no' or user_input.lower() == 'n':

        exit('程序退出')


def __dir(dir_path):
    '''
        目录所有文件转换
    '''
    cresult = compileall.compile_dir(dir_path)

    if cresult:

        print('\033[1;33m\n* succeed/转换成功! \033[0m')

        user_input = input('是否删除源文件：')

        if user_input.lower() == 'yes' or user_input.lower() == 'y':

            for root, dir, filename in os.walk(dir_path):

                for file in filename:

                    all_file = os.path.join(root, file)

                    cre = re.findall('.*py', all_file)

                    if cre:

                        for path in cre:

                            os.remove(path)

                            return print('删除成功')

        if user_input.lower() == 'no' or user_input.lower() == 'n':

            exit('程序退出')

    else:

        print('\033[1;33m\n* unsuccessful/转换失败! \033[0m')


if __name__ == '__main__':
    while True:

        file_or_dir = input('请输入你要转换的py文件或者文件夹：').strip()

        if file_or_dir.lower() == 'quit' or file_or_dir.lower() == 'q':

            exit('程序退出')

        if not os.path.exists(file_or_dir):

            print('\033[1;34m文件路径不存在! 请重新输入 \033[0m')

        if os.path.isfile(file_or_dir):

            __file(file_or_dir)

        if os.path.isdir(file_or_dir):

            __dir(file_or_dir)




