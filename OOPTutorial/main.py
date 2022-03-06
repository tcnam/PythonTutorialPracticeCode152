from phone import Phone
from item import Item

Item.instantiate_from_csv()
for instan in Item.all_items:
    print(instan)



