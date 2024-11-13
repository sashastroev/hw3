from random import randint
from random import choice
#  Импортируем наши классы
from classes.customer import Customer
from classes.product import Product
from classes.order import Order
from classes.discount import Discount

# Создадим константу, которая будет определять сколько заказов мы создаим
COUNT_ORDERS = 3 

# создаем словарь товаров, скидок
product_dict = {'car': 10000, 'moto': 5000, 'bicycle': 1000, 'scooter': 2000, 'shoes': 200}
discount_dict = {'начальная скидка': 10, 'средняя скидка': 20, 'высокая скидка': 30, 'оптова скидка': 40}
# Создадим список имен клиентов
names_list = ['Mikhail', 'Stepan', 'Leonid']

# Получаем список с объектами класса Product и выводим его
product_list = []
print('\nНаш список товаров:\n')
for key, val in product_dict.items():
    product_list.append(Product(key, val))
    print(product_list[-1])

# Получаем список с объектами класса Discount и выводим его
discount_list = []
print('\nНаш список скидок:\n')
for key, val in discount_dict.items():
    discount_list.append(Discount(key, val))
    print(discount_list[-1])

# Получаем список с объектами класса Order. Создаем некоторое количество заказов. В каждом заказе 
# будем циклом добавлять случайное количество товаров. Сами товары тоже выбираем случайтым образом из списка товаров
# Так же будем применять случайные скидки к заказм
# Выведем список заказов на экран
order_list = []
print('\nНаши заказы:')
for i in range(COUNT_ORDERS):
    print(f'\nЗаказ №{i+1}:')
    this_order_list = []
    this_discount = choice(discount_list)    
    for j in range(randint(1, 3)):
        this_product = choice(product_list)
        this_order_list.append(this_product)
    order_list.append(Order(this_order_list, this_discount))
    print(order_list[-1])

# Создаем список с объектами класса Customer
customer_list = []
print('\nНаши клиенты:')
for i in names_list:
    customer_list.append(Customer(i, choice(order_list)))
    print(customer_list[-1])

# Посчитаем общее количество заказов и сумму всех заказов для всех клиентов.
qount_all_orders = 0
summ_all_orders = 0
for customer in customer_list:
    qount_all_orders += customer.count_orders()
    summ_all_orders += customer.orders.total_price()
print(f'\n\nОбщее количество заказов: {qount_all_orders}')
print(f'Сумма по всем заказам с учетом скидки: {summ_all_orders}')