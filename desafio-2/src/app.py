"""Código de testes para aula"""
import requests

def get_product(product_id):
    """Função que retorna o objeto requests de consumo de API"""
    try:
        results = requests.get("https://dummyjson.com/products/"+str(product_id), timeout=5)
        if results.status_code == 200:
            return results
        return None
    except requests.RequestException as e:
        print(e)
        return None

def get_product_price(product_id):
    """Função que retorna o preço de um produto"""
    results = requests.get("https://dummyjson.com/products/"+str(product_id), timeout=5)
    data = results.json()
    return data["price"]

def get_product_image(product_id):
    """Função que retorna imagens de um produto"""
    results = requests.get("https://dummyjson.com/products/"+str(product_id), timeout=5)
    data = results.json()
    images = data["images"]
    return images[:3]

response = get_product(1)

print(response.status_code)
print(response.text)

response = get_product_price(1)

print(response)

response = get_product_image(1)
print(response)
