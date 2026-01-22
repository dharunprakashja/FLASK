from flask import Flask, render_template, request, redirect, url_for
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
        form_name = request.form['name']
        form_age = request.form['age']
        print(form_name, form_age)
        new_details = Details(name=form_name, age=form_age)

        db.session.add(new_details)
        db.session.commit()
        return redirect(url_for('table'))

    return render_template('form.html')


@app.route('/table')
def table():
    data = Details.query.all()
    return render_template('table.html', details=data)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    data = Details.query.get(id)

    if (request.method == 'POST'):
        data.name = request.form['name']
        data.age = request.form['age']
        db.session.commit()
        return redirect(url_for('table'))

    return render_template('edit.html', detail=data)


@app.route('/delete/<int:id>')
def delete(id):
    data = Details.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('table'))


if (__name__ == "__main__"):
    app.run(debug=True)
