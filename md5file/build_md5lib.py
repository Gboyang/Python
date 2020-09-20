#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import os
import json

'''
        生成md5lib比对文件
'''


def public_file_md5(filename, content):
    '''
    md5,
    content : 传入file内容进行加密
    '''
    key_dic = {}

    md5 = hashlib.md5()

    md5.update(content)

    key_dic[filename] = md5.hexdigest()

    str_dic = json.dumps(key_dic)

    with open('md5lib', 'a+', encoding='utf-8') as f1:

        f1.write(str_dic + '\n')

    return print('\033[0;32m 文件：%s md5: %s \033[0m' % (filename, md5.hexdigest()))


def func_dir(dir_path):
    '''
        读取目录中文件
    '''
    for root, dirname, filename in os.walk(dir_path):

        for file in filename:

            filepath = os.path.join(root, file)

            with open(filepath, 'rb') as f1:

                file_content = f1.read()

                if file_content:

                    public_file_md5(file, file_content)

                else:

                    continue


def func_file(file_path):
    '''
        处理针对文件
    '''
    with open(file_path, 'rb') as f1:

        file_content = f1.read()

        file_name = file_path.split("\\")[-1]  # linux 下将\\换成/

        if file_content:

            public_file_md5(file_name, file_content)
        else:

            return print('\033[0;31m 文件%s 为空 \033[0m' % file_name)


def func_run(target_path):
    '''
        程序人口
    '''
    if not os.path.exists(target_path):

        return print('\033[0;31m【%s】路径不存在\033[0m' % target_path)

    if os.path.isdir(target_path):

        func_dir(target_path)

    if os.path.isfile(target_path):

        func_file(target_path)


if __name__ == '__main__':

    while True:

        path = input('请输入你要md5的文件或者目录：').strip()

        if path == 'q' or path == 'quit' or path == 'exit':

            exit('程序退出')

        func_run(path)