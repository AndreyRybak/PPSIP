from flask import Flask, session, render_template

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Замените на ваш секретный ключ

@app.route('/')
def index():
    # Устанавливаем значение для ключа 'username' в сессии
    session['username'] = "Андрей"
    # Рендерим шаблон index.html, передавая имя пользователя
    return render_template('index.html', username=session['username'])

if __name__ == '__main__':
    app.run(debug=True)
