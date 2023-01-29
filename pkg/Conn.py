import pymysql

"""
    openConn
    open Connection to DB Server
    parameter : None
    return : connection object
"""
def open():
    conn = pymysql.connect(host = 'localhost',
        user ='root',
        password = 'root1234',
        db = 'daoudaou',
        charset = 'utf8')
    cur = conn.cursor()
    return conn, cur