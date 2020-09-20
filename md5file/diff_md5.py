#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
import hashlib
'''
    比对md5值
'''


def diff_file_md5(filename, content):
    '''
    md5,
    content : 传入file内容进行加密
    '''
    md5 = hashlib.md5()

    md5.update(content)

    md5_val = md5.hexdigest()

    with open('md5lib', 'r', encoding='utf-8') as f1:

        for str_dic in f1:

            dic_content = json.loads(str_dic)

            for key, val in dic_content.items():

                if filename in key:

                    if md5_val in val:

                        print('文件:【%s】没有发生改变' % filename)

                        continue

                    else:

                        print('\033[0;31m 文件:【%s】发生改变\n md5: 【%s】 【%s】 \033[0m' % (filename, val, md5_val))
                else:

                    continue


def func_dir(dir_path):
    '''
        处理目录
    '''
    for root, dirname, filename in os.walk(dir_path):

        for file in filename:

            filepath = os.path.join(root, file)

            with open(filepath, 'rb') as f1:

                file_content = f1.read()

                if file_content:

                    diff_file_md5(file, file_content)

                else:

                    continue


def func_file(file_path):
    '''
        处理文件
    '''
    with open(file_path, 'rb') as f1:

        file_content = f1.read()

        file_name = file_path.split("\\")[-1]  # linux 下将\\换成/

        if file_content:

            diff_file_md5(file_name, file_content)
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

    path = input('请输入你要比对的目录或者文件：').strip()

    func_run(path)
