# Импортируем необходимые библиотеки
import base64

# Открываем изображение и читаем его в бинарном режиме
with open("image.png", "rb") as image_file:
    # Кодируем изображение в формат base64
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

# HTML-шаблон с вставкой изображения
html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Картинка</title>
</head>
<body>
    <h1>Моя картинка</h1>
    <img src="data:image/jpeg;base64,{encoded_string}" alt="Картинка">
</body>
</html>
"""

# Сохраняем HTML в файл
with open("index.html", "w") as html_file:
    html_file.write(html_template)

print("HTML-файл с изображением успешно создан!")
