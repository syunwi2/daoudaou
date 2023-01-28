import pymysql

conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = 'root1234',
                       db = 'daoudaou',
                       charset = 'utf8')
cur = conn.cursor()



my_list = [
        {
            "datetime": "10월 7일 10시 30분",
            "title": "워 할까요?",
            "content": "이야호",
        },
    ]

# 비정기 일정 조회    
dict = {}

sql_view1 = 'select * from event order by datetime'
cur.execute(sql_view1)

schedule_list_irreg = []

for record in cur:
    schedule_list_irreg.append(list(record[2:]))

for scd in schedule_list_irreg:
    scd[0] = str(scd[0])

print(schedule_list_irreg)
conn.close()


# 정기 일정 조회    
sql_view2 = 'select * from routine order by day'
cur.execute(sql_view2)

schedule_list_reg = []

for record in cur:
    schedule_list_reg.append(list(record[2:]))

for scd in schedule_list_reg:
    scd[0] = str(scd[0])

print(schedule_list_reg)
conn.close()
