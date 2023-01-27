from flask import Flask, render_template
from flask import request
import pymysql

app = Flask(__name__)

@app.route("/db") #외부에서 들어온 number라는 변수도
def view_template(): # 여기에 파라미터로 전달해서 뷰함수실행 가능
	return render_template("db.html")
    #여기에 값들 반환시켜줘야한다!
    
# form의 action을 route랑 맞춰줘야 버튼 클릭했을 때(버튼 클릭하면 요청) 해당 기능이 실행된다.

# 백엔드 서버
@app.route("/dept-search")
def search_dept():
    dept_no = request.args.get('deptno') # 화면에서 정보 받는 방식은 get, post// 따로 설정 안한 이상 기본은 get방식이라 get으로 받게 하면 된다.    
    print(dept_no)
    print('---')
# 1. mysql - python 연결
    conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = 'root1234',
                       db = 'scott',
                       charset = 'utf8')
# 2. 커서 
    cur = conn.cursor()
    sql = f'select * from emp where deptno = {dept_no}'
    cur.execute(sql)
# result에 요청된 값을 담아줌
    result =[]
    for record in cur:
        result.append([record[0], record[1]])
    print('--------------------------------------------')
# return을 통해 화면을 출력(응답에 대한 결과로 브라우저에서 결과값 확인 가능)
    return render_template("result.html", result = result)
# 결과를 보여줄 때는 반드시 그에 해당하는 html이 존재해야한다.

if __name__ == "__main__":
		app.run(host = "0.0.0.0", port = 5002, debug = True)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
# 프레임워크는 폴더 이름이랑 파일 위치도 다 지켜서 형식 맞춰서 해놔야 나온다. 아니믄 안나온다ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ.
#ex. Flask에서 문서 제공하는 경로가 templates

# DB 서버 설정 기본 포맷
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/db") #외부에서 들어온 number라는 변수도
# def view_template(): # 여기에 파라미터로 전달해서 뷰함수실행 가능
# 	return render_template()
#     #여기에 값들 반환시켜줘야한다!
    
    
# if __name__ == "__main__":
# 		app.run(host = "0.0.0.0", port = 5002, debug = True)
  
