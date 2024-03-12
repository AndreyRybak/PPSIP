from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    a = "Программа"
    b = "работает"
    result = a + " " + b
    result += " плохо"

    html_content = f"""
    <html>
    <head><title>Результат выполнения скрипта</title></head>
    <body>
        <h1>{result}</h1>
    </body>
    </html>
    """

    return html_content

if __name__ == '__main__':
    app.run(debug=True)
