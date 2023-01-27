import pymysql

conn = pymysql.connect(host = 'localhost',
        user ='root',
        password = 'root1234',
        db = 'daoudaou',
        charset = 'utf8')
cur = conn.cursor()
        
class Login:
    """
        로그인 함수
        입력된 id가 db에 존재하고
        pw가 일치하면
        True반환
    """
    def test_login(id, pw):
        id = id
        pw = pw
        
        isID = isID(id)
        isPW = isPW(pw)

        conn.close()
        return False
    
    """
        유효한 ID인지 검사하는 함수
    """
    def isID(id):
        
        return True
    
    """
        유효한 비밀번호인지 검사하는 함수
    """
    def isRightPW(id, pw):
        
        return True