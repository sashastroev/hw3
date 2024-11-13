class Order:
    '''
    Класс Order
    
    Этот класс представляет заказ товаров.
    
    Метод __ini__:
        Конструктор инициализирует объект класса Order. Содержит атрибут products (список тоаров) 
        и атрибут discount (информация о скидке). 
    
    Метод total_price:
        Функция возвращает сумму по всем товарам с учетом скидки.

    Метод __str__:
        Функция возвращает строковое представление объекта класса Order. Содержит список товаров с ценой. 
        Так же выводит информацию о примененной скидке к заказу. Выводит сумму по всем товарам в заказе (с учетом скидки)
    '''

    def __init__(self, products: list, discount):
        self.products = products
        self.discount = discount

    def total_price(self):
        return sum(self.discount.set_type_discount(product.price, self.discount) for product in self.products)
    
    def __str__(self):
        out = 'товары:'
        for i in self.products:
            out += f'\n\t{i.name} по цене {i.price}'
        out += f'\nПримененная скидка: {self.discount.description} - {self.discount.discount_percent}'
        out += f'\nСумма заказа с учетом скидки: {self.total_price()}'
        return out
    
