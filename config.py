import os
basedir = os.path.abspath(os.path.dirname(__file__))
#SRF_ENABLED = True
WTF_CSRF_ENABLED = True
SECRET_KEY = 'THIS-IS-AMAZING-KEY'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True