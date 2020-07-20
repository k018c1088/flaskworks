from flask import Flask
import datetime
app = Flask(__name__)

@app.route('/')

def get_date():
    dtn = datetime.datetime.now()
    dt = dtn.strftime('%m/%d %H:%M')
    return dt
    

if __name__ == "__main__":
    app.run(debug=True)