from flask import Flask, redirect, url_for, request, render_template
import sqlite3
#测试暂用 初始化数据库
def init():
    con=sqlite3.connect("./db/accounts.sqlite")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS catalog \
    (id INTEGER PRIMARY KEY NOT NULL, username TEXT UNIQUE, password TEXT)")
    sql1='''
    insert into catalog(ID,username,password)
    values (0, 'Admin', '123456')
    '''
    cur.execute(sql1)
    con.commit()
    con.close()