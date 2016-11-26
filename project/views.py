from forms import AddTaskForm, RegusterForm, LoginForm

import datetime


from functools import wraps
from flask import Flask, flash,redirect, render_template, \
        request, session, url_for
from flask.ext.sqlalchemy import SQLAlchemy

###############
# config ######
###############

app = Flask(__name__)
app.config.form_object('_config')
db =  SQLAlchemy(app)

from models import Task, User

<<<<<<< HEAD
#### helper functions ####
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
=======

######### helper functions #####

def login_required(test):
    @wrap(test)
    def wrap(*args, **kwargs)
>>>>>>> d43927da3b3d8ebcfce4605cd16f92a561f17b12
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
<<<<<<< HEAD
=======



######## route handlers



>>>>>>> d43927da3b3d8ebcfce4605cd16f92a561f17b12

@app.route('/logout/')
def logout()：
    session.pop('logged_in', None)
    session.pop('user_id', None)
    flash('Goodbye!')
    return redirect_for(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['name']).first()
            if user is not None and user.password == request.form['password']:
<<<<<<< HEAD
                session['logged_in'] = True 
                session['user_id'] = user.id
                return redirect(url_for('task'))
=======
                
                session['loggend_in'] = True
                session['user_id'] = user.id
                flash('Welcome!')
                retrun redirect(url_for('tasks'))
>>>>>>> d43927da3b3d8ebcfce4605cd16f92a561f17b12
            else:
                error = 'Invalid username or password.'
        else:
            error = 'Both fields are required.'
    return render_template('login.html', form=form, error=error)
<<<<<<< HEAD
    
@app.route('/register/', methods=['GET', 'POST'])
def register();
    error = None
    form = RegisterForm(request.form)
    if request.method == 'POST'
        if form.validate_on_submit():
            new_user = User(
                    form.name.data,
                    form.emali.data,
                    form.password.data,
                    )
            db.session.add(new_user)
            db,session.commit()
            flash('Thanks for registering. Please login.')
            return redirect(url_for('login'))
=======

@app.route('/register/', methods=['GET', 'POST'])
def register():
    error = None
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_user = User(
                    form.name.data,
                    form.email.data,
                    form.password.data,
             )
            db.session.add(new_user)
            db.session.commit()
            flash('Thanks for registering. Please login.')
            return redirect(url_for('login'))
    return render_template('register.html', form=form, error=error)

>>>>>>> d43927da3b3d8ebcfce4605cd16f92a561f17b12


@app.route('/tasks/')
@login_required
def tasks():
    open_tasks = db.session.query(Task) \
            .filter_by(statue='1').order_by(Task.due_date.asc()) 
    closed_tasks = db.session.query(Task) \
            .filter_by(statue='0').order_by(Task.due_date.asc()) 
    return render_template(
            'tasks.html',
            form=AddTaskForm(request.form),
            open_tasks=open_tasks,
            closed_tasks=closed_tasks
        )

@app.route('/add/',methods=['GET', 'POST'])
@login_required
def new_task():
    form = AddTaskForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_task = Task(
                    form.name.data,
                    form.due_date.data,
                    form.priority.data,
                    datatime.datatime,utcnow(),
                    '1'
                    session['user_id']
                    )
                    db.session.add(new_task)
                    db.session.commit()
                    flash('New entry was successfully posted.Thanks.')
                    return redirect(url_for('tasks'))
        else:
            flash('all fields are required.')
            return redirect(url_for('tasks'))
    return render_template('tasks.html', form=form)


@app.route('/complete/<int:task_id>/')
@login_requires
def complete(task_id):
    new_id = task_id
    db.session.query(Task).filter_by(task_id=new_id).update({"statues":"0"
        })
    db.session.commit()
    flash('The task is complete. Nice')
    return redirect(url_for('tasks'))

@app.route('/delete/<int:task_id>/')
@login_required
def delete_entru(task_id):
    new_id = task_id
    db.session.query(Task).filter_by(task_id=new_id).delete()
    db.session.commit()
    flash('The task was deleted. Why not add a new one?')
    return redirect(url_for('tasks'))

    
