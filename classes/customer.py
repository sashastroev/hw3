from classes.discount import Discount

class Customer:
    '''
    Класс Customer
    
    Класс представляет собой информацию о покупателе с атрибутами name и order
    
    Метод __ini__:
        Конструктор инициализирует объект класса Customer с двумя атрибутами: name (имя покупателя) 
        и orders (список заказов этого покупателя).

    Метод count_orders:
        Функция возвращает количество заказов у покупателя (объекта класса Custoner)

    Метод sum_orders:
        Функция возвращает сумму по всем заказам у покупателя (объекта класса Custoner)
    
    Метод __str__:
        Функция возвращает строковое представление объекта Customer и содержит имя клиента и список товаров с ценой со скидкой. 
        Так же выводит сумму по всем заказам клиента с учетом скидки.
        Если заказов у клиента нет, то выводит вместо списка заказов сообщение: Заказов пока не  было
    '''
    
    def __init__(self, name: str, orders):
        self.name = name
        self.orders = orders
    
    def count_orders(self):
        return len(self.orders.products)
    
    def sum_orders(self):
        return self.orders.total_price()
    
    def __str__(self):
        out = f'\nИмя: {self.name}'
        if self.orders != []:
            for i in self.orders.products:
                final_price = Discount.set_type_discount(i.price, self.orders.discount)
                out += f'\n\tТовар {i.name} со скидкой {final_price}'
            out += f'\nСумма заказов с учетом скидки: {self.orders.total_price()}'
        else:
            out += '\n\tЗаказов пока не  было'
        return out
    