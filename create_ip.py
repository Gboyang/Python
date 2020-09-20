#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randrange

count = int(input("输入生成ip数量："))

for num in range(count):

    ip = ""

    for i in range(4):

        tmp = randrange(255)

        ip = ip + str(tmp) + "."

    ip = ip[:-1]

    print(ip + "\n".strip())
