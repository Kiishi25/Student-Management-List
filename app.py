from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import  SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField #Frame Agnostic Form system
from wtforms.validators import DataRequired #Check if something has been write
from werkzeug.security import generate_password_hash, check_password_hash



#from app import db

app = Flask(__name__) 
#Add Database
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/student_list"
#Initialize Database
db = SQLAlchemy(app)
app.app_context().push()
app.config['SECRET_KEY'] = "super secret key" #Key no one is suppose to know


#Initialize Database



# Create Model
class Students(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    dob = db.Column(db.DateTime(200), nullable=False)
    email_Address = db.Column(db.String(200), nullable=False, unique=True)
    password_hash = db.Column(db.String(176))

    


class Courses(db.Model):
    course_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)

class Grades(db.Model):
    grad_id = db.Column(db.Integer, primary_key=True)
    percentage = db.Column(db.Float, nullable=False)

    db.init_app(app)

    def __ini__(self,first_name,last_name,address,dob,email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email_Address = email_address


#Create a form class
class StudentForm(FlaskForm):
    first_name = StringField("Enter your first name", validators=[DataRequired()])
    last_name = StringField("Enter your last name", validators=[DataRequired()])
    address = StringField("Enter your address", validators=[DataRequired()])
    dob = StringField("Enter your date of birth", validators=[DataRequired()])
    email = StringField("Enter your email address", validators=[DataRequired()])
    submit = SubmitField("Submit")

    

    
@app.route("/")
def home():
    data_students = db.session.query(Students)

    return render_template ('index.html', data=data_students)

@app.route("/input",methods=['GET', 'POST'])
def input_data():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        address = request.form['address']
        dob= request.form['telp']
        email_address = request.form['email_address']
        
        

        add_data = Students(first_name, last_name,address,dob,email_address)
        
        db.session.add(add_data)
        db.session.commit()


        return redirect(url_for('index'))

    return render_template('input.html')
    return render_template ('input.html', first_name=first_name, form = form)

