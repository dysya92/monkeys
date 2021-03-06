import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'this-is-too-difficult'
POSTS_PER_PAGE = 5

if os.environ.get("DATABASE_URL") is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
