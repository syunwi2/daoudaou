import pymysql
from flask import Flask, render_template
from flask import request
import pymysql
from pkg import User

# 1. 비정기 스케쥴 등록하기
# 서버에서 받아오기


def get_info_reg():
    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    decimal = 0
    i = 64
    for day in days:
        if day in request.form.keys():
            decimal += i
            i = int(i / 2)
        else:
            i = int(i / 2)
            continue

    sc_day = decimal
    sc_email = str(User.session['id'])  # 사용자 이메일
    #    sc_day = request.form['event_day']
    sc_title = request.form["event_title"]  # 일정 제목
    sc_content = request.form["event_content"]  # 일정 내용
    sc_time = request.form["event_time"]
    # request.form key 명칭...
    return (sc_email, sc_day, sc_title, sc_content, sc_time)


# DB 추가
def make_reg():
    email = get_info_reg()[0]
    day = int(get_info_reg()[1])
    title = get_info_reg()[2]
    content = get_info_reg()[3]
    time = str(get_info_reg()[4])

    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="root1234",
        db="daoudaou",
        charset="utf8",
    )
    cur = conn.cursor()

    sql_reg = f'insert into routine(email,day,title,content,time) values("{email}","{day}","{title}","{content}","{time}")'
    cur.execute(sql_reg)
    conn.commit()
    conn.close()


# 2. 일정 조회
def reg_view():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="root1234",
        db="daoudaou",
        charset="utf8",
    )
    cur = conn.cursor()

    sql_view2 = f"select * from routine where email = '{User.session['id']}' order by day desc"  # 정렬 기능.. ??? 일단 앞 요일일수록 숫자 크니까 역순으로 정렬...
    cur.execute(sql_view2)

    schedule_list_reg = []
    reg_dict_list = []

    for record in cur:
        schedule_list_reg.append(list(record))
    for scd in schedule_list_reg:
        scd[5] = str(scd[5])
    for scd in schedule_list_reg:
        dict = {}
        dict["routine_key"] = scd[0]
        dict["routine_title"] = scd[3]
        dict["routine_day"] = scd[2]
        dict["routine_time"] = scd[5]
        dict["routine_content"] = scd[4]
        reg_dict_list.append(dict)

    conn.commit()
    conn.close()
    return reg_dict_list


# 3. 일정 삭제
def erase_routine(key, sort_of):
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="root1234",
        db="daoudaou",
        charset="utf8",
    )
    cur = conn.cursor()
    # sql_erase1 = f'delete from routine where event_key = "{key}"'
    sql_erase1 = f'delete from {sort_of} where {sort_of}_key = "{key}"'
    cur.execute(sql_erase1)

    conn.commit()
    conn.close()
