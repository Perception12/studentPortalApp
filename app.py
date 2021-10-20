from flask import Flask, render_template, url_for, request, flash
from flaskext.mysql import MySQL
import pymysql.cursors
import datetime
import json


app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_DB'] = 'university'
app.config['MYSQL_DATABASE_USER'] = 'perception'
app.config['MYSQL_DATABASE_PASSWORD'] = '$Eunfunmi2021'

mysql = MySQL(app, cursorclass=pymysql.cursors.DictCursor)



#  # if state_lg[n]["state"] == "Abia":
#         #     print(state_lg[n]["local"])    

# conn = mysql.get_db()
# curr = conn.cursor()
# curr.execute()
# conn.commit()
# curr.close()


@app.route('/')
def index():
     return render_template('index.html')


@app.route('/student/portal')
def portal():
        with open('static/json/data.json') as file:
            content = file.read()
        state_lg = json.loads(content)
        states = []

        n = len(state_lg)

        for i in range(n):
            states.append(state_lg[i]["state"])

        return render_template('portal.html', states=states, state_lg = state_lg, n=n)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/students/<id>')
def students(id):
    id_number = id
    return render_template('students.html', id_number = id_number)


if __name__ == "__main__":
    app.run(debug=True)