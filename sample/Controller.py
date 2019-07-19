from flask import Flask,flash,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mydb1.sqlite3'
db=SQLAlchemy(app)

class Sample(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(100))
	email=db.Column(db.String(50))
	phno=db.Column(db.String(200))
	pswd=db.Column(db.String(20))

	def __init__(self,name,email,phno,pswd):
		self.name=name
		self.email=email
		self.phno=phno
		self.pswd=pswd



@app.route('/welcome/<name>')
def Name(name):
	#name="Srinivas Reddy"
	return "<h1>welcome  "+name+"</h1>"
@app.route('/welcome/<name>/<int:roll>')



def Msg(name,roll):
	#name="Srinivas Reddy"
	#return "<h1>welcome  "+name+"</h1>"
	return "<h1>welcome to {} and my number {} </h1>".format(name,roll)

@app.route('/')
def Message():
	return "<h1>welcome to Python Flask</h1>"

@app.route('/home')
def home():
	return redirect(url_for('Message'))

@app.route('/Student')
def Student():
	return "<h1>Welcome to Student</h1>"

@app.route('/Admin')
def Admin():
	return '<h1>Welcome to Admin</h1>'

@app.route('/Lib')
def Lib():
	return "<h1>welocme to Lib</h1>"

@app.route('/User/<name>')
def User(name):
	if name=='Student':
		return redirect(url_for("Student"))
	elif name=='Admin':
		return redirect(url_for("Admin"))
	elif name=="Lib":
		return redirect(url_for("Lib"))

@app.route('/MyHtml')
def MyHtml():
	return render_template("sample.html")
	 
@app.route('/MyHtml1/<name>')
def MyHtml1(name):
	return render_template("sample.html",name1=name)

@app.route('/retrive')
def retrive():
	return render_template("sample1.html",data=Sample.query.all())


@app.route('/mypage/register',methods=["POST",'GET'])
def register():
	if request.method=="POST":
		Name=request.form['name']
		Email=request.form['email']
		Mobile=request.form['mobile']
		Pswd=request.form['pswd']

		data=Sample(Name,Email,Mobile,Pswd)
		db.session.add(data)
		db.session.commit()

		return "<h2>Record Stored</h2>"
		#print(Name,Email,Mobile,Pswd)
		#flash("Registraion completed,you can login")
		#return render_template("login.html")
	flash("U Can Reigister")
	return render_template('register.html')

@app.route('/mypage/login',methods=["POST","GET"])
def login():
	if request.method=="POST":
		Email=request.form['email']
		Pswd=request.form['pswd']
		#print(Email,Pswd)
		#flash("")



	return render_template('login.html')


if __name__=='__main__':
	app.secret_key="ad"
	db.create_all()
	app.run(debug=True)
