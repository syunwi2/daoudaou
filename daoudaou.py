from flask import Flask, render_template, request
import pkg.User as User
from pkg import make_irreg
from pkg import make_reg
from pkg.mail import sched_send, sched_del_event
# from pkg.practice_printhello import print_hello




app = Flask(__name__)




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
    return render_template("routine.html", events=my_list)


@app.route("/send_event", methods=["POST"])
def send_event():
    make_irreg.get_info_irreg()
    make_irreg.make_irreg()
    my_list=[]
    return render_template("event.html", events=my_list)


@app.route("/send_routine", methods=["POST"])
def send_routine():
    make_reg.get_info_reg()
    make_reg.make_reg()
    my_list =[]
    return render_template("routine.html", events=my_list)



sched_send(app)
sched_del_event()
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

