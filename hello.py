x = int(input("Введите количество продуктов: "))
total_price = []
list_product = []

for i in range(1, x + 1):
    product = input(f"Название {i} продукта: ")
    price = int(input("Цена продукта: "))
    list_product.append(product)
    total_price.append(price)

print()
print("Список продуктов")

for i in range(x):
    print(f"{list_product[i]} / {total_price[i]} руб.")

print()
sum_purchase = sum(total_price)

print(f"Итого: {sum_purchase} руб.")