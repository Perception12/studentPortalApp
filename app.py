from flask import Flask, render_template, url_for, request, flash

app = Flask(__name__)

@app.route('/')
def index():
     return render_template('index.html')


@app.route('/student/portal')
def portal():
    return render_template('portal.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/students/<id>')
def students(id):
    id_number = id
    return render_template('students.html', id_number = id_number)



if __name__ == "__main__":
    app.run(debug=True)