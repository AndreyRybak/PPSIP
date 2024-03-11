from model import UserModel
from view import UserView

class UserController:
    def __init__(self):
        self.model = UserModel("Andrew Rybak", "2003ryba@gmail.com")
        self.view = UserView()

    def show_user(self):
        user_info = self.model
        return self.view.render_user(user_info)