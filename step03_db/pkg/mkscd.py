import pymysql
from flask import Flask, render_template
from flask import request
import pymysql


#서버에서 받아오기
def get_info_reg():
    sc_email = request.args.get('email') #사용자 이메일
    sc_date = request.args.get('date')
    sc_time = request.args.get('time') # 일정 날짜
    sc_title = request.args.get('title') #일정 제목
    sc_content = request.args.get('content') #일정 내용
    
    return (sc_email, sc_date, sc_time, sc_title, sc_content)


 
# 쿼리 추가
def make_reg():
    event_key = '잘늘려보자' #auto increment로 UID 부여
    email = get_info_reg()[0]
    date_time = get_info_reg()[1] + ' ' + get_info_reg()[2]
    title = get_info_reg()[3]
    content = get_info_reg()[4]
    
    conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = 'root1234',
                       db = 'scott',
                       charset = 'utf8')
    cur = conn.cursor()
    
    
    sql_reg = 'insert into event(event_key,email,datetime,title,content) values(%s,%s,%s,%s,%s)'
    cur.execute(sql_reg)
    conn.commit()
    conn.close()