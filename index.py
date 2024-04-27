from flask import (
    Flask, redirect, url_for, request, render_template,session,flash
)
import sqlite3
from init import init
from db import(
    connect_db,close_db,insert_into,get_db,set_null
)
import time,uuid,json
from settings import Config
config=Config()

app = Flask(__name__)
app.config.from_object('settings.EnvConfig')
init()

@app.route('/')
def index():
    if 'user' in session:
        return render_template("index.html",username=session['user'])
    return render_template("index.html")

@app.route('/login',methods = ['POST', 'GET'])
def login():
    error=None
    if request.method == 'POST':
        username = request.form['username']        
        password = request.form['password']
        #从index.html中读取username和password
        db=get_db("accounts")
        #保存表单
        for i in db:
            if(i[0]==username and i[1]==password):
                session['user']=username
                flash('You were successfully logged in')
                return redirect(url_for('index'))
        flash('Invalid username or password. Please try again!','error')
    return render_template("login.html")
        
@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/register',methods = ['POST','GET'])
def register():
    error=None
    if request.method == 'POST':
        username = request.form['username']        
        password = request.form['password']
        c_password = request.form['confirm_password']
        if password==c_password:
            new_account=(username,password,0,'')
            if insert_into("accounts",new_account):
                flash('You have successfully registered. Please log in.','info')
                set_null("accounts","map_name",f'WHERE username = "{username}" ')
                return redirect(url_for('login'))
            else:
                flash('This username has been taken, please try again.','error')
                return redirect(url_for('register'))
        else:
            flash("Passwords doesn't match. Please try again!",'error')
    return render_template("register.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/chess')
def chess():
    
    if 'user' in session:
        username=[(session['user'])]
        partner=''
        a=''
        flag=False
        con=connect_db()
        cur=con.cursor()
        cur.execute('insert into valid_accounts (username) values (?)',username)
        con.commit()
        con.close()
        while True:
            db=get_db("valid_accounts")
            con.close()
            if len(db)==2:
                for i in range(0,len(db)):
                    if(db[i][1]==username[0]):
                        if(db[i][0]%2==0):
                            partner=db[i-1][1]
                            master=True
                        else:
                            partner=db[i+1][1]
                            master=False
                        flag=True
            if flag:
                break 
        if flag==False:
            return redirect(url_for('fail'))

        #建立新的棋局数据库
        if master:
            a=str('x'+str(uuid.uuid3(uuid.NAMESPACE_DNS,username[0]+'_'+partner))[0:8])
            con=connect_db()
            cur=con.cursor()
            cur.execute(f"create table if not exists {a} (playerW text, playerB text, map text, current_player text);")
            cur.execute(f"insert into {a} values(?,?,?,?);",(username[0],partner,config.DEFAULT_STATUS,username[0]))
            cur.execute("UPDATE accounts SET onPlay = 1 WHERE username IN (?,?)",(username[0],partner))
            session['master']=1
            cur.execute(f"UPDATE accounts SET map_name = ? WHERE username IN (?,?)",(a,username[0],partner))
            con.commit()
            con.close()
        else:
            a=str('x'+str(uuid.uuid3(uuid.NAMESPACE_DNS,partner+'_'+username[0]))[0:8])
        return redirect(url_for('chess_game',index=a))
    return "0"

@app.route('/chess_game/<index>')
def chess_game(index):
    session['map']=index
    #检测到onplay就把自己从valid_accounts中丢出  
    username=session['user']
    con=connect_db()
    cur=con.cursor()
    cur.execute(f'SELECT onplay FROM accounts WHERE username = "{username}"')
    con.commit()
    is_playing=cur.fetchall()[0][0]
    print(is_playing)
    if is_playing==1:
        print("yes")
        cur.execute(f'DELETE FROM valid_accounts WHERE username = "{username}" ')
        con.commit()
    else:
        return redirect(url_for('fail'))
    con.close()
    
    con=connect_db()
    cur=con.cursor()
    #cur.execute("DELETE FROM valid_accounts WHERE username = %s" %(session['user']))
    #con.commit()
    cur.execute(f"SELECT map FROM {index}")
    data=cur.fetchall()[0][0]
    con.commit()
    close_db(con)

    #return render_template("chess_game.html",**config.ORIGINAL_MAP)
    return render_template("chess_game.html",data=data)
#TODO 在js中遍历White和Black并渲染棋子，现在遍历有一点问题

@app.route('/fail')
def fail():
    return "Fail"

@app.route('/chess_index')
def chess_index():
    return 1

if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT)