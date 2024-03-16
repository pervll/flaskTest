from flask import Flask, redirect, url_for, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        print(1)
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
                return redirect(url_for('success',name = username))
            else:
                return "fail"
        
    else:
        print(2)
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))
@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

if __name__ == '__main__':
    app.run()