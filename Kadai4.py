from flask import Flask, render_template

app = Flask(__name__)
list = []

@app.route('/')

def index():
    return render_template('Kadai4.html',title="ユーザー一覧", list=list)

@app.route('/user/<username>/')

def profile(username):
    list.append(username)
    return render_template('user.html',masseage=username + 'を追加しました')

if __name__ == "__main__":
    app.run(debug=True)