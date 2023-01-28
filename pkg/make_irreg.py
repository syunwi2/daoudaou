import pymysql
from flask import Flask, render_template
from flask import request
import pymysql


# 1. 비정기 스케쥴 등록하기
#서버에서 받아오기
def get_info_irreg():

    sc_email = '22' #사용자 이메일
    sc_date = request.form['event_date']
    sc_time = request.form['event_time'] # 일정 날짜
    sc_title = request.form['event_title'] #일정 제목
    sc_content = request.form['event_content'] #일정 내용

    
    return (sc_email, sc_date, sc_time, sc_title, sc_content)
 
# 쿼리 추가
def make_irreg():
    email = get_info_irreg()[0]
    date_time = str(get_info_irreg()[1]) + ' ' + str(get_info_irreg()[2])
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
    
    
def irreg_view():
    conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = 'root1234',
                       db = 'daoudaou',
                       charset = 'utf8')
    cur = conn.cursor()

    
    sql_view1 = 'select * from event order by datetime'
    cur.execute(sql_view1)

    schedule_list_irreg = []
    irreg_dict_list = []

    for record in cur:
        schedule_list_irreg.append(list(record))

    for scd in schedule_list_irreg:
        scd[2] = str(scd[2])

    for scd in schedule_list_irreg:
        dict = {}
        dict['event_key'] = scd[0]
        dict['event_title'] = scd[3]
        dict['event_date'] = scd[2][:11]
        dict['event_time'] = scd[2][11:]
        dict['event_content'] = scd[4]
        irreg_dict_list.append(dict)

    return irreg_dict_list
