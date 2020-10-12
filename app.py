import numpy as np
from flask import Flask,render_template,redirect,request, url_for
from flask_sqlalchemy import SQLAlchemy
import pickle
app = Flask(__name__,static_folder='static')

# ENV = 'dev'
# if ENV == 'dev':
#     app.debug = True
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/edu_tutoring_platform'

# else:
#     app.debug = False
#     app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Questions(db.Model):
    __tablename__ = 'questions'
    standard = db.Column(db.Integer, primary_key=True)
    qno = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(300))
    answer = db.column(db.String(40))
    subject = db.Column(db.String(25))
    a = db.Column(db.String(100))
    b = db.Column(db.String(100))
    c = db.Column(db.String(100))
    d = db.Column(db.String(100))

    def __init__(self, standard, qno, question, answer, subject, a, b, c, d):
        self.standard  =standard
        self.qno = qno
        self.question = question
        self.answer = answer
        self.subject = subject
        self.a = a
        self.b = b
        self.c = c
        self.d = d

@app.route('/',methods=['GET', 'POST'])
def welcomepage():
    if request.method == 'POST':
        return redirect(url_for('info'))
    return render_template('welcomepage.html')

@app.route('/info')
def info():
    return render_template('info.html')

std=''

@app.route('/submit-info',methods=['GET','POST'])
def submit_info():
    if request.method == 'POST':
        global std
        name=request.form['name']
        std=int(request.form['class'])
        state=request.form['state']
        takeassmnt=request.form['take-asmnt']
        if takeassmnt=='yes':
            # print(db.session.query(Questions).filter(Questions.standard==8 and Questions.qno==5).all())
            return redirect(url_for('assessment'))
        else:
            print(std)
            return redirect(url_for('teachers'))

# ques=db.session.query(Questions).filter(Questions.standard == std ).first().question

@app.route('/assesment')
def assessment():
    return render_template('assessment.html')

@app.route('/teachers')
def teachers():
    return render_template('teachers.html')


if __name__ == '__main__':
    app.run(debug=True)