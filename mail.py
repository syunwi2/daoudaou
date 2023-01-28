import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import pymysql
import datetime


conn = pymysql.connect(host = 'localhost',
                        user = 'root',
                        password = 'root1234',
                        db = 'daoudaou',
                        charset = 'utf8')
cur = conn.cursor()  

sql1 = 'select * from user'
sql2 = 'select * from event'        
sql3 = 'select * from routine'                      


def send_mail(user_email, user_events, user_routines):                    # 메일 발송 모듈
    SMTP_SERVER = 'smtp.gmail.com'                                        # 환경 변수
    SMTP_PORT = 465
    SMTP_USER = 'daoudaouuu@gmail.com'
    SMTP_PASSWORD = 'udgcjxmqtamredsa'

    msg = MIMEMultipart('alternative')   
                                        
    msg['From'] = SMTP_USER                         # 발신자
    msg['To'] = f'{user_email}'                     # 수신자
    
    today = datetime.datetime.today()               # 제목에 들어갈 오늘 날짜
    
    msg['Subject'] = f'[다우다우] {today.month}월 {today.day}일 일정입니다우다우 ♡'           # 제목      
    
    mail_text = '\n일회성 일정\n'                              # 메일 내용
    for event in user_events:                                 # event 일정 추가
        mail_text += f'일정 이름 : {event[3]}\n'
        mail_text += f'시간 : {str(event[2])[11:16]}\n'
        mail_text += f'일정 내용 : {event[4]}\n'
        
    mail_text += f'\n반복성 일정\n'  
    for routine in user_routines:                             # routine 일정 추가
        mail_text += f'일정 이름 : {routine[3]}\n'
        mail_text += f'일정 내용 : {routine[4]}\n'
    
    text = MIMEText(mail_text, _charset='utf-8')          
    msg.attach(text)


    # 실제 메일을 보내는 코드
    smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)     
    smtp.login(SMTP_USER, SMTP_PASSWORD)                
    smtp.sendmail(msg['From'], msg['To'], msg.as_string())
    smtp.close()


def check_schedule():                                            # 발송 여부 체크 및 발송
    today_date = str(datetime.datetime.now().date())             # 오늘 날짜 for event 체크
    today_day = datetime.datetime.today().weekday()              # 오늘 요일 2진수 변환 for routine 체크
    if today_day == 0:                                           
        today_day = 0b1000000
    if today_day == 1:
        today_day = 0b0100000
    if today_day == 2:
        today_day = 0b0010000
    if today_day == 3:
        today_day = 0b0001000
    if today_day == 4:
        today_day = 0b0000100
    if today_day == 5:
        today_day = 0b0000010
    if today_day == 6:
        today_day = 0b0000001
 
    cur.execute(sql1)                                              # 유저 메일 user_mail에 저장
    for user in cur:
        user_email = user[0]                                         
        user_events = []
        user_routines = []
        
        cur.execute(f'select * from event where email = \'{user_email}\'')            # event date 검사 및 user_events 에 당일 일정 추가
        for event in cur:
            event_date = str(event[2])[0:10]
            if event_date == today_date:
                user_events.append(event)
        
        cur.execute(f'select * from routine where email = \'{user_email}\'')          # routine day 검사 및 user_routines 에 당일 일정 추가
        for routine in cur:
            routine_day = int(bin(routine[2])[2:])
            if (today_day&routine_day):
                user_routines.append(routine)
        # print(user_events, user_routines)            
        if user_events or user_routines: 
            send_mail(user_email, user_events, user_routines)                            # 메일 발송
        

check_schedule()
        
# 루틴과 이벤트 모두 있을경우 메일 두번 발송 이슈 해결해야됨..
# 이벤트랑 루틴 여러번 있을경우 메일 여러번 발송 이슈



