import src.app as app
import requests
import pytest
from pathlib import Path

def test_api_return():
    results = app.get_product(1)
    data = results.json()

    assert results.status_code == 200, "O retorno da conexão não foi bem sucedida"
    assert "id" in data, "Não existe chave id no retorno"
    assert data["id"] == 1, "Id enviado não é o mesmo recebido"


def test_api_price_return():
    result = app.get_product_price(1)
    assert isinstance(result, (int, float)), "O preço não é numérico"


def test_get_product_http_error_handling(mocker):
    mocker.patch("src.app.requests.get").return_value.status_code = 404
    result = app.get_product(2)
    assert result is None, "Valor não nulo em condição de erro."

def test_timeout_handling(mocker):
    mocker.patch("src.app.requests.get", side_effect=requests.exceptions.Timeout)
    result = app.get_product(3)
    assert result is None, "Valor não nulo em condição de erro."

def test_qtd_product_image():
    result = app.get_product_image(1)
    assert len(result) >= 1, "Número de imagens insuficientes."
    
def test_image_type_product_image():
    result = app.get_product_image(1)
    
    # teste
    #result = [
    #    'https://cdn.dummyjson.com/product-images/1/1.jpg',
    #    'https://cdn.dummyjson.com/product-images/1/2.jpg',
    #    'https://cdn.dummyjson.com/product-images/1/3.jpg',
    #    'https://cdn.dummyjson.com/product-images/1/4.png',
    #    'https://cdn.dummyjson.com/product-images/1/5.png',
    #    'https://cdn.dummyjson.com/product-images/1/6.png',
    #    'https://cdn.dummyjson.com/product-images/1/a.gif',  
    #]

    for url in result:
        if url.endswith('.jpg'):
            assert 'jpg' == 'jpg'
        elif url.endswith('.png'):
            assert 'png' == 'png'
        else:
            assert False, "Extensão não suportada."

def test_image_name_type_product_image():
    result = app.get_product_image(1)

    # teste
    #result = [
    #    'https://cdn.dummyjson.com/product-images/1/1.jpg',
    #    'https://cdn.dummyjson.com/product-images/1/2.jpg',
    #    'https://cdn.dummyjson.com/product-images/1/3.jpg',
    #    'https://cdn.dummyjson.com/product-images/1/4.png',
    #    'https://cdn.dummyjson.com/product-images/1/5.png',
    #    'https://cdn.dummyjson.com/product-images/1/6.png',
    #    'https://cdn.dummyjson.com/product-images/1/a.gif',  
    #]

    for url in result:
        nome_arquivo = Path(url).stem
        assert nome_arquivo.isnumeric(), "Nome do arquivo não é numérico."