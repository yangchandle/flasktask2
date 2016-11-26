# project/form.py 

from flask_wtf  import Form
from wtforms import StringField, DateField, IntegerField, \
        SelectField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo

class AddTaskForm(Form):
    task_id = IntegerField()
    name = StringField('Task Name', validators=[DataRequired()])
    due_date = DateField(
            'Date Due (mm/dd/yyyy)',
            validators=[DateRequired()], format='%m/%d/%y'
    )
    priority = SelectField(
            'Priority',
            validators=[DataRequired()],
            choices=[
               ('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'), ('7', '7'),('8', '8'),('9', '9'),('10', '10')
        ] 
    )
     
    status = IntegerField('Status')

class RegisterForm(Form):
    name = StringField(
            'username',
            validators=[DataRequired(),Length(min=6, max=25)]
    )
    email = StringField(
            'Email',
            validators=[DataRequired(), Length(min=6, max =40)]
    )
    password = PasswordField(
            'password',
            validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField(
            'Report Password',
            validators=[DateRequired(), EqualTo('password', message='Password must match')]
    )


class LoginForm(Form):
    name = StringField(
            'username',
            vlidators=[DataRequired()]
     )
    password = PasswordField(
            'password',
            validators=[DataRequired()]
    )


