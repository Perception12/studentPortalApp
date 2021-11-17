from flask import Flask, render_template, url_for, request, flash, current_app
from flaskext.mysql import MySQL
import pymysql.cursors
import datetime
import json
import os


app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_DB'] = 'university'
app.config['MYSQL_DATABASE_USER'] = 'username'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'

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



# RECIEVES USER INPUT AND STORES IT IN THE DATABASE
@app.route('/student/add', methods=['POST'])
def add_student():
    req = request.get_json()
    global email
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

    # QUERY DATABASE
    
    conn = mysql.get_db()
    curr = conn.cursor()
    curr.execute("INSERT INTO student (firstName, middleName, lastName, dateOfBirth, gender, phoneNumber, address, stateOfOrigin, localGovernment, nextOfKin, jambScore, email)" +
    f" VALUES ('{firstName}', '{middleName}', '{lastName}', '{dateOfBirth}', '{gender}', '{phoneNumber}', '{address}', '{state}', '{localGovernment}', '{nextOfKin}', {jambScore}, '{email}');")
    conn.commit()
    curr.close()

    return json.dumps('success')


@app.route('/student/photo', methods=['POST'])
def save_image():
    global email
    photoName = email.split('@')[0]
    image = request.files['file']
    if image:
        filepath = os.path.join(current_app.root_path, f'static/images/{photoName}.jpg')
        image.save(filepath)
        print('success')
    else:
        print('error')

    return 'success'


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')



@app.route('/students/<id>')
def students(id):
    id_number = id
    return render_template('students.html', id_number = id_number)



if __name__ == "__main__":
    app.run(debug=True)
