from flask import Flask, render_template, request
import datetime

app = Flask(__name__)
data_list = []

@app.route('/')

def index():
    return render_template('Kadai5_2.html')

@app.route('/', methods=['POST'])

def send():
    dtn = datetime.datetime.now()
    time = dtn.strftime('%m/%d %H:%M')
    data = request.form['data']
    data_time = [time, data]
    if not data == '':
        data_list.append(data_time)
    return render_template('Kadai5_2.html', list = data_list)



if __name__ == '__main__':
    app.run(debug=True)