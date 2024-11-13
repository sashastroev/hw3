class Discount:
    '''
    Класс Discount

    Предаставляет собой информацию о скидке на товар.

    Метод __init__:
        конструктор объекта класса Discount с атрибутами description (описание скидки) 
        и discount_percent (процент скидки).
    '''
    def __init__(self, description: str, discount_percent: int):
        self.description = description
        self.discount_percent = discount_percent

    @staticmethod
    def set_type_discount(price: float, discount):
        return price * (1 - discount.discount_percent / 100)
    
    def __str__(self):
        return f'{self.description}: {self.discount_percent}%'