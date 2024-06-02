from flask import Flask, render_template
from random import choice

app = Flask(__name__)


@app.route('/')
def hello():
    return 'БГИТУ лучшие'


@app.route('/ist/')
def hello_ist():
    user = {'username': 'Cтанислав'}
    title_sp = ("Олень", 'Деноминация', 'Феррари')
    return render_template('index.html', title=choice(title_sp), user=user)

@app.route('/privet/')
def greeting():
    return '<h2> Здравствуй милый друг </h2>'


@app.route('/<user>/')
def users(user):
    return f'<h2> Здравствуй наш пользователь {user} </h2>'


@app.route('/<int:id>/')
def users_id(id):
    return f'<h2> Ваш номер после номера {id} </h2>'


if __name__ == '__main__':
    app.run(debug=True)