from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import db, Details
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Dharun29042005@localhost/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def server():
    return "DATABASE SERVER"


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        data = request.json
        data = request.json
        form_name = data["name"]
        form_age = data["age"]
        print(data)
        print(form_name)
        print(form_age)
        new_details = Details(name=form_name, age=form_age)

        db.session.add(new_details)
        db.session.commit()

    return jsonify({"status":"Success"})


@app.route('/test')
def test():
    data = {"message": "Hello", "status": "success"}
    return jsonify(data)


@app.route('/table')
def table():
    data = Details.query.all()
    box = []
    for d in data:
        box.append({"id":d.id,"name": d.name, "age": d.age})
    print(box)
    return jsonify(box)


@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    data = Details.query.get(id)

    if (request.method == 'POST'):
        data.name = request.json['name']
        data.age = request.json['age']
        db.session.commit()

    return jsonify({"status":"success"})


@app.route('/delete/<int:id>',methods=['DELETE'])
def delete(id):
    data = Details.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return jsonify({"delete":"sucess"})


if (__name__ == "__main__"):
    app.run(debug=True)
