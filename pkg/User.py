import pymysql
from flask import render_template

"""
    openConn
    open Connection to DB Server
    parameter : None
    return : connection object
"""
def openConn():
    conn = pymysql.connect(host = 'localhost',
        user ='root',
        password = 'root1234',
        db = 'daoudaou',
        charset = 'utf8')
    return conn

"""
    firstpage
    show first login page
    parameter : None
    return : (html template)
"""
def firstpage():
    return render_template("login.html", isLoginned=None)
  
"""
    login
    show login page or event page, depending on the result of login
    parameter : id, pw
    return : (html template)
"""
def login(id, pw):
    isLoginned = test_login(id, pw)

    # 수정 필요
    if isLoginned:
        my_list = [
            {
            "datetime": "10월 7일 10시 30분",
            "title": "뭐 할까요?",
            "content": "야호",
            },
        ]
        return render_template("event.html", events=my_list)

    else:
        return render_template("login.html", isLoginned=isLoginned)

"""
    test_login
    check the input ID and PASSWORD is in the DB and right pair.
    parameter : id, pw
    return : True/False
"""
def test_login(id, pw):
    conn = openConn()
    cur = conn.cursor()
    
    IDquery = f'SELECT EMAIL FROM USER WHERE EMAIL = "{id}";'
    numID = cur.execute(IDquery)

    if numID is 0:
        conn.close()
        return False

    PWquery = f'SELECT EMAIL FROM USER WHERE EMAIL = "{id}" AND PASSWORD = "{pw}";'
    numRightPW = cur.execute(PWquery)
    
    if numRightPW is 0:
        conn.close()
        return False

    conn.close()
    return True

"""
    joinPage
    show join page
    return : (html template)
"""
def joinPage():
    return render_template("join.html")

"""
    join
    get data from user and send it to DB 
    parameter : id, name, pw
    return : (html template)
"""
def join():
    return render_template("login.html", isLoginned=None)