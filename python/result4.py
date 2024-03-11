arr = [2, -3, 4, -5]

negative_product = 1

for num in arr:

    if num < 0:
        negative_product *= num


print("Произведение отрицательных элементов:", negative_product)
