import os
basedir = os.path.abspath(os.path.dirname(__file__))
CSRF_ENABLED = True
SECRET_KEY = 'youshouldchangethis' 

# email server
#MAIL_DEBUG = True
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'flaskdemowithgit@google.com'
MAIL_PASSWORD = 'passwordgoeshere'

