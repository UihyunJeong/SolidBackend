from asyncio import run_coroutine_threadsafe
from crypt import methods
from click import style
from flask import Flask, jsonify, request
from uihyun import *

app = Flask(__name__)

app.users = {}
app.id_count = 1
app.tweets = []

@app.route("/ping", methods=["GET"])
def ping():
    return "pong"


@app.route("/sign-up", methods=["POST"])
def sing_up():
    new_user = request.json
    new_user["id"] = app.id_count
    app.users[app.id_count] = new_user
    app.id_count += 1

    return jsonify(new_user)

@app.route('/tweet-300', methods=['POST'])
def tweet_300():
    payload = request.json

    if payload['id'] not in app.users:
        return f"{payload['id']}는 등록되지 않은 사용자입니다.", 400
    
    if len(payload['tweet']) > 300 :
        return '300자를 초과하였습니다.', 400

    app.tweets.append(payload)
    return 'Ok', 200
    


if __name__ == "__main__":
    app.run(port="10219", debug=True)
