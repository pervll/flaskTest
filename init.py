import sqlite3
import db
def init():
    con=sqlite3.connect("./db/database.sqlite")
    cur=con.cursor()
    cur.execute('''
        SELECT * FROM sqlite_master WHERE type='table' AND name LIKE 'x%';
    ''')
    rows=cur.fetchall()
    for row in rows:
        table_name=row[1]
        cur.execute(f'''
            DROP TABLE {table_name};
        ''')
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
        delete from accounts
    ''')
    cur.execute('''
        delete from valid_accounts
    ''')
    sql1='INSERT INTO accounts (username,password) VALUES (?,?)'
    cur.executemany(sql1,[('Admin','123456'),('Admin1','123456')])
    cur.execute('''
                UPDATE sqlite_sequence SET seq = 0 WHERE name='valid_accounts';
                ''')
    con.commit()
    cur.execute('VACUUM;')
    con.commit()
    con.close()