import pymysql
from flask import Flask, render_template
from flask import request
import pymysql


# 1. 비정기 스케쥴 등록하기
#서버에서 받아오기
def get_info_irreg():
    sc_email = request.args.get('email') #사용자 이메일
    sc_date = request.args.get('date')
    sc_time = request.args.get('time') # 일정 날짜
    sc_title = request.args.get('title') #일정 제목
    sc_content = request.args.get('content') #일정 내용
    
    return (sc_email, sc_date, sc_time, sc_title, sc_content)
 
# 쿼리 추가
def make_irreg():
    email = get_info_irreg()[0]
    date_time = get_info_irreg()[1] + ' ' + get_info_irreg()[2]
    title = get_info_irreg()[3]
    content = get_info_irreg()[4]
    
    conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = 'root1234',
                       db = 'daoudaou',
                       charset = 'utf8')
    cur = conn.cursor()
    

    sql_irreg = f'insert into event(email,datetime,title,content) values("{email}","{date_time}","{title}","{content}")'
    cur.execute(sql_irreg)
    conn.commit()
    conn.close()
    