# Бесконечный цикл для ввода количества продуктов
while True:
    try:
        n = input("Введите количество продуктов: ").strip()
        # Проверяем, не пустая ли строка
        if n == "":
            print("Список не может быть пустым.")
            continue
        else:
            # Преобразуем ввод в целое число
            qua = int(n)
            # Проверяем, что число положительное
            if qua < 0:
                print("Количество не может быть меньше 0.")
                continue
            else:
                break
    except ValueError:
        print("Ошибка! Введите число.")
        continue

# Создаем пустые списки для хранения данных
products = []
price = []

# Цикл для ввода названий продуктов
for i in range(qua):
    while True:
        name = input(f"Введите название {i + 1} продукта: ").strip()
        # Проверяем, не пустая ли строка
        if name == "":
            print("Название продукта не может быть пустым.")
            continue

        products.append(name)
        break

# Цикл для ввода цен на продукты
for bye_name in products:
    while True:
        try:
            y = input(f"Введите цену продукта {bye_name}: ").strip()
            if not y:
                print("Цена не может быть пустой.")
                continue
            else:
                bye = int(y)
                if bye <= 0:
                    print("Цена должна быть больше нуля.")
                    continue
                else:
                    price.append(bye)
                    break

        except ValueError:
            print("Ошибка! Введите число.")

print()
print("Список (продукт / цена): ")
for pr in range(qua):
    print(f"{products[pr]} / {price[pr]}руб.")

summ = sum(price)
average =  summ / qua
min_ = min(price)
max_ = max(price)
print()
print(f"Минимальная цена продукта: {min_}руб.")
print(f"Максимальная цена продукта: {max_}руб.")
print(f"Средняя цена продукта: {average}руб.")
print()
print(f"Итог: {summ}руб.")