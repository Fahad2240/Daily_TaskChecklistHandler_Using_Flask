from doctest import debug
from multiprocessing import context
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite'
db=SQLAlchemy(app)
class TaskManager(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(255))
    complete=db.Column(db.Boolean)
    

@app.route("/")
def home():
    task_list=TaskManager.query.all()
    # print(task_list)
    return render_template('base.html',task_list=task_list)
@app.route("/about")
def about():
    return "<h1>About Page.Learn Flask"
with app.app_context():
    db.create_all()
    # new_task=TaskManager(title='Task 1',complete=False)
    # db.session.add(new_task)
    # db.session.commit()

if __name__ =='__main__':
    app.run(debug=True)
