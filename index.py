from flask import (
    Flask, redirect, url_for, request, render_template,session,flash
)
import sqlite3
from init import init
from db import(
    connect_db,close_db,insert_into,get_db
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
            new_account=(username,password)
            if insert_into("accounts",new_account):
                print(1)
                flash('You have successfully registered. Please log in.','info')
                return redirect(url_for('login'))
            else:
                print(2)
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
        con=connect_db()
        cur=con.cursor()
        cur.execute('insert into valid_accounts (username) values (?)',username)
        con.commit()
        con.close()
        while True:
            db=get_db("valid_accounts")
            flag=False
            if len(db)==2:
                for i in range(0,len(db)):
                    if(db[i][1]==username[0]):
                        if(db[i][0]%2==0):
                            partner=db[i-1][1]
                            match_index=db[i-1][0]+db[i][0]
                            master=True
                        else:
                            partner=db[i+1][1]
                            match_index=db[i-1][0]+db[i][0]
                            master=False
                        flag=True
                        print(partner)
            if flag:
                break 
        #将配对完成的二人组从数据库中删除
        #建立新的棋局数据库
        if master:
            con=connect_db()
            cur=con.cursor()
            a='x'+str(uuid.uuid1())[0:8]
            cur.execute(f"create table if not exists {a} (playerW text, playerB text, map text);")
            cur.execute(f"insert into {a} values(?,?,?);",(partner,username[0],json.dumps(config.ORIGINAL_MAP)))
            cur.execute(f"DELETE FROM valid_accounts WHERE username IN (?,?);",(partner,username[0]))
            con.commit()
            con.close()
            return redirect(url_for('chess_game',index=a))
    return "0"

@app.route('/chess_game/<index>')
def chess_game(index):
    return "Success!"


if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT)