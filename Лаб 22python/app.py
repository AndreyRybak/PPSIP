from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    a = "Программа"
    b = "работает"
    result = a + " " + b
    result += " плохо"

    fio = "Рыбак Андрей Иосифович"
    raz = 16 + 5

    arr = [2, -3, 4, -5]

    negative_product = 1

    for num in arr:

        if num < 0:
            negative_product *= num

    # Заданная строка
    S1 = "Рыбак"
    S2 = "  пр. Клецкова 41а"

    # Преобразуем строку в нижний регистр с помощью метода lower()
    lowercase_S1 = S1.lower()

    # Выводим строку в нижнем регистре

    # Используем функцию len() для определения длины строки
    length_S2 = len(S2)

    html_content = f"""
    <html>
    <head><title>Результат выполнения скрипта</title></head>
    <body>
    Задание 2
        <h1>{result}</h1>
        Задание 3
         <h1>{fio}</h1>
         <h1>{raz}</h1>
         Задание 4
         <h1>{arr}</h1>
         <h1>{negative_product}</h1>
         задание 5
         <h1>{length_S2}</h1>
         <h1>{S1+S2}</h1>
         <h1>{lowercase_S1}</h1>
    </body>
    </html>
    """

    return html_content

if __name__ == '__main__':
    app.run(debug=True)
