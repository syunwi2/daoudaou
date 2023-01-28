import pymysql
from flask import Flask, render_template
from flask import request
import pymysql

# 2. 비정기 스케쥴 등록하기
#서버에서 받아오기
def get_info_reg():
    sc_email = request.form['event_email'] #사용자 이메일
    sc_day = request.form['event_day']
    sc_title = request.form['event_title'] #일정 제목
    sc_content = request.form['event_content'] #일정 내용
    
    return (sc_email, sc_day, sc_title, sc_content)


 
# 쿼리 추가
def make_reg():
    email = get_info_reg()[0]
    day = get_info_reg()[1]
    title = get_info_reg()[2]
    content = get_info_reg()[3]
    
    conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = 'root1234',
                       db = 'daoudaou',
                       charset = 'utf8')
    cur = conn.cursor()
    
    
    sql_reg = f'insert into routine(email,day,title,content) values("{email}","{day}","{title}","{content}")'
    cur.execute(sql_reg)
    conn.commit()
    conn.close()
    

