class Discount:
    '''
    Класс Discount

    Предаставляет собой информацию о скидке на товар.

    Метод __init__:
        конструктор объекта класса Discount с атрибутами description (описание скидки) 
        и discount_percent (процент скидки).

    Метод set_type_discount:
        Статическая функция. Принимает цену и скидку. Возвращает цену с учетом скидки.

    Метод __str__:
        Функция возвращает строковое представление объекта класса Discount. 
        Возвращает наименование скидки и величину скидки в %
    '''
    def __init__(self, description: str, discount_percent: int):
        self.description = description
        self.discount_percent = discount_percent

    @staticmethod
    def set_type_discount(price: float, discount):
        return price * (1 - discount.discount_percent / 100)
    
    def __str__(self):
        return f'{self.description}: {self.discount_percent}%'