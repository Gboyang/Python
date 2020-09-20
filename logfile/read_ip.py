#!/usr/bin/env python
# -*- coding: utf-8 -*-
log_file = "access.log"

ip = {}

with open(log_file) as f:

    for i in f.readlines():

        ip_attr = i.strip().split()[0]

        if ip_attr in ip.keys():

            ip[ip_attr] = ip[ip_attr] + 1

        else:

            ip[ip_attr] = 1

print(ip)
