from flask import Flask

from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'


def main():
    db_session.global_init("db/data.sqlite")
    db_file = ("db/docs.db")
    app.run(port=8080, host='127.0.0.1')  # , debug=True)


if __name__ == '__main__':
    main()
