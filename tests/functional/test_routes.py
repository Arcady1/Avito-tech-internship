# Built-in Modules
import json


def test_balance_status_valid_arguments_and_user_not_in_db(test_client):
    """
    GIVEN GET request to api/v1.0/balance/users
    WHEN user ID and currency are valid, user ID is not in DB
    THEN check the response
    """
    # Correct user ID
    response_1 = test_client.get("api/v1.0/balance/users?user_id=4")
    response_1_json = json.loads(response_1.data)

    # Correct user ID and currency
    response_2 = test_client.get("api/v1.0/balance/users?user_id=4&currency=RUB")
    response_2_json = json.loads(response_2.data)

    response_3 = test_client.get("api/v1.0/balance/users?user_id=4&currency=rub")
    response_3_json = json.loads(response_3.data)

    response_4 = test_client.get("api/v1.0/balance/users?user_id=4&currency=EUR")
    response_4_json = json.loads(response_4.data)

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
           response_5_json["data"]["userBalance"] == float(0) and \
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


def test_balance_status_valid_arguments_and_user_in_db(test_client):
    """
    GIVEN GET request to api/v1.0/balance/users
    WHEN user ID and currency are valid, user ID is in DB
    THEN check the response
    """
    # Correct user ID
    response_1 = test_client.get("api/v1.0/balance/users?user_id=2")
    response_1_json = json.loads(response_1.data)

    # Correct user ID and currency
    response_2 = test_client.get("api/v1.0/balance/users?user_id=2&currency=RUB")
    response_2_json = json.loads(response_2.data)

    response_3 = test_client.get("api/v1.0/balance/users?user_id=2&currency=rub")
    response_3_json = json.loads(response_3.data)

    response_4 = test_client.get("api/v1.0/balance/users?user_id=2&currency=EUR")
    response_4_json = json.loads(response_4.data)

    response_5 = test_client.get("api/v1.0/balance/users?user_id=2&currency=eur")
    response_5_json = json.loads(response_5.data)

    assert response_1.status_code == 200 and \
           response_1_json["data"]["userId"] == 2 and \
           response_1_json["data"]["userBalance"] == float(15000) and \
           response_1_json["data"]["sender"]["id"] is None and \
           response_1_json["data"]["reciever"]["id"] is None and \
           response_1_json["data"]["amount"] is None and \
           response_1_json["data"]["currency"] == "RUB"
    assert response_2.status_code == 200 and \
           response_2_json["data"]["userId"] == 2 and \
           response_2_json["data"]["userBalance"] == float(15000) and \
           response_2_json["data"]["sender"]["id"] is None and \
           response_2_json["data"]["reciever"]["id"] is None and \
           response_2_json["data"]["amount"] is None and \
           response_2_json["data"]["currency"] == "RUB"
    assert response_3.status_code == 200 and \
           response_3_json["data"]["userId"] == 2 and \
           response_3_json["data"]["userBalance"] == float(15000) and \
           response_3_json["data"]["sender"]["id"] is None and \
           response_3_json["data"]["reciever"]["id"] is None and \
           response_3_json["data"]["amount"] is None and \
           response_3_json["data"]["currency"] == "RUB"
    assert response_4.status_code == 200 and \
           response_4_json["data"]["userId"] == 2 and \
           isinstance(response_3_json["data"]["userBalance"], float) and \
           response_4_json["data"]["sender"]["id"] is None and \
           response_4_json["data"]["reciever"]["id"] is None and \
           response_4_json["data"]["amount"] is None and \
           response_4_json["data"]["currency"] == "EUR"
    assert response_5.status_code == 200 and \
           response_5_json["data"]["userId"] == 2 and \
           isinstance(response_3_json["data"]["userBalance"], float) and \
           response_5_json["data"]["sender"]["id"] is None and \
           response_5_json["data"]["reciever"]["id"] is None and \
           response_5_json["data"]["amount"] is None and \
           response_5_json["data"]["currency"] == "EUR"


def test_balance_status_invalid_arguments(test_client):
    """
        GIVEN GET request to api/v1.0/balance/users
        WHEN user ID or currency is invalid
        THEN check the response
    """
    # No arguments
    response_1 = test_client.get("api/v1.0/balance/users")

    # No user ID, only currency
    response_2 = test_client.get("api/v1.0/balance/users?currency=RUB")

    # Wrong user ID
    response_3 = test_client.get("api/v1.0/balance/users?user_id=-1")
    response_3_json = json.loads(response_3.data)

    response_4 = test_client.get("api/v1.0/balance/users?user_id=0")
    response_4_json = json.loads(response_4.data)
    response_5 = test_client.get("api/v1.0/balance/users?user_id=abc")
    response_5_json = json.loads(response_5.data)

    # Correct user ID, wrong currency
    response_6 = test_client.get("api/v1.0/balance/users?user_id=1&currency=123")
    response_6_json = json.loads(response_6.data)
    response_7 = test_client.get("api/v1.0/balance/users?user_id=1&currency=zzz")
    response_7_json = json.loads(response_7.data)
    response_8 = test_client.get("api/v1.0/balance/users?user_id=1&currency=rubs")
    response_8_json = json.loads(response_8.data)

    assert response_1.status_code == 400
    assert response_2.status_code == 400
    assert response_3.status_code == 400 and \
           response_3_json["data"]["userId"] is None and \
           response_3_json["data"]["userBalance"] is None and \
           response_3_json["data"]["sender"]["id"] is None and \
           response_3_json["data"]["reciever"]["id"] is None and \
           response_3_json["data"]["amount"] is None and \
           response_3_json["data"]["currency"] == "RUB"
    assert response_4.status_code == 400 and \
           response_4_json["data"]["userId"] is None and \
           response_4_json["data"]["userBalance"] is None and \
           response_4_json["data"]["sender"]["id"] is None and \
           response_4_json["data"]["reciever"]["id"] is None and \
           response_4_json["data"]["amount"] is None and \
           response_4_json["data"]["currency"] == "RUB"
    assert response_5.status_code == 400 and \
           response_5_json["data"]["userId"] is None and \
           response_5_json["data"]["userBalance"] is None and \
           response_5_json["data"]["sender"]["id"] is None and \
           response_5_json["data"]["reciever"]["id"] is None and \
           response_5_json["data"]["amount"] is None and \
           response_5_json["data"]["currency"] == "RUB"
    assert response_6.status_code == 400 and \
           response_6_json["data"]["userId"] == 1 and \
           response_6_json["data"]["userBalance"] == float(10000) and \
           response_6_json["data"]["sender"]["id"] is None and \
           response_6_json["data"]["reciever"]["id"] is None and \
           response_6_json["data"]["amount"] is None and \
           response_6_json["data"]["currency"] == "RUB"
    assert response_7.status_code == 400 and \
           response_7_json["data"]["userId"] == 1 and \
           response_7_json["data"]["userBalance"] == float(10000) and \
           response_7_json["data"]["sender"]["id"] is None and \
           response_7_json["data"]["reciever"]["id"] is None and \
           response_7_json["data"]["amount"] is None and \
           response_7_json["data"]["currency"] == "RUB"
    assert response_8.status_code == 400 and \
           response_8_json["data"]["userId"] == 1 and \
           response_8_json["data"]["userBalance"] == float(10000) and \
           response_8_json["data"]["sender"]["id"] is None and \
           response_8_json["data"]["reciever"]["id"] is None and \
           response_8_json["data"]["amount"] is None and \
           response_8_json["data"]["currency"] == "RUB"


def test_balance_refill_valid_arguments(test_client):
    """
        GIVEN PUT request to api/v1.0/refill/users
        WHEN user ID and amount are valid
        THEN check the response
    """
    # Correct user ID and amount. The user is in DB
    response_1 = test_client.put("api/v1.0/refill/users?user_id=1&amount=5000")
    response_1_json = json.loads(response_1.data)

    # Correct user ID and amount. The user is not in DB
    response_2 = test_client.put("api/v1.0/refill/users?user_id=4&amount=5000")
    response_2_json = json.loads(response_2.data)

    assert response_1.status_code == 200 and \
           response_1_json["data"]["userId"] == 1 and \
           response_1_json["data"]["userBalance"] == float(15000) and \
           response_1_json["data"]["sender"]["id"] is None and \
           response_1_json["data"]["reciever"]["id"] is None and \
           response_1_json["data"]["amount"] == float(5000) and \
           response_1_json["data"]["currency"] == "RUB"
    assert response_2.status_code == 200 and \
           response_2_json["data"]["userId"] == 4 and \
           response_2_json["data"]["userBalance"] == float(5000) and \
           response_2_json["data"]["sender"]["id"] is None and \
           response_2_json["data"]["reciever"]["id"] is None and \
           response_2_json["data"]["amount"] == float(5000) and \
           response_2_json["data"]["currency"] == "RUB"


def test_balance_refill_invalid_arguments(test_client):
    """
        GIVEN PUT request to api/v1.0/refill/users
        WHEN user ID or amount is invalid
        THEN check the response
    """
    # No arguments
    response_1 = test_client.put("api/v1.0/refill/users")

    # No amount, only user ID
    response_2 = test_client.put("api/v1.0/refill/users?user_id=1")

    # No user ID, only amount
    response_3 = test_client.put("api/v1.0/refill/users?amount=5000")

    # Correct amount, wrong user ID
    response_4 = test_client.put("api/v1.0/refill/users?user_id=-1&amount=5000")
    response_4_json = json.loads(response_4.data)
    response_5 = test_client.put("api/v1.0/refill/users?user_id=0&amount=5000")
    response_5_json = json.loads(response_5.data)
    response_6 = test_client.put("api/v1.0/refill/users?user_id=abc&amount=5000")
    response_6_json = json.loads(response_6.data)

    # Correct user ID, wrong amount
    response_7 = test_client.put("api/v1.0/refill/users?user_id=1&amount=0")
    response_7_json = json.loads(response_7.data)
    response_8 = test_client.put("api/v1.0/refill/users?user_id=1&amount=-1")
    response_8_json = json.loads(response_8.data)
    response_9 = test_client.put("api/v1.0/refill/users?user_id=1&amount=zzz")
    response_9_json = json.loads(response_9.data)

    assert response_1.status_code == 400
    assert response_2.status_code == 400
    assert response_3.status_code == 400
    assert response_4.status_code == 400 and \
           response_4_json["data"]["userId"] is None and \
           response_4_json["data"]["userBalance"] is None and \
           response_4_json["data"]["sender"]["id"] is None and \
           response_4_json["data"]["reciever"]["id"] is None and \
           response_4_json["data"]["amount"] is None and \
           response_4_json["data"]["currency"] == "RUB"
    assert response_5.status_code == 400 and \
           response_5_json["data"]["userId"] is None and \
           response_5_json["data"]["userBalance"] is None and \
           response_5_json["data"]["sender"]["id"] is None and \
           response_5_json["data"]["reciever"]["id"] is None and \
           response_5_json["data"]["amount"] is None and \
           response_5_json["data"]["currency"] == "RUB"
    assert response_6.status_code == 400 and \
           response_6_json["data"]["userId"] is None and \
           response_6_json["data"]["userBalance"] is None and \
           response_6_json["data"]["sender"]["id"] is None and \
           response_6_json["data"]["reciever"]["id"] is None and \
           response_6_json["data"]["amount"] is None and \
           response_6_json["data"]["currency"] == "RUB"
    assert response_7.status_code == 400 and \
           response_7_json["data"]["userId"] == 1 and \
           response_7_json["data"]["userBalance"] == float(15000) and \
           response_7_json["data"]["sender"]["id"] is None and \
           response_7_json["data"]["reciever"]["id"] is None and \
           response_7_json["data"]["amount"] is None and \
           response_7_json["data"]["currency"] == "RUB"
    assert response_8.status_code == 400 and \
           response_8_json["data"]["userId"] == 1 and \
           response_8_json["data"]["userBalance"] == float(15000) and \
           response_8_json["data"]["sender"]["id"] is None and \
           response_8_json["data"]["reciever"]["id"] is None and \
           response_8_json["data"]["amount"] is None and \
           response_8_json["data"]["currency"] == "RUB"
    assert response_9.status_code == 400 and \
           response_9_json["data"]["userId"] == 1 and \
           response_9_json["data"]["userBalance"] == float(15000) and \
           response_9_json["data"]["sender"]["id"] is None and \
           response_9_json["data"]["reciever"]["id"] is None and \
           response_9_json["data"]["amount"] is None and \
           response_9_json["data"]["currency"] == "RUB"


def test_balance_writeoff_valid_arguments(test_client):
    """
    GIVEN PUT request to api/v1.0/writeoff/users
    WHEN user ID and amount are valid
    THEN check the response
    """
    # Correct user ID and amount. The user is in DB
    response_1 = test_client.put("api/v1.0/writeoff/users?user_id=1&amount=5000")
    response_1_json = json.loads(response_1.data)

    assert response_1.status_code == 200 and \
           response_1_json["data"]["userId"] == 1 and \
           response_1_json["data"]["userBalance"] == float(10000) and \
           response_1_json["data"]["sender"]["id"] is None and \
           response_1_json["data"]["reciever"]["id"] is None and \
           response_1_json["data"]["amount"] == float(5000) and \
           response_1_json["data"]["currency"] == "RUB"


def test_balance_writeoff_invalid_arguments(test_client):
    """
    GIVEN PUT request to api/v1.0/writeoff/users
    WHEN user ID or amount is invalid
    THEN check the response
    """
    # No arguments
    response_1 = test_client.put("api/v1.0/writeoff/users")

    # No amount, only user ID
    response_2 = test_client.put("api/v1.0/writeoff/users?user_id=1")

    # No user ID, only amount
    response_3 = test_client.put("api/v1.0/writeoff/users?amount=5000")

    # Correct amount, wrong user ID
    response_4 = test_client.put("api/v1.0/writeoff/users?user_id=-1&amount=5000")
    response_4_json = json.loads(response_4.data)
    response_5 = test_client.put("api/v1.0/writeoff/users?user_id=0&amount=5000")
    response_5_json = json.loads(response_5.data)
    response_6 = test_client.put("api/v1.0/writeoff/users?user_id=abc&amount=5000")
    response_6_json = json.loads(response_6.data)

    # Correct user ID, wrong amount
    response_7 = test_client.put("api/v1.0/writeoff/users?user_id=1&amount=0")
    response_7_json = json.loads(response_7.data)
    response_8 = test_client.put("api/v1.0/writeoff/users?user_id=1&amount=-1")
    response_8_json = json.loads(response_8.data)
    response_9 = test_client.put("api/v1.0/writeoff/users?user_id=1&amount=zzz")
    response_9_json = json.loads(response_9.data)

    # Correct user ID and amount. User is not in DB
    response_10 = test_client.put("api/v1.0/writeoff/users?user_id=5&amount=5000")
    response_10_json = json.loads(response_10.data)

    # Correct user ID and amount. Amount > user's balance
    response_11 = test_client.put("api/v1.0/writeoff/users?user_id=1&amount=11000")
    response_11_json = json.loads(response_11.data)

    assert response_1.status_code == 400
    assert response_2.status_code == 400
    assert response_3.status_code == 400
    assert response_4.status_code == 400 and \
           response_4_json["data"]["userId"] is None and \
           response_4_json["data"]["userBalance"] is None and \
           response_4_json["data"]["sender"]["id"] is None and \
           response_4_json["data"]["reciever"]["id"] is None and \
           response_4_json["data"]["amount"] is None and \
           response_4_json["data"]["currency"] == "RUB"
    assert response_5.status_code == 400 and \
           response_5_json["data"]["userId"] is None and \
           response_5_json["data"]["userBalance"] is None and \
           response_5_json["data"]["sender"]["id"] is None and \
           response_5_json["data"]["reciever"]["id"] is None and \
           response_5_json["data"]["amount"] is None and \
           response_5_json["data"]["currency"] == "RUB"
    assert response_6.status_code == 400 and \
           response_6_json["data"]["userId"] is None and \
           response_6_json["data"]["userBalance"] is None and \
           response_6_json["data"]["sender"]["id"] is None and \
           response_6_json["data"]["reciever"]["id"] is None and \
           response_6_json["data"]["amount"] is None and \
           response_6_json["data"]["currency"] == "RUB"
    assert response_7.status_code == 400 and \
           response_7_json["data"]["userId"] == 1 and \
           response_7_json["data"]["userBalance"] == float(10000) and \
           response_7_json["data"]["sender"]["id"] is None and \
           response_7_json["data"]["reciever"]["id"] is None and \
           response_7_json["data"]["amount"] is None and \
           response_7_json["data"]["currency"] == "RUB"
    assert response_8.status_code == 400 and \
           response_8_json["data"]["userId"] == 1 and \
           response_8_json["data"]["userBalance"] == float(10000) and \
           response_8_json["data"]["sender"]["id"] is None and \
           response_8_json["data"]["reciever"]["id"] is None and \
           response_8_json["data"]["amount"] is None and \
           response_8_json["data"]["currency"] == "RUB"
    assert response_9.status_code == 400 and \
           response_9_json["data"]["userId"] == 1 and \
           response_9_json["data"]["userBalance"] == float(10000) and \
           response_9_json["data"]["sender"]["id"] is None and \
           response_9_json["data"]["reciever"]["id"] is None and \
           response_9_json["data"]["amount"] is None and \
           response_9_json["data"]["currency"] == "RUB"
    assert response_10.status_code == 400 and \
           response_10_json["data"]["userId"] == 5 and \
           response_10_json["data"]["userBalance"] is None and \
           response_10_json["data"]["sender"]["id"] is None and \
           response_10_json["data"]["reciever"]["id"] is None and \
           response_10_json["data"]["amount"] == float(5000) and \
           response_10_json["data"]["currency"] == "RUB"
    assert response_11.status_code == 400 and \
           response_11_json["data"]["userId"] == 1 and \
           response_11_json["data"]["userBalance"] == float(10000) and \
           response_11_json["data"]["sender"]["id"] is None and \
           response_11_json["data"]["reciever"]["id"] is None and \
           response_11_json["data"]["amount"] == float(11000) and \
           response_11_json["data"]["currency"] == "RUB"


def test_balance_transfer_money_valid_arguments(test_client):
    """
    GIVEN PUT request to api/v1.0/transfer/users
    WHEN sender_uid and reciever_uid are valid
    THEN check the response
    """
    # Correct sender_uid and reciever_uid. The users are in DB
    response_1 = test_client.put("api/v1.0/transfer/users?sender_uid=1&reciever_uid=2&amount=5000")
    response_1_json = json.loads(response_1.data)

    assert response_1.status_code == 200 and \
           response_1_json["data"]["userId"] is None and \
           response_1_json["data"]["userBalance"] is None and \
           response_1_json["data"]["sender"]["id"] == 1 and \
           response_1_json["data"]["sender"]["balance"] == float(5000) and \
           response_1_json["data"]["reciever"]["id"] == 2 and \
           response_1_json["data"]["reciever"]["balance"] == float(20000) and \
           response_1_json["data"]["amount"] == float(5000) and \
           response_1_json["data"]["currency"] == "RUB"


def test_balance_writeoff_invalid_arguments(test_client):
    """
    GIVEN PUT request to api/v1.0/transfer/users
    WHEN sender_uid or reciever_uid or amount is invalid
    THEN check the response
    """

    # No arguments
    response_1 = test_client.put("api/v1.0/transfer/users")

    # Only sender_uid
    response_2 = test_client.put("api/v1.0/transfer/users?sender_uid=1")

    # Only reciever_uid
    response_3 = test_client.put("api/v1.0/transfer/users?reciever_uid=2")

    # Only amount
    response_4 = test_client.put("api/v1.0/transfer/users?amount=5000")

    # Only sender_uid and reciever_uid, no amount
    response_5 = test_client.put("api/v1.0/transfer/users?sender_uid=1&reciever_uid=2")

    # Only sender_uid and amount, no reciever_uid
    response_6 = test_client.put("api/v1.0/transfer/users?sender_uid=1&amount=5000")

    # Only reciever_uid and amount, no sender_uid
    response_7 = test_client.put("api/v1.0/transfer/users?reciever_uid=2&amount=5000")

    # Wrong sender_uid
    response_8 = test_client.put("api/v1.0/transfer/users?sender_uid=0&reciever_uid=2&amount=5000")
    response_8_json = json.loads(response_8.data)
    response_9 = test_client.put("api/v1.0/transfer/users?sender_uid=-1&reciever_uid=2&amount=5000")
    response_9_json = json.loads(response_9.data)
    response_10 = test_client.put("api/v1.0/transfer/users?sender_uid=zzz&reciever_uid=2&amount=5000")
    response_10_json = json.loads(response_10.data)

    # Wrong reciever_uid
    response_11 = test_client.put("api/v1.0/transfer/users?sender_uid=1&reciever_uid=0&amount=5000")
    response_11_json = json.loads(response_11.data)
    response_12 = test_client.put("api/v1.0/transfer/users?sender_uid=1&reciever_uid=-1&amount=5000")
    response_12_json = json.loads(response_12.data)
    response_13 = test_client.put("api/v1.0/transfer/users?sender_uid=1&reciever_uid=zzz&amount=5000")
    response_13_json = json.loads(response_13.data)

    # Wrong amount
    response_14 = test_client.put("api/v1.0/transfer/users?sender_uid=1&reciever_uid=2&amount=0")
    response_14_json = json.loads(response_14.data)
    response_15 = test_client.put("api/v1.0/transfer/users?sender_uid=1&reciever_uid=2&amount=-1")
    response_15_json = json.loads(response_15.data)
    response_16 = test_client.put("api/v1.0/transfer/users?sender_uid=1&reciever_uid=2&amount=zzz")
    response_16_json = json.loads(response_16.data)

    # Correct arguments. sender_uid not in DB
    response_17 = test_client.put("api/v1.0/transfer/users?sender_uid=11&reciever_uid=2&amount=5000")
    response_17_json = json.loads(response_17.data)

    # Correct arguments. reciever_uid not in DB
    response_18 = test_client.put("api/v1.0/transfer/users?sender_uid=1&reciever_uid=22&amount=5000")
    response_18_json = json.loads(response_18.data)

    # Correct arguments. sender_uid and reciever_uid not in DB
    response_19 = test_client.put("api/v1.0/transfer/users?sender_uid=11&reciever_uid=22&amount=5000")
    response_19_json = json.loads(response_19.data)

    # Correct arguments. Amount > sender's balance
    response_20 = test_client.put("api/v1.0/transfer/users?sender_uid=1&reciever_uid=2&amount=7000")
    response_20_json = json.loads(response_20.data)

    assert response_1.status_code == 400
    assert response_2.status_code == 400
    assert response_3.status_code == 400
    assert response_4.status_code == 400
    assert response_5.status_code == 400
    assert response_6.status_code == 400
    assert response_7.status_code == 400
    assert response_8.status_code == 400 and \
           response_8_json["data"]["userId"] is None and \
           response_8_json["data"]["userBalance"] is None and \
           response_8_json["data"]["sender"]["id"] is None and \
           response_8_json["data"]["reciever"]["id"] is None and \
           response_8_json["data"]["amount"] is None and \
           response_8_json["data"]["currency"] == "RUB"
    assert response_9.status_code == 400 and \
           response_9_json["data"]["userId"] is None and \
           response_9_json["data"]["userBalance"] is None and \
           response_9_json["data"]["sender"]["id"] is None and \
           response_9_json["data"]["reciever"]["id"] is None and \
           response_9_json["data"]["amount"] is None and \
           response_9_json["data"]["currency"] == "RUB"
    assert response_10.status_code == 400 and \
           response_10_json["data"]["userId"] is None and \
           response_10_json["data"]["userBalance"] is None and \
           response_10_json["data"]["sender"]["id"] is None and \
           response_10_json["data"]["reciever"]["id"] is None and \
           response_10_json["data"]["amount"] is None and \
           response_10_json["data"]["currency"] == "RUB"
    assert response_11.status_code == 400 and \
           response_11_json["data"]["userId"] is None and \
           response_11_json["data"]["userBalance"] is None and \
           response_11_json["data"]["sender"]["id"] == 1 and \
           response_11_json["data"]["sender"]["balance"] == float(5000) and \
           response_11_json["data"]["reciever"]["id"] is None and \
           response_11_json["data"]["amount"] is None and \
           response_11_json["data"]["currency"] == "RUB"
    assert response_12.status_code == 400 and \
           response_12_json["data"]["userId"] is None and \
           response_12_json["data"]["userBalance"] is None and \
           response_12_json["data"]["sender"]["id"] == 1 and \
           response_12_json["data"]["sender"]["balance"] == float(5000) and \
           response_12_json["data"]["reciever"]["id"] is None and \
           response_12_json["data"]["amount"] is None and \
           response_12_json["data"]["currency"] == "RUB"
    assert response_13.status_code == 400 and \
           response_13_json["data"]["userId"] is None and \
           response_13_json["data"]["userBalance"] is None and \
           response_13_json["data"]["sender"]["id"] == 1 and \
           response_13_json["data"]["sender"]["balance"] == float(5000) and \
           response_13_json["data"]["reciever"]["id"] is None and \
           response_13_json["data"]["amount"] is None and \
           response_13_json["data"]["currency"] == "RUB"
    assert response_14.status_code == 400 and \
           response_14_json["data"]["userId"] is None and \
           response_14_json["data"]["userBalance"] is None and \
           response_14_json["data"]["sender"]["id"] == 1 and \
           response_14_json["data"]["sender"]["balance"] == float(5000) and \
           response_14_json["data"]["reciever"]["id"] == 2 and \
           response_14_json["data"]["reciever"]["balance"] == float(20000) and \
           response_14_json["data"]["amount"] is None and \
           response_14_json["data"]["currency"] == "RUB"
    assert response_15.status_code == 400 and \
           response_15_json["data"]["userId"] is None and \
           response_15_json["data"]["userBalance"] is None and \
           response_15_json["data"]["sender"]["id"] == 1 and \
           response_15_json["data"]["sender"]["balance"] == float(5000) and \
           response_15_json["data"]["reciever"]["id"] == 2 and \
           response_15_json["data"]["reciever"]["balance"] == float(20000) and \
           response_15_json["data"]["amount"] is None and \
           response_15_json["data"]["currency"] == "RUB"
    assert response_16.status_code == 400 and \
           response_16_json["data"]["userId"] is None and \
           response_16_json["data"]["userBalance"] is None and \
           response_16_json["data"]["sender"]["id"] == 1 and \
           response_16_json["data"]["sender"]["balance"] == float(5000) and \
           response_16_json["data"]["reciever"]["id"] == 2 and \
           response_16_json["data"]["reciever"]["balance"] == float(20000) and \
           response_16_json["data"]["amount"] is None and \
           response_16_json["data"]["currency"] == "RUB"
    assert response_17.status_code == 400 and \
           response_17_json["data"]["userId"] is None and \
           response_17_json["data"]["userBalance"] is None and \
           response_17_json["data"]["sender"]["id"] == 11 and \
           response_17_json["data"]["sender"]["balance"] is None and \
           response_17_json["data"]["reciever"]["id"] == 2 and \
           response_17_json["data"]["reciever"]["balance"] == float(20000) and \
           response_17_json["data"]["amount"] is None and \
           response_17_json["data"]["currency"] == "RUB"
    assert response_18.status_code == 400 and \
           response_18_json["data"]["userId"] is None and \
           response_18_json["data"]["userBalance"] is None and \
           response_18_json["data"]["sender"]["id"] == 1 and \
           response_18_json["data"]["sender"]["balance"] == float(5000) and \
           response_18_json["data"]["reciever"]["id"] == 22 and \
           response_18_json["data"]["reciever"]["balance"] is None and \
           response_18_json["data"]["amount"] is None and \
           response_18_json["data"]["currency"] == "RUB"
    assert response_19.status_code == 400 and \
           response_19_json["data"]["userId"] is None and \
           response_19_json["data"]["userBalance"] is None and \
           response_19_json["data"]["sender"]["id"] == 11 and \
           response_19_json["data"]["sender"]["balance"] is None and \
           response_19_json["data"]["reciever"]["id"] == 22 and \
           response_19_json["data"]["reciever"]["balance"] is None and \
           response_19_json["data"]["amount"] is None and \
           response_19_json["data"]["currency"] == "RUB"
    assert response_20.status_code == 400 and \
           response_20_json["data"]["userId"] is None and \
           response_20_json["data"]["userBalance"] is None and \
           response_20_json["data"]["sender"]["id"] == 1 and \
           response_20_json["data"]["sender"]["balance"] == float(5000) and \
           response_20_json["data"]["reciever"]["id"] == 2 and \
           response_20_json["data"]["reciever"]["balance"] == float(20000) and \
           response_20_json["data"]["amount"] == float(7000) and \
           response_20_json["data"]["currency"] == "RUB"
