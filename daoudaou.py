from flask import Flask, render_template, request
import User

app = Flask(__name__)

"""
    로그인 페이지
"""
@app.route('/')
def login():
   return render_template('login.html', isLoginned=None)

"""
    로그인 성공 : 일정 페이지로 이동
    로그인 실패 : 로그인 페이지로 이동
""" 
@app.route('/login', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
    id = request.form['id']
    pw = request.form['pw']
      
    isLoginned = User.Login.test_login(id, pw)
      
    if isLoginned:
        return render_template('user.html', isLoginned=isLoginned)
    
    else:
        return render_template('login.html', isLoginned=isLoginned)
 
if __name__ == '__main__':
   app.run(host='0.0.0.0', port = 80, debug = True)
