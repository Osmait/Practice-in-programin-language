import requests
from functools import reduce


try:

    reponse = requests.get("https://dummyjson.com/product/1")
except Exception as e:
    print(e)
    exit()

responds_json = reponse.json()


class Product:

    def __init__(self, id: int,
                 title: str,
                 description: str,
                 price: int,
                 discountPercentage: float,
                 rating: float,
                 stock: int,
                 brand: str,
                 category: str,
                 thumbnail: str,
                 images: list[str]) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.discount_percentage = discountPercentage
        self.rating = rating
        self.stock = stock
        self.brand = brand
        self.category = category
        self.thumbnail = thumbnail
        self.images = images

    def __str__(self):
        return f"{self.title} - {self.price} - {self.description}"

    def __repr__(self):
        return f"{self.title} - {self.price} - {self.description}"


product = Product(**responds_json)
boolean = True
p1 = product if boolean else "ahi "

print(p1)


lista = [1, 2, 3, 4]

result = reduce(lambda x, y: x+y, lista)
print(result)
