from flask_cors import CORS
from flaskext.mysql import MySQL


class AppConfig:

    def __init__(self, app):
        app.config['MYSQL_DATABASE_USER'] = 'televiones'
        app.config['MYSQL_DATABASE_PASSWORD'] = 'televiones'
        app.config['MYSQL_DATABASE_DB'] = 'songs'
        app.config['MYSQL_DATABASE_HOST'] = 'db'
        mysql = MySQL()
        mysql.init_app(app)
        CORS(app)
        self._cursor = mysql.connect().cursor()
        self._app = app

    @property
    def cursor(self):
        return self._cursor

    @property
    def app(self):
        return self._app
