#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def get_cpu_status(path='/proc/loadavg'):
    '''
        监控CPU负载
    '''
    loadavg = {}

    with open(path, 'r', encoding='utf-8') as f1:

        list_content = f1.read().split()

        # ['0.00', '0.03', '0.05', '2/114', '1752'] 三个数1、5、15分钟内的平均进程数，后面两个一个的分子是正在运行的进程数，分母是进程总数
        loadavg['lavg_1'] = list_content[0]

        loadavg['lavg_2'] = list_content[1]

        loadavg['lavg_15'] = list_content[2]

    return loadavg


def get_memory_status(path='/proc/meminfo'):
    '''
       内存监控
    '''
    mem_dic = {}

    with open(path, 'r', encoding='utf-8') as f2:

        lines = f2.readlines()

        for line in lines:

            name = line.strip().split(':')[0]

            data = line.split(":")[1].split()[0]

            mem_dic[name] = float(data)

    return mem_dic['MemTotal'] - mem_dic['MemFree'] - mem_dic['Buffers'] - mem_dic['Cached']


def get_network_status(path='/proc/net/dev'):
    '''
        网卡流量
    '''
    net_info = {}

    with open(path, 'r', encoding='utf-8') as f3:

        lines = f3.readlines()

        for line in lines[2:]:

            line = line.split(":")

            eth_name = line[0].strip()

            if eth_name != 'lo':

                io_dic = {}

                io_dic['receive'] = round(float(line[1].split()[0]) / (1024.0 * 1024.0), 2)

                io_dic['transmit'] = round(float(line[1].split()[8]) / (1024.0 * 1024.0), 2)

                net_info[eth_name] = io_dic

    return net_info


def get_disk_status():
    '''
        抓取磁盘io
    '''
    f = {}

    r = {}

    disk = os.statvfs('/')

    f['available'] = float(disk.f_bsize * disk.f_bavail)

    f['capacity'] = float(disk.f_bsize * disk.f_blocks)

    f['used'] = float((disk.f_blocks - disk.f_bfree) * disk.f_frsize)

    r['used'] = round(f['used'] / (1024 * 1024 * 1024), 2)

    r['capacity'] = round(f['capacity'] / (1024 * 1024 * 1024), 2)

    r['available'] = r['capacity'] - r['used']

    r['percent'] = int(round(float(r['used']) / r['capacity'] * 100))

    return f, r
