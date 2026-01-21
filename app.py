from flask import Flask
from models import db
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Dharun@29042005@localhost/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db.init_app(app)
migrate = Migrate(app,db)

@app.route('/')
def server():
    return "DATABASE SERVER"

if(__name__=="__main__"):
    app.run(debug=True)
