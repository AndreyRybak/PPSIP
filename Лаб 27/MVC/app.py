from flask import Flask, render_template
from controller import UserController

app = Flask(__name__)
controller = UserController()

@app.route('/')
def index():
    user_info_html = controller.show_user()
    return render_template('index.html', user_info_html=user_info_html)

if __name__ == "__main__":
    app.run(debug=True)
