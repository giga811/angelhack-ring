"""Config"""

### Variables
DATABASE = './database.db'
PER_PAGE = 30
DEBUG = True
SECRET_KEY = 'angelhack' # secret key for app

# mysql settings
MYSQL_DATABASE_HOST = 'localhost'
MYSQL_DATABASE_PORT = 3306
MYSQL_DATABASE_USER = 'angel'
MYSQL_DATABASE_PASSWORD = 'angelring'
MYSQL_DATABASE_DB = 'angelring'
MYSQL_DATABASE_CHARSET = 'utf8'
# format is dialect+driver://username:password@host:port/database
# SQLALCHEMY_DATABASE_URI = 'mysql://ange:angelring@localhost/angelring'
SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite://' + DATABASE