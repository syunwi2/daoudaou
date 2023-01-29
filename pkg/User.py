import pkg.Conn as Conn
import pkg.make_irreg as irreg
from flask import render_template, session, redirect, url_for

"""
    logout
    expire the session
    parameter : None
    return : (html template)
"""
def logout():
    session.pop('id', None)
    return redirect(url_for('firstpage', isLoginned=None))


"""
    firstpage
    show first login page if user is not loginned.
    if user is loginned, show event page.
    parameter : None
    return : (html template)
"""
def firstpage():
    if 'id' in session:
        return redirect(url_for('event'))
    else:
        return render_template("login.html", isLoginned=None)
  
"""
    login
    show login page or event page, depending on the result of login
    parameter : id, pw
    return : (html template)
"""
def login(id, pw):
    isLoginned = test_login(id, pw)

    if isLoginned:
        session['id'] = id
        return redirect(url_for('event'))

    else:
        return render_template("login.html", isLoginned=isLoginned)

"""
    test_login
    check the input ID and PASSWORD is in the DB and right pair.
    parameter : id, pw
    return : True/False
"""
def test_login(id, pw):
    conn, cur = Conn.open()
    
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

    # --- CHECK THE FORM ---
    # if there is blank in form, show notification.
    noID, noName, noPW, noPW2 = isBlankInForm(id, name, pw, pw2)
    if noID or noName or noPW or noPW2:
        return render_template("join.html", noID=noID, noName=noName, noPW=noPW, noPW2=noPW2)

    # if there is no blank in form, check the email is valid.
    unvalidID = isIDunvalid(id)
    if unvalidID:
        return render_template("join.html", isUnvalidEmail=True)

    # if email is valid, check the email is ued.
    usedID = isIDused(id)
    if usedID:
        return render_template("join.html", isEmailExist=True)

    # if pw and pw2 is different, show notification.
    isPWsame = (pw == pw2)
    if isPWsame is False:
        return render_template("join.html", isPWsame=False)

    # --- INSERT CATA INTO DB ---
    # if there is no problem in form, insert values in DB.
    if not usedID and isPWsame:
        if insertData(id, name, pw):
            return render_template("login.html", isLoginned=None)
        else:
            return render_template("join.html")

"""
    isBlankInForm
    get data from user and check is it completed.
    parameter : id, name, pw, pw2
    return : tuple of (True/False)
"""
def isBlankInForm(id, name, pw, pw2):
    noID, noName, noPW, noPW2 = False, False, False, False

    if id is "":
        noID=True
    if name is "":
        noName=True
    if pw is "":
        noPW=True
    if (noPW is False) and (pw2 is ""):
        noPW2=True

    return noID, noName, noPW, noPW2

"""
    isIDunvalid
    check the input id value is valid.
    parameter : id
    return : (True/False)    
"""
def isIDunvalid(id):
    numAt = id.count('@')
    if numAt != 1:
        return True
    else:
        numDot = id.split('@')[1].count('.')
        if numDot < 1:
            return True
        else:
            return False 

"""
    isIDused
    check the input id value is already in DB.
    parameter : id
    return : (True/False)    
"""
def isIDused(id):
    isIDused = True

    conn, cur = Conn.open()
    idCheckQuery = f'SELECT EMAIL FROM USER WHERE EMAIL = "{id}";'
    numID = cur.execute(idCheckQuery)

    if numID == 1:
        conn.close()
        return isIDused
    else:
        isIDused = False
        conn.close()
        return isIDused

"""
    insertData
    insert id, name, pw value into DB
    return : True
"""
def insertData(id, name, pw):
        conn, cur = Conn.open()

        insertQuery = f'INSERT INTO USER VALUES("{id}", "{name}", "{pw}");'
        cur.execute(insertQuery)
        conn.commit()

        conn.close()
        return True