import sqlite3
def init():
    con=sqlite3.connect("./db/database.sqlite")
    cur=con.cursor()
    cur.execute('''
        create table if not exists accounts (
            username text unique, 
            password text
        )
    ''')
    cur.execute('''
        delete from accounts
    ''')
    cur.execute('''
        insert into accounts
            values('Admin','123456')
    ''')
    con.commit()
    con.close()