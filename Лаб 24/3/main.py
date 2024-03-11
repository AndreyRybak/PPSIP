from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Замените на ваш секретный ключ

# Пароль для входа в административную часть
ADMIN_PASSWORD = 'admin'

# Функция проверки авторизации
def check_auth():
    return session.get('logged_in')

# Маршрут для отображения главной страницы
@app.route('/')
def index():
    return render_template('index.html', logged_in=check_auth())

# Маршрут для входа в административную часть
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form['password']
        if password == ADMIN_PASSWORD:
            session['logged_in'] = True
            return redirect('/')
    return render_template('login.html')

# Маршрут для выхода из административной части
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
