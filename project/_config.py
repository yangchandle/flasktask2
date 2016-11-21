# project/_config.py


import os


# grab the folder where thsi script lives
basedir = os.path.abspath(os.path,dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNMAE ='admin'
PASSWORD = 'admin'
CSRF_ENABLED = True
SECRET_KEY = 'my_precious'

# define the full path for the datebase
DATABASE_PATH = os.path.join(basedir, DATABASE)

# the database uri
SQLACHEMY_DATABASE_URI ='sqlite:///' + DATABASE_PATH

