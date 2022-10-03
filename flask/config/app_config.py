from flaskext.mysql import MySQL
import time


class AppConfig:

    def __init__(self, app):
        app.config['MYSQL_DATABASE_USER'] = 'root'
        app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
        app.config['MYSQL_DATABASE_DB'] = 'songs'
        app.config['MYSQL_DATABASE_HOST'] = 'db'
        app.config['MYSQL_DATABASE_PORT'] = 3306
        mysql = MySQL()
        # Not the best way to do it,
        # but sleep ensures that mysql image is going to be up working
        # when Flask tries to connect to it
        time.sleep(20)
        mysql.init_app(app)
        self._cursor = mysql.connect().cursor()
        self._app = app

    @property
    def cursor(self):
        return self._cursor

    @property
    def app(self):
        return self._app
