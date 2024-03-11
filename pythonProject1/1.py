from your_app.models import User, Account

# Создание пользователя
tom = User.objects.create(name="Tom")

# Создание объекта Account
acc = Account(login="1234", password="6565")

# Привязка аккаунта к пользователю
tom.account = acc

# Сохранение аккаунта
acc.save()

# Изменение логина и пароля аккаунта
tom.account.login = "qwerty"
tom.account.password = "123456"

# Повторное сохранение аккаунта
tom.account.save()
