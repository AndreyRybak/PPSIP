from flask import Flask, session, render_template

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Замените на ваш секретный ключ

@app.route('/index2')
def index2():
    # Получаем значение 'username' из сессии
    username = session.get('username', 'Гость')
    # Рендерим шаблон page2.html, передавая имя пользователя
    return render_template('index2.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
