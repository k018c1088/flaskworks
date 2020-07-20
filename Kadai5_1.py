from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('Kadai5_1.html')


@app.route('/send', methods=['POST'])

def send():
    name = request.form['name']
    mail = request.form['mail']
    return render_template('send.html', name = name, mail = mail)

if __name__ == '__main__':
    app.run(debug=True)