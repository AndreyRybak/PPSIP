from flask import Flask, render_template
import datetime
import locale

app = Flask(__name__)

@app.route('/')
def index():
   # locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

    current_datetime = datetime.datetime.now()


    formatted_date = current_datetime.strftime("%d. %m. %Y")


    formatted_time = current_datetime.strftime("%H:%M:%S")


    day_of_week = current_datetime.strftime("%A")


    return render_template('index.html', date=formatted_date, time=formatted_time, day=day_of_week)

if __name__ == '__main__':
    app.run(debug=True)
