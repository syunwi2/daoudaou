from flask import Flask, render_template, request, redirect, url_for
import pkg.User as User
from pkg import make_irreg
from pkg import make_reg
from pkg.mail import sched_del_event, sched_send

app = Flask(__name__)
app.secret_key = "Key"


"""
    로그인 페이지
    로그인 성공 : 일정 페이지로 이동
    로그인 실패 : 로그인 페이지로 이동
"""
@app.route("/", methods=["POST", "GET"])
def firstpage():
    if request.method == "POST":
        id = request.form["id"]
        pw = request.form["pw"]
        return User.login(id, pw)
    else:
        return User.firstpage()


"""
    회원 가입 
"""
@app.route("/join", methods=["POST", "GET"])
def join():
    if request.method == "POST":
        id = request.form["id"]
        name = request.form["name"]
        pw = request.form["pw"]
        pw2 = request.form["pw2"]
        return User.join(id, name, pw, pw2)
    else:
        return User.joinPage()


"""
    로그아웃
"""
@app.route("/logout")
def logout():
    return User.logout()


"""
    일회성 일정 페이지
"""


@app.route("/event")
def event():
    my_list = make_irreg.irreg_view()
    return render_template("event.html", events=my_list)


"""
    반복성 일정 페이지
"""


@app.route("/routine")
def routine():
    page = True
    my_list = make_reg.reg_view()
    day_list = ["월", "화", "수", "목", "금", "토", "일"]
    for routine in my_list:
        my_day_list = []
        day_number = routine["routine_day"]
        day_number = bin(day_number)[2:]
        day_number = "0" * (7 - len(day_number)) + day_number
        for i in range(0, 7):
            if day_number[i] == "1":
                my_day_list.append(day_list[i])
        routine["routine_day"] = ", ".join(my_day_list)
    return render_template("routine.html", events=my_list)


@app.route("/send_event", methods=["POST"])
def send_event():
    make_irreg.get_info_irreg()
    make_irreg.make_irreg()
    my_list = []
    return redirect(url_for("event"))


sched_del_event
sched_send


@app.route("/send_routine", methods=["POST"])
def send_routine():
    make_reg.get_info_reg()
    make_reg.make_reg()
    my_list = []
    return redirect(url_for("routine"))


# 이벤트 삭제
@app.route("/erase_event", methods=["delete"])
def erase_event():
    key = request.get_json()["key"]
    sort_of = "event"
    make_reg.erase_routine(key, sort_of)
    return "success"


# 루틴 삭제
@app.route("/erase_routine", methods=["delete"])
def erase_routine():
    key = request.get_json()["key"]
    sort_of = "routine"
    make_reg.erase_routine(key, sort_of)
    return "success"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
