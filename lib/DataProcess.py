# -*- coding: utf-8 -*-

import pymysql

def fetch():
    try:
        DB = {
            "host": "10.5.127.4",
            "user": "zabbix",
            "password": "MySQL@123",
            "db": "",
            }
        conn = pymysql.connect(DB["host"], DB["user"], DB["password"], DB["db"])
        cursor = conn.cursor()
        # SQL 查询语句
        sql = "select * from zabbix.verifyCode"
        cursor.execute(sql)
        rs = cursor.fetchall()
        password = trans(rs)
        conn.close()
        return rs
    except Exception as e:
        print(e)
        return '8877up'
