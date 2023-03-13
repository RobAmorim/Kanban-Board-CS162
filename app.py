from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
from datetime import datetime
import os 

def create_app():
    app = Flask(__name__)
    app.app_context().push()

    return app

#app instance 
app = create_app()
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
db = SQLAlchemy()


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(200))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

db.init_app(app)
db.create_all()


#calls our main page acessing the url "/"
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        task_status = "todo"
        new_task = Todo(content=task_content, status=task_status)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        # tasks = Todo.query.order_by(Todo.date_created).all()
        todo_tasks = Todo.query.filter_by(status='todo').all()
        inprogress_tasks = Todo.query.filter_by(status='inprogress').all()
        done_tasks = Todo.query.filter_by(status='done').all()
        
        return render_template('index.html', todo_tasks=todo_tasks, inprogress_tasks=inprogress_tasks, done_tasks=done_tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task=task)
    
@app.route('/forward/<int:id>', methods=['GET', 'POST'])
def forward(id):
    task = Todo.query.get_or_404(id)

    if task.status == 'todo':
        task.status = 'inprogress'

    elif task.status == 'inprogress':
        task.status = 'done'

    try:
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue moving your task'

@app.route('/backward/<int:id>', methods=['GET', 'POST'])
def backward(id):
    task = Todo.query.get_or_404(id)

    if task.status == 'inprogress':
            task.status = 'todo'

    elif task.status == 'done':
        task.status = 'inprogress'

    try:
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue moving your task'



if __name__ == "__main__":
    app.run(debug=True, port=5300)


