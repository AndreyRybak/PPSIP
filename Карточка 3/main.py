from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        maiden_name = request.form.get('maiden_name', '')
        army = 'Да' if 'army' in request.form else 'Нет'
        military_rank = request.form.get('military_rank', '')

        # Запись данных в файл
        with open('fio.txt', 'a') as file:  # 'a' - режим добавления (добавление в конец файла)
            file.write(f'Имя: {name}\n')
            file.write(f'Пол: {gender}\n')
            file.write(f'Девичья фамилия: {maiden_name}\n')
            file.write(f'Служил в армии: {army}\n')
            file.write(f'Воинское звание: {military_rank}\n\n')

        return render_template('result.html', name=name, gender=gender, maiden_name=maiden_name, army=army, military_rank=military_rank)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
