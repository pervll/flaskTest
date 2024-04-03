import sqlite3
from flask import g

#连接表
def connect_db():
    CON=sqlite3.connect("./db/database.sqlite")
    return CON


def close_db(CON):
    CON.close()
    return

#向database.db中的表SHEET_NAME插入元组DATA，返回操作是否成功，注意DATA内的元素需与表单的列相互对应。
def insert_into(SHEET_NAME,DATA):
    con=connect_db()
    cur=con.cursor()
    N=len(DATA)
    sql1="insert into %s values(%s)" %(SHEET_NAME,(N-1)*"?,"+"?")
    #print(sql1)
    try:
        cur.execute(sql1,DATA)
        con.commit()
    except:
        flag=False
    else:
        flag=True
    finally:
        close_db(con)
    return flag

#获取SHEET_NAME中所有的元素
def get_db(SHEET_NAME):
    con=connect_db()
    cur=con.cursor()
    cur.execute("select * from %s" %(SHEET_NAME))
    con.commit()
    return cur.fetchall()
