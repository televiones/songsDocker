import os

from flask import Flask, jsonify, Response

from config.app_config import AppConfig

app = AppConfig(Flask(__name__))
flask_app = app.app
cursor = app.cursor


def get_songs() -> list[dict]:
    cursor.execute('SELECT * FROM song')
    results = parse_json([x[0] for x in cursor.description], cursor.fetchall())
    cursor.close()
    cursor.close()
    return results


@flask_app.route("/")
def index():
    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")

    if app_name:
        return f"Hello from {app_name} running in a Docker container behind Nginx!"

    return "Hello from Flask"


@flask_app.route('/db')
def index_db() -> Response:
    return jsonify(get_songs())


def parse_json(headers, datasource):
    return [dict(zip(headers, result)) for result in datasource]


if __name__ == '__main__':
    flask_app.run(host='localhost', port=8080)
