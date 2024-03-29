from flask import (
    Flask, redirect, url_for, request, render_template,session,flash
)
import sqlite3
from init import init
from db import(
    connect_db,close_db,insert_into,get_db
)
import time

app = Flask(__name__)
app.secret_key='asfda8r9s' #这个好像和session有关
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
        username=session['user']
        con=connect_db()
        cur=con.cursor()
        
        cur.execute('insert into valid_accounts (username) values (?)',username)
        while True:
            db=get_db()
            if len(db)==2:
                for i in db:
                    if(db[i][1]=="username"):
                        if(db[i][0]%2==0):
                            partner=db[i-1]
                        else:
                            partner=db[i+1]
                        
                            
                    
            
    return "0"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)