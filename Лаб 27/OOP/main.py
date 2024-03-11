from flask import Flask, render_template

app = Flask(__name__)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info_html(self):
        return f"<p>Name: {self.name}, Age: {self.age}</p>"

@app.route('/')
def index():
    # Создаем экземпляр класса Person
    person = Person("Andrew Rybak", 20)
    # Получаем HTML-код информации о персоне
    person_info_html = person.info_html()
    return render_template('index.html', person_info_html=person_info_html)

if __name__ == '__main__':
    app.run(debug=True)
