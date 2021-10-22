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


@app.route('/student/add')
def add_student():
    req = request.get_json()

    firstName = req['firstName']
    middleName = req['middleName']
    lastName = req['lastName']
    email = req['email']
    dateOfBirth = req['dateOfBirth']
    gender = req['gender']
    phoneNumber = req['phoneNumber']
    address = req['address']
    state = req['state']
    localGovernment = req['localGovernment']
    nextOfKin = req['nextOfKin']
    jambScore = req['jambScore']
    email = req['email']

    print(firstName)

    # conn = mysql.get_db()
    # curr = conn.cursor()
    # curr.execute(f'INSERT INTO student (firstName, middleName, lastName, dateOfBirth, gender, phoneNumber, address, stateOfOrigin, localGovernment, nextOfKin, jambScore, email) VALUES ({firstName}, {middleName}, {lastName}, {dateOfBirth}, {gender}, {phoneNumber}, {address}, {state}, {localGovernment}, {nextOfKin}, {jambScore}, {email});')
    # conn.commit()
    # curr.close()

    return json.dumps('success')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/students/<id>')
def students(id):
    id_number = id
    return render_template('students.html', id_number = id_number)


if __name__ == "__main__":
    app.run(debug=True)