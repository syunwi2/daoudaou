import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import pymysql

j


conn = pymysql.connect(host = 'localhost',
                        user = 'root',
                        password = 'root1234',
                        db = 'daoudaou',
                        charset = 'utf8')
cur = conn.cursor()  
sql =                    
                       

# SMTP : 보내는 메일과 관련된 정보들 필요
# POP  : 받는 메일과 관련된 정보들 필요
# 보내는 계정의 정보 ex) 비밀번호

def send_mail():
    # 환경 변수 
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 465
    SMTP_USER = 'daoudaouuu@gmail.com'
    SMTP_PASSWORD = 'udgcjxmqtamredsa'


    # 기본 내용 및 구조
    msg = MIMEMultipart('alternative')   # 기본 속성값.
                                        # 첨부 파일 관련 속성값 : 'mixed'
    msg['From'] = SMTP_USER              # 발신자
    msg['To'] = SMTP_USER                # 수신자
    msg['Subject'] = '[다우다우] x월 x일 일정입니다우다우 ♡'                  

    text = MIMEText('테스트2', _charset='utf-8')
    msg.attach(text)


    # 실제 메일을 보내는 코드
    smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)     # 메일 서버 빌려서 쓰겠다고 인증 받기
    smtp.login(SMTP_USER, SMTP_PASSWORD)                # 로그인
    smtp.sendmail(SMTP_USER, SMTP_USER, msg.as_string())
    smtp.close()



def if_send_mail():
    

schedule.every().day.at('08:30').if_send_mail()


    