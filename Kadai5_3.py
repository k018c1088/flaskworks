from flask import Flask, render_template, request
import datetime

app = Flask(__name__)
data_list = []
total = 0

@app.route('/', methods=['GET', 'POST'])

def index():
    global total
    dtn = datetime.datetime.now()
    time = dtn.strftime('%m/%d %H:%M')
    data = request.form.get('data')
    if data is not None:
        data_time = [time, data]
        total += int(data)
        data_list.append(data_time)
        return render_template('Kadai5_3.html', ave = total / len(data_list), list = data_list)
    else :
        return render_template('Kadai5_3.html', ave = total, list = data_list)


if __name__ == '__main__':
    app.run(debug=True)