from flask import Flask,render_template,url_for,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///collegeinfo.db"

mydb=SQLAlchemy(app)
#database connection
class Signup(mydb.Model):
	id=mydb.Column(mydb.Integer,primary_key=True)
	s_name=mydb.Column(mydb.String(200))
	roll_no=mydb.Column(mydb.String(50))
	mail_id=mydb.Column(mydb.String(50))
	phone_no=mydb.Column(mydb.String(50))
	branch=mydb.Column(mydb.String(50))
	def __init__(self,name,rollno,emailid,phno,branch):
		self.s_name=name
		self.roll_no=rollno
		self.mail_id=emailid
		self.phone_no=phno
		self.branch=branch

@app.route('/myportal/signup',methods=['POST','GET'])
def signup():
	if request.method=="POST":
		#data=request.form
		stu_name=request.form['sname']
		stu_rollno=request.form['rollno']
		stu_email=request.form['email']
		stu_phno=request.form['phno']
		stu_branch=request.form['branch']

		sgn = Signup(stu_name,stu_rollno,stu_email,stu_phno,stu_branch)
		mydb.session.add(sgn)
		mydb.session.commit()
		return render_template('status.html')
		#print(stu_name,stu_rollno,stu_email,stu_phno,stu_branch)
	return render_template("signup.html")

@app.route('/myportal/studentList',methods=['POST','GET'])
def display():


	return render_template('showDetails.html',data=Signup.query.all())

if __name__=="__main__":
	mydb.create_all()
	app.run(debug=True)