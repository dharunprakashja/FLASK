from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def hello():
    return "HELLO FLASK"

@app.route("/home")
def home():
    return render_template("home.html",language = "javascs",numbers = [1,2,3,4,5])


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

@app.route('/page1')
def page1():
    return render_template("page1.html")

@app.route('/page2')
def page2():
    return render_template("page2.html")

@app.route('/temp')
def temp():
    return render_template("temp.html",d = "DHAROO", a = 40)

@app.template_filter()
def double(a):
    return a*2

@app.route('/card')
def card():
    return render_template("macrocard.html")

if(__name__ == '__main__'):
    app.run(port=8000,debug=True)