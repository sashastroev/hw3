class Product:
    '''
    Класс Product

    Этот класс представляет товар в интернет-магазине.

    Метод __init__:
        Конструктор инициализирует объект Product с двумя атрибутами: name (название товара) и price (цена товара).
        Пример: product1 = Product("Laptop", 1000) создаст товар с названием "Laptop" и ценой 1000.

    Метод __str__:
        Возвращает строковое представление объекта с указанием наименования товара и его цены
    '''
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f'Товар {self.name} по цене {self.price}'