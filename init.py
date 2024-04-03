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
            id integer primary key autoincrement,
            username text
        )
    ''')
    cur.execute('''
        delete from valid_accounts
    ''')
    con.commit()
    con.close()