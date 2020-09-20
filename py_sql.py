#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql


def pysql_connect():
    '''
    连接
    '''
    try:
        conn = pymysql.connect(host='10.0.0.40', port=3306, user='test',
                               password='123123', db='test', charset='utf8'
                               )

        cursor = conn.cursor()

    except Exception as err:

        return print(err)

    return conn, cursor


def pysql_execute(sql_list):
    '''
    执行sql语句
    '''
    conn, cursor = pysql_connect()

    try:

        for sql in sql_list:

            cursor.execute(sql)

        conn.commit()

    except Exception as err:

        return print(err)

    cursor.close(), conn.close()


if __name__ == '__main__':
    sql = [
        'create table test(id int(4) not null , name varchar(16) not null);',
        'insert into test(id,name) values(2,"yy"),(3,"hh");',
    ]
    pysql_execute(sql)
