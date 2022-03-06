from item import Item
class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int = 0, status: int =1):
        # call to super function to have access to all atributes /methods
        super().__init__(name, price, quantity)

        assert status>=0, f"Status {status} is not greater than 0"

        self.__status=status

"""
Phone.instantiate_from_csv()
print(Phone.all_items)
print(Item.all_items)
"""
