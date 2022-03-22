# Built-in Modules
import json

# Third Party Modules
from flask_restful import Api

# Project Modules
from server.resources.balance_status.balance_status import BalanceStatus


def test_balance_status_valid_user_id_user_and_user_not_in_db(test_client):
    """
    GIVEN GET request to api/v1.0/balance/users
    WHEN user ID and currency are valid, user ID is not in DB
    THEN check the response
    """
    # Корректный ID пользователя
    response_1 = test_client.get("api/v1.0/balance/users?user_id=4")
    response_1_json = json.loads(response_1.data)
    # Корректные ID пользователя и валюта
    response_2 = test_client.get("api/v1.0/balance/users?user_id=4&currency=RUB")
    response_2_json = json.loads(response_2.data)
    # Корректные ID пользователя и валюта
    response_3 = test_client.get("api/v1.0/balance/users?user_id=4&currency=rub")
    response_3_json = json.loads(response_3.data)
    # Корректные ID пользователя и валюта
    response_4 = test_client.get("api/v1.0/balance/users?user_id=4&currency=EUR")
    response_4_json = json.loads(response_4.data)
    # Корректные ID пользователя и валюта
    response_5 = test_client.get("api/v1.0/balance/users?user_id=4&currency=eur")
    response_5_json = json.loads(response_5.data)

    assert response_1.status_code == 200 and \
           response_1_json["data"]["userId"] == 4 and \
           response_1_json["data"]["userBalance"] == float(0) and \
           response_1_json["data"]["sender"]["id"] is None and \
           response_1_json["data"]["reciever"]["id"] is None and \
           response_1_json["data"]["amount"] is None and \
           response_1_json["data"]["currency"] == "RUB"
    assert response_2.status_code == 200 and \
           response_2_json["data"]["userId"] == 4 and \
           response_2_json["data"]["userBalance"] == float(0) and \
           response_2_json["data"]["sender"]["id"] is None and \
           response_2_json["data"]["reciever"]["id"] is None and \
           response_2_json["data"]["amount"] is None and \
           response_2_json["data"]["currency"] == "RUB"
    assert response_3.status_code == 200 and \
           response_3_json["data"]["userId"] == 4 and \
           response_3_json["data"]["userBalance"] == float(0) and \
           response_3_json["data"]["sender"]["id"] is None and \
           response_3_json["data"]["reciever"]["id"] is None and \
           response_3_json["data"]["amount"] is None and \
           response_3_json["data"]["currency"] == "RUB"
    assert response_4.status_code == 200 and \
           response_4_json["data"]["userId"] == 4 and \
           response_4_json["data"]["sender"]["id"] is None and \
           response_4_json["data"]["reciever"]["id"] is None and \
           response_4_json["data"]["amount"] is None and \
           response_4_json["data"]["currency"] == "EUR"
    assert response_5.status_code == 200 and \
           response_5_json["data"]["userId"] == 4 and \
           response_5_json["data"]["userBalance"] == float(0) and \
           response_5_json["data"]["sender"]["id"] is None and \
           response_5_json["data"]["reciever"]["id"] is None and \
           response_5_json["data"]["amount"] is None and \
           response_5_json["data"]["currency"] == "EUR"
#
# def test_balance_status_valid_user_id_user_and_user_in_db(test_client):
#     """
#     GIVEN GET request to api/v1.0/balance/users
#     WHEN user ID and currency are valid, user ID is in DB
#     THEN check the response
#     """
#     # Корректный ID пользователя
#     response_1 = test_client.get("api/v1.0/balance/users?user_id=2")
#     response_1_json = json.loads(response_1.data)
#     # Корректные ID пользователя и валюта
#     response_2 = test_client.get("api/v1.0/balance/users?user_id=2&currency=RUB")
#     response_2_json = json.loads(response_2.data)
#     # Корректные ID пользователя и валюта
#     response_3 = test_client.get("api/v1.0/balance/users?user_id=2&currency=rub")
#     response_3_json = json.loads(response_3.data)
#     # Корректные ID пользователя и валюта
#     response_4 = test_client.get("api/v1.0/balance/users?user_id=2&currency=EUR")
#     response_4_json = json.loads(response_4.data)
#     # Корректные ID пользователя и валюта
#     response_5 = test_client.get("api/v1.0/balance/users?user_id=2&currency=eur")
#     response_5_json = json.loads(response_5.data)
#
#     assert response_1.status_code == 200 and \
#            response_1_json["data"]["userId"] == 2 and \
#            response_1_json["data"]["userBalance"] == float(15000) and \
#            response_1_json["data"]["sender"]["id"] is None and \
#            response_1_json["data"]["reciever"]["id"] is None and \
#            response_1_json["data"]["amount"] is None and \
#            response_1_json["data"]["currency"] == "RUB"
#     assert response_2.status_code == 200 and \
#            response_2_json["data"]["userId"] == 4 and \
#            response_2_json["data"]["userBalance"] == float(15000) and \
#            response_2_json["data"]["sender"]["id"] is None and \
#            response_2_json["data"]["reciever"]["id"] is None and \
#            response_2_json["data"]["amount"] is None and \
#            response_2_json["data"]["currency"] == "RUB"
#     assert response_3.status_code == 200 and \
#            response_3_json["data"]["userId"] == 4 and \
#            response_3_json["data"]["userBalance"] == float(0) and \
#            response_3_json["data"]["sender"]["id"] is None and \
#            response_3_json["data"]["reciever"]["id"] is None and \
#            response_3_json["data"]["amount"] is None and \
#            response_3_json["data"]["currency"] == "RUB"
#     assert response_4.status_code == 200 and \
#            response_4_json["data"]["userId"] == 4 and \
#            response_4_json["data"]["sender"]["id"] is None and \
#            response_4_json["data"]["reciever"]["id"] is None and \
#            response_4_json["data"]["amount"] is None and \
#            response_4_json["data"]["currency"] == "EUR"
#     assert response_5.status_code == 200 and \
#            response_5_json["data"]["userId"] == 4 and \
#            response_5_json["data"]["userBalance"] == float(0) and \
#            response_5_json["data"]["sender"]["id"] is None and \
#            response_5_json["data"]["reciever"]["id"] is None and \
#            response_5_json["data"]["amount"] is None and \
#            response_5_json["data"]["currency"] == "EUR"


def test_balance_status_invalid_user_id(test_client):
    """
    GIVEN
    WHEN
    THEN
    """
    # Нет аргументов
    response_1 = test_client.get("api/v1.0/balance/users")
    # Переданна только валюта
    response_2 = test_client.get("api/v1.0/balance/users?currency=RUB")
    # Некорректный ID пользователя
    response_3 = test_client.get("api/v1.0/balance/users?user_id=-1")
    response_5 = test_client.get("api/v1.0/balance/users?user_id=0")
    response_4 = test_client.get("api/v1.0/balance/users?user_id=abc")
    # Корректный ID пользователя, некорректная валюта
    response_8 = test_client.get("api/v1.0/balance/users?user_id=1&currency=123")
    response_9 = test_client.get("api/v1.0/balance/users?user_id=1&currency=zzz")
    response_10 = test_client.get("api/v1.0/balance/users?user_id=1&currency=rubs")

    # TODO


def test_balance_refill_valid_user_id(test_client):
    """
    GIVEN
    WHEN
    THEN
    """
    # Корректные ID пользователя и валюта

    # TODO


def test_balance_refill_invalid_user_id(test_client):
    """
    GIVEN
    WHEN
    THEN
    """
    # Нет аргументов
    # Передан только ID пользователя
    # Переданна только сумма
    # Некорректный ID пользователя
    # Некорректная сумма

    # TODO


def test_balance_writeoff_valid_user_id(test_client):
    """
    GIVEN
    WHEN
    THEN
    """
    # Корректные ID пользователя и валюта, пользователь есть в БД
    # Пользователь есть в БД
    # Сумма >= баланса пользователя

    # TODO


def test_balance_writeoff_invalid_user_id(test_client):
    """
    GIVEN
    WHEN
    THEN
    """
    # Нет аргументов
    # Передан только ID пользователя
    # Переданна только сумма
    # Некорректный ID пользователя
    # Некорректная сумма
    # Корректные ID пользователя и валюта, пользователя нет в БД

    # TODO
