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
        create table if not exists valid_accounts (
            id integer primary key autoincrement
            username text unique
        )
    ''')
    cur.execute('''
        delete from accounts
    ''')
    cur.execute('''
        delete from valid_accounts
    ''')
    cur.execute('''
        insert into accounts
            values('Admin','123456')
    ''')
    con.commit()
    con.close()