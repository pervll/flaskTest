from flask import Flask, redirect, url_for, request, render_template,flash,session
import functools
import sqlite3
from init import init

app = Flask(__name__)
app.secret_key='asfda8r9s'
init()

#这块显示登录装态不知道那里错了
@app.route('/')
def index():
    if 'user' in session:
        return render_template("index.html",username=session['user'])
    return render_template("index.html")
#你们研究一下

@app.route('/login',methods = ['POST', 'GET'])
def login():
    error=None
    if request.method == 'POST':
        username = request.form['username']        
        password = request.form['password']
        #从index.html中读取username和password
        con=sqlite3.connect("./db/accounts.sqlite")
        cur=con.cursor()
        cur.execute("select * from catalog")
        a=cur.fetchall()
        #保存表单
        for i in a:
            if(i[1]==username and i[2]==password):
                session['user']=username
                flash('You were successfully logged in')
                return redirect(url_for('index'))
        flash('Invalid username or password. Please try again!','error')
    return render_template("login.html")
        
@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/register')
def register():
    username = request.form['username']        
    password = request.form['password']
    c_password = request.form['confirm_password']
    return render_template("register.html")

if __name__ == '__main__':
    app.run()