import src.app as app
import requests
import pytest


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

