class Order:
    '''
    Класс Order
    
    Этот класс представляет заказ товаров
    
    Метод __ini__:
        содержит атрибут products (список тоаров)
    
    '''

    def __init__(self, products: list, discount):
        self.products = products
        self.discount = discount

    def total_price(self):
        return sum(product.price for product in self.products) * (1 - self.discount.discount_percent / 100)
    
    def __str__(self):
        out = 'товары:'
        for i in self.products:
            out += f'\n\t{i.name} по цене {i.price}'
        out += f'\nПримененная скидка: {self.discount.description} - {self.discount.discount_percent}'
        out += f'\nСумма заказа с учетом скидки: {self.total_price()}'
        return out
    
