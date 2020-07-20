from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def index():
    list = {"英語":87, "数学":90, "国語":45, "理科":76, "社会":31}
    return render_template('Kadai3_2.html',title="70点以上の科目：", list=list)

if __name__ == "__main__":
    app.run(debug=True)