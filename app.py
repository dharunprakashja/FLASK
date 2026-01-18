from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def hello():
    return "HELLO FLASK"

@app.route("/home")
def home():
    return render_template("home.html")

@app.route('/contact/')
def contact():
    print(request.args)
    print(request.args['name'])
    print(request.args.get('age'))
    return render_template("contact.html")

@app.route('/about/<int:age>')
def about(age):
    print("AGE",age)
    return render_template("about.html")

if(__name__ == '__main__'):
    app.run(port=8000,debug=True)