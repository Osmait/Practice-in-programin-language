import requests
from functools import reduce



try:

    reponse = requests.get("https://dummyjson.com/product/1")
except Exception as e:
    print(e)
    exit()

responds_json = reponse.json()


class Product:
    def __init__(self, title, price, description):
        self.title = title
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.title} - {self.price} - {self.description}"

    def __repr__(self):
        return f"{self.title} - {self.price} - {self.description}"
    
product = Product(responds_json['title'], responds_json['price'], responds_json['description'])

boolean = True
p1 =  product if boolean else "ahi "

print( p1)


lista = [1,2,3,4]

result  = reduce(lambda x,y: x+y, lista)
print(result)