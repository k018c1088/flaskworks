from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def index():
    list = []
    for val in range(1,11):
        if not (val) % 2 == 0:
            list.append(str(val))
    list = " ".join(list)
    return render_template('Kadai3_1.html', list=list)

if __name__ == "__main__":
    app.run(debug=True)