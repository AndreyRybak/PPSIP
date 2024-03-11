from flask import Flask, render_template, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Получаем текущую дату
    current_date = datetime.datetime.now().strftime("%d.%m.%Y")
    return render_template('index.html', date=current_date)

@app.route('/get_date', methods=['GET'])
def get_date():
    # Получаем текущую дату
    current_date = datetime.datetime.now().strftime("%d.%m.%Y")
    return jsonify({'date': current_date})

if __name__ == '__main__':
    app.run(debug=True)
