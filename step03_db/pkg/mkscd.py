import pymysql
from flask import Flask, render_template
from flask import request
import pymysql


#�꽌踰꾩뿉�꽌 諛쏆븘�삤湲�
def get_info_reg():
    sc_email = request.args.get('email') #�궗�슜�옄 �씠硫붿씪
    sc_date = request.args.get('date')
    sc_time = request.args.get('time') # �씪�젙 �궇吏�
    sc_title = request.args.get('title') #�씪�젙 �젣紐�
    sc_content = request.args.get('content') #�씪�젙 �궡�슜
    
    return (sc_email, sc_date, sc_time, sc_title, sc_content)


 
# 荑쇰━ 異붽��
def make_reg():
    event_key = 234324 #auto increment濡� UID 遺��뿬
    email = get_info_reg()[0]
    date_time = get_info_reg()[1] + ' ' + get_info_reg()[2]
    title = get_info_reg()[3]
    content = get_info_reg()[4]
    
    conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = 'root1234',
                       db = 'daoudaou',
                       charset = 'utf8')
    cur = conn.cursor()
    
    
    sql_reg = f'insert into event(event_key,email,datetime,title,content) values("{event_key}","{email}","{date_time}","{title}","{content}")'
    print(sql_reg)
    cur.execute(sql_reg)
    conn.commit()
    conn.close()