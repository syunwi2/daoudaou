from flask import Flask, render_template
from flask import request
import pymysql
from pkg.mkscd import *

app = Flask(__name__)

@app.route("/db") #외부에서 들어온 number라는 변수도
def view_template(): # 여기에 파라미터로 전달해서 뷰함수실행 가능
	return render_template("db.html")
    #여기에 값들 반환시켜줘야한다!
    
# form의 action을 route랑 맞춰줘야 버튼 클릭했을 때(버튼 클릭하면 요청) 해당 기능이 실행된다.

# 백엔드 서버
@app.route("/dept-search")
def search_dept():
    get_info_reg()
    make_reg()
    
    return render_template("db.html",result = print(get_info_reg()))

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
  
