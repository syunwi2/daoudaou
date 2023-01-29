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
    cur = conn.cursor()
    return conn, cur

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
    conn, cur = openConn()
    
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
def join(id, name, pw, pw2):
    print(id, name, pw, pw2)

    noID, noName, noPW, noPW2 = False, False, False, False
    if id is "":
        noID=True
    if name is "":
        noName=True
    if pw is "":
        noPW=True
    if pw is not "" and pw2 is "":
        noPW=False
        noPW2=True
    if noID or noName or noPW or noPW2:
        return render_template("join.html", noID=noID, noName=noName, noPW=noPW, noPW2=noPW2)

    conn, cur = openConn()

    idCheckQuery = f'SELECT EMAIL FROM USER WHERE EMAIL = "{id}";'
    numID = cur.execute(idCheckQuery)
    if numID is 1:
        return render_template("join.html", isEmailExist=True)

    isPWsame = (pw == pw2)
    if isPWsame is False:
        return render_template("join.html", isPWsame=False)

    if (numID is 0) and isPWsame:
        insertQuery = f'INSERT INTO USER VALUES("{id}", "{name}", "{pw}");'
        print(insertQuery)
        cur.execute(insertQuery)
        conn.commit()

        idCheckQuery = f'SELECT EMAIL FROM USER WHERE EMAIL = "{id}";'
        numID = cur.execute(idCheckQuery)
        print(numID)

        conn.close()
        return render_template("login.html", isLoginned=None)