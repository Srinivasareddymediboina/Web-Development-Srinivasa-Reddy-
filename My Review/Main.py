from flask import *
app=Flask(__name__)


@app.route('/register')
def register():
	return render_template("register.html")

@app.route('/login')
def login():
	return render_template("login.html")

@app.route('/details',methods=['POST','GET'])
def details():
	if request.method=="POST":
		Name=request.form['name']
		Email=request.form['email']
		Mobile=request.form['mobile']
		Pswd=request.form['pswd']


	return render_template("details.html",n=Name,e=Email,m=Mobile,p=Pswd)
@app.route('/logindetails',methods=['POST','GET'])
def logindetails():
	if request.method=="POST":
		#Name=request.form['name']
		Email=request.form['email']
		#Mobile=request.form['mobile']
		Pswd=request.form['pswd']


	return render_template("logindetails.html",e=Email,p=Pswd)
	

if __name__=='__main__':
	app.run(debug=True)