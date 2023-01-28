from flask import Flask, render_template, request
import User

app = Flask(__name__)

"""
    로그인 페이지
"""
@app.route("/")
def login():
    isLoginned=None
    return render_template("login.html", isLoginned=isLoginned)


"""
    로그인 성공 : 일정 페이지로 이동
    로그인 실패 : 로그인 페이지로 이동
"""
@app.route("/login", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        id = request.form["id"]
        pw = request.form["pw"]

        isLoginned = User.test_login(id, pw)
        print(isLoginned)

        if isLoginned:
            return render_template("user.html", isLoginned=isLoginned)

        else:
            print("here")
            return render_template("login.html", isLoginned=isLoginned)


"""
    일회성 일정 페이지
"""
@app.route("/event")
def event():
    page = True
    my_list = [
        {
            "datetime": "10월 7일 10시 30분",
            "title": "뭐 할까요?",
            "content": "야호",
        },
    ]
    return render_template("event.html", events=my_list)


"""
    반복성 일정 페이지
"""
@app.route("/routine")
def routine():
    page = True
    my_list = [
        {
            "datetime": "10월 7일 10시 30분",
            "title": "워 할까요?",
            "content": "이야호",
        },
    ]
    return render_template("routine.html", events=my_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
