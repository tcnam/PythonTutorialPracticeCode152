import csv

class Item:
    # class attributes not instance attributes
    pay_rate=0.8
    all_items=[]

    # constructor
    def __init__(self, name:str, price:float, quantity:int=0):
        # Run validations to the received arguments
        assert price >=0, f"Price {price} is not greater than 0"
        assert quantity>=0, f"Quantity {quantity} is not greater than 0"

        # Assign to self object
        self.__name=name
        self.__price=price
        self.__quantity=quantity 

        # Actions to execute
        Item.all_items.append(self)

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    @name.setter
    def name(self, value):
        self.__name=value

    def calculate_total_price(self):
        return self.__quantity*self.__price

    def apply_discount(self):
        self.price=self.__price* Item.pay_rate

    @staticmethod                   # like isolated function, don't use class or instance as argument
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()

    @classmethod
    def instantiate_from_csv(cls):   # use class as first argument not instance
        with open('item.csv','r') as f:
            reader = csv.DictReader(f)
            items=list(reader)

        for item in items:
            Item(
                str(item.get('name')),
                float(item.get('price')),
                int(item.get('quantity')),
            )
 
    def __repr__(self):
        return f"Item ('{self.__name}', {self.__price},{self.__quantity})"

"""
Item.instantiate_from_csv()
for instance in Item.all_items:
    print(instance.name)
print(Item.is_integer(7.5))
"""    
