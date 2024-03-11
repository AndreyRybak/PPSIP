class UserView:
    def render_user(self, user):
        return f"<p>Name: {user.name}, Email: {user.email}</p>"