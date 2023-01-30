from flask import Flask, render_template, request, redirect, url_for
import pkg.User as User
from pkg import make_irreg
from pkg import make_reg
import pkg.mail as mail
from pkg.mail import sched_del_event, sched_send
from pkg import User

app = Flask(__name__)
app.secret_key = "Key"

"""
    로그인 페이지
    로그인 성공 : 일정 페이지로 이동
    로그인 실패 : 로그인 페이지로 이동
"""


@app.route("/", methods=["POST", "GET"])
def firstpage():
    
    sched_send()
    sched_del_event()
    
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
    if not User.isLoginned():
        return redirect(url_for("firstpage", isLoginned=None))
    return User.logout()


"""
    일회성 일정 페이지
"""


@app.route("/event")
def event():
    if not User.isLoginned():
        return redirect(url_for("firstpage", isLoginned=None))
    user_name = make_irreg.get_name()
    my_list = make_irreg.irreg_view()
    return render_template("event.html", events=my_list, name=user_name)


"""
    반복성 일정 페이지
"""


@app.route("/routine")
def routine():
    if not User.isLoginned():
        return redirect(url_for("firstpage", isLoginned=None))
    page = True
    user_name = make_irreg.get_name()
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
    return render_template("routine.html", events=my_list, name=user_name)


@app.route("/send_event", methods=["GET", "POST"])
def send_event():
    if request.method == "POST":
        make_irreg.get_info_irreg()
        make_irreg.make_irreg()
        my_list = []
        return redirect(url_for("event"))
    else:
        return redirect(url_for("firstpage", isLoginned=None))
        


@app.route("/send_routine", methods=["GET", "POST"])
def send_routine():
    if request.method == "POST":
        make_reg.get_info_reg()
        make_reg.make_reg()
        my_list = []
        return redirect(url_for("routine"))
    else:
        return redirect(url_for("firstpage", isLoginned=None))


# 이벤트 삭제
@app.route("/erase_event", methods=["GET", "DELETE"])
def erase_event():
    if request.method == "DELETE":
        key = request.get_json()["key"]
        sort_of = "event"
        make_reg.erase_routine(key, sort_of)
        return "success"
    else:
        return redirect(url_for("firstpage", isLoginned=None))


# 루틴 삭제
@app.route("/erase_routine", methods=["GET", "DELETE"])
def erase_routine():
        if request.method == "DELETE":
            key = request.get_json()["key"]
            sort_of = "routine"
            make_reg.erase_routine(key, sort_of)
            return "success"
        else:
            return redirect(url_for("firstpage", isLoginned=None))

# sched_send(app)
# sched_del_event()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)
