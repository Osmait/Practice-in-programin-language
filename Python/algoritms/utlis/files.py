import requests
import json




# response = requests.get('https://dummyjson.com/products/1')
# result = response.json()

# with open("product.json", "w") as file:
#     file.write(str(result))


with open("product.json", "r") as file:
    result = file.read()
    print(json.loads(result)["id"])