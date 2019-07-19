from flask import Flask#1
app=Flask(__name__)#3
@app.route('/')
def hello():
    return "welcome to MY NEW Flask Application"
@app.route('/he')
def he():
    s="Srinivas Reddy"
    return '<h1> Hi '+s,'</h1>'

if __name__=='__main__':#2
    app.run(debug=True)
