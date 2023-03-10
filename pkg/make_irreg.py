import pymysql
from flask import Flask, render_template
from flask import request
import pymysql
from pkg import User


# 1. 비정기 스케쥴 등록하기
#서버에서 받아오기
def get_info_irreg():

    sc_email = str(User.session['id']) #사용자 이메일
    sc_date = request.form['event_date']
    sc_time = request.form['event_time'] # 일정 날짜
    sc_title = request.form['event_title'] #일정 제목
    sc_content = request.form['event_content'] #일정 내용

    
    return (sc_email, sc_date, sc_time, sc_title, sc_content)
 
# DB 추가
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
    
# 2. 조회
def irreg_view():
    conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = 'root1234',
                       db = 'daoudaou',
                       charset = 'utf8')
    cur = conn.cursor()
    
    sql_view1 = f"select * from event where email = '{User.session['id']}' order by datetime"
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

    
    conn.close()

    return irreg_dict_list

# 3. 일정 삭제
def erase_event():
    key = request.form['event_key']

    conn = pymysql.connect(host = 'localhost',
                           user = 'root',
                           password = 'root1234',
                           db = 'daoudaou',
                           charset = 'utf8')
    cur = conn.cursor()

    sql_erase1 = f'delete from event where event_key = "{key}"'
    cur.execute(sql_erase1)

    conn.commit()
    conn.close()
    
# 이름 받아오기
def get_name():
    conn = pymysql.connect(host = 'localhost',
                           user = 'root',
                           password = 'root1234',
                           db = 'daoudaou',
                           charset = 'utf8')
    cur = conn.cursor()

    sql_name = f"select NAME from user where email = '{User.session['id']}'"
    cur.execute(sql_name)
    name= []
    for record in cur:
        name.append(list(record))
    return name[0][0]

    conn.close()
