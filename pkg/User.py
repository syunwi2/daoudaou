import pymysql

def openConn():
    conn = pymysql.connect(host = 'localhost',
        user ='root',
        password = 'root1234',
        db = 'daoudaou',
        charset = 'utf8')
    return conn

"""
    로그인 함수
    입력된 id가 db에 존재하고
    pw가 일치하면
    True반환
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