# Built-in Modules
import json


def test_balance_status_valid_arguments(test_client):
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
           response_1_json["data"]["currency"] == "RUB"
    assert response_2.status_code == 200 and \
           response_2_json["data"]["userId"] == 2 and \
           response_2_json["data"]["userBalance"] == float(15000) and \
           response_2_json["data"]["currency"] == "RUB"
    assert response_3.status_code == 200 and \
           response_3_json["data"]["userId"] == 2 and \
           response_3_json["data"]["userBalance"] == float(15000) and \
           response_3_json["data"]["currency"] == "RUB"
    assert response_4.status_code == 200 and \
           response_4_json["data"]["userId"] == 2 and \
           isinstance(response_3_json["data"]["userBalance"], float) and \
           response_4_json["data"]["currency"] == "EUR"
    assert response_5.status_code == 200 and \
           response_5_json["data"]["userId"] == 2 and \
           isinstance(response_3_json["data"]["userBalance"], float) and \
           response_5_json["data"]["currency"] == "EUR"


def test_balance_status_invalid_arguments(test_client):
    """
        GIVEN GET request to api/v1.0/balance/users
        WHEN user ID or currency is invalid or user is not in the DB
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

    # Correct user ID and currency, user is not in the DB
    response_9 = test_client.get("api/v1.0/balance/users?user_id=5&currency=RUB")
    response_9_json = json.loads(response_9.data)

    assert response_1.status_code == 400
    assert response_2.status_code == 400
    assert response_3.status_code == 400 and \
           response_3_json["data"]["userId"] is None and \
           response_3_json["data"]["userBalance"] is None and \
           response_3_json["data"]["currency"] == "RUB"
    assert response_4.status_code == 400 and \
           response_4_json["data"]["userId"] is None and \
           response_4_json["data"]["userBalance"] is None and \
           response_4_json["data"]["currency"] == "RUB"
    assert response_5.status_code == 400 and \
           response_5_json["data"]["userId"] is None and \
           response_5_json["data"]["userBalance"] is None and \
           response_5_json["data"]["currency"] == "RUB"
    assert response_6.status_code == 400 and \
           response_6_json["data"]["userId"] == 1 and \
           response_6_json["data"]["userBalance"] == float(10000) and \
           response_6_json["data"]["currency"] == "RUB"
    assert response_7.status_code == 400 and \
           response_7_json["data"]["userId"] == 1 and \
           response_7_json["data"]["userBalance"] == float(10000) and \
           response_7_json["data"]["currency"] == "RUB"
    assert response_8.status_code == 400 and \
           response_8_json["data"]["userId"] == 1 and \
           response_8_json["data"]["userBalance"] == float(10000) and \
           response_8_json["data"]["currency"] == "RUB"
    assert response_9.status_code == 404 and \
           response_9_json["data"]["userId"] == 5 and \
           response_9_json["data"]["userBalance"] is None and \
           response_9_json["data"]["currency"] == "RUB"


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
           response_1_json["data"]["amount"] == float(5000) and \
           response_1_json["data"]["currency"] == "RUB"
    assert response_2.status_code == 201 and \
           response_2_json["data"]["userId"] == 4 and \
           response_2_json["data"]["userBalance"] == float(5000) and \
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
           response_4_json["data"]["amount"] is None and \
           response_4_json["data"]["currency"] == "RUB"
    assert response_5.status_code == 400 and \
           response_5_json["data"]["userId"] is None and \
           response_5_json["data"]["userBalance"] is None and \
           response_5_json["data"]["amount"] is None and \
           response_5_json["data"]["currency"] == "RUB"
    assert response_6.status_code == 400 and \
           response_6_json["data"]["userId"] is None and \
           response_6_json["data"]["userBalance"] is None and \
           response_6_json["data"]["amount"] is None and \
           response_6_json["data"]["currency"] == "RUB"
    assert response_7.status_code == 400 and \
           response_7_json["data"]["userId"] == 1 and \
           response_7_json["data"]["userBalance"] == float(15000) and \
           response_7_json["data"]["amount"] is None and \
           response_7_json["data"]["currency"] == "RUB"
    assert response_8.status_code == 400 and \
           response_8_json["data"]["userId"] == 1 and \
           response_8_json["data"]["userBalance"] == float(15000) and \
           response_8_json["data"]["amount"] is None and \
           response_8_json["data"]["currency"] == "RUB"
    assert response_9.status_code == 400 and \
           response_9_json["data"]["userId"] == 1 and \
           response_9_json["data"]["userBalance"] == float(15000) and \
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
           response_4_json["data"]["amount"] is None and \
           response_4_json["data"]["currency"] == "RUB"
    assert response_5.status_code == 400 and \
           response_5_json["data"]["userId"] is None and \
           response_5_json["data"]["userBalance"] is None and \
           response_5_json["data"]["amount"] is None and \
           response_5_json["data"]["currency"] == "RUB"
    assert response_6.status_code == 400 and \
           response_6_json["data"]["userId"] is None and \
           response_6_json["data"]["userBalance"] is None and \
           response_6_json["data"]["amount"] is None and \
           response_6_json["data"]["currency"] == "RUB"
    assert response_7.status_code == 400 and \
           response_7_json["data"]["userId"] == 1 and \
           response_7_json["data"]["userBalance"] == float(10000) and \
           response_7_json["data"]["amount"] is None and \
           response_7_json["data"]["currency"] == "RUB"
    assert response_8.status_code == 400 and \
           response_8_json["data"]["userId"] == 1 and \
           response_8_json["data"]["userBalance"] == float(10000) and \
           response_8_json["data"]["amount"] is None and \
           response_8_json["data"]["currency"] == "RUB"
    assert response_9.status_code == 400 and \
           response_9_json["data"]["userId"] == 1 and \
           response_9_json["data"]["userBalance"] == float(10000) and \
           response_9_json["data"]["amount"] is None and \
           response_9_json["data"]["currency"] == "RUB"
    assert response_10.status_code == 400 and \
           response_10_json["data"]["userId"] == 5 and \
           response_10_json["data"]["userBalance"] is None and \
           response_10_json["data"]["amount"] == float(5000) and \
           response_10_json["data"]["currency"] == "RUB"
    assert response_11.status_code == 400 and \
           response_11_json["data"]["userId"] == 1 and \
           response_11_json["data"]["userBalance"] == float(10000) and \
           response_11_json["data"]["amount"] == float(11000) and \
           response_11_json["data"]["currency"] == "RUB"


def test_money_transfer_valid_arguments(test_client):
    """
    GIVEN PUT request to api/v1.0/transfer/users
    WHEN sender_uid and receiver_uid are valid
    THEN check the response
    """
    # Correct sender_uid and receiver_uid. The users are in DB
    response_1 = test_client.put("api/v1.0/transfer/users?sender_uid=1&receiver_uid=2&amount=5000")
    response_1_json = json.loads(response_1.data)

    assert response_1.status_code == 200 and \
           response_1_json["data"]["sender"]["id"] == 1 and \
           response_1_json["data"]["sender"]["balance"] == float(5000) and \
           response_1_json["data"]["receiver"]["id"] == 2 and \
           response_1_json["data"]["receiver"]["balance"] == float(20000) and \
           response_1_json["data"]["amount"] == float(5000) and \
           response_1_json["data"]["currency"] == "RUB"


def test_money_transfer_invalid_arguments(test_client):
    """
    GIVEN PUT request to api/v1.0/transfer/users
    WHEN sender_uid or receiver_uid or amount is invalid
    THEN check the response
    """

    # No arguments
    response_1 = test_client.put("api/v1.0/transfer/users")

    # Only sender_uid
    response_2 = test_client.put("api/v1.0/transfer/users?sender_uid=1")

    # Only receiver_uid
    response_3 = test_client.put("api/v1.0/transfer/users?receiver_uid=2")

    # Only amount
    response_4 = test_client.put("api/v1.0/transfer/users?amount=5000")

    # Only sender_uid and receiver_uid, no amount
    response_5 = test_client.put("api/v1.0/transfer/users?sender_uid=1&receiver_uid=2")

    # Only sender_uid and amount, no receiver_uid
    response_6 = test_client.put("api/v1.0/transfer/users?sender_uid=1&amount=5000")

    # Only receiver_uid and amount, no sender_uid
    response_7 = test_client.put("api/v1.0/transfer/users?receiver_uid=2&amount=5000")

    # Wrong sender_uid
    response_8 = test_client.put("api/v1.0/transfer/users?sender_uid=0&receiver_uid=2&amount=5000")
    response_8_json = json.loads(response_8.data)
    response_9 = test_client.put("api/v1.0/transfer/users?sender_uid=-1&receiver_uid=2&amount=5000")
    response_9_json = json.loads(response_9.data)
    response_10 = test_client.put("api/v1.0/transfer/users?sender_uid=zzz&receiver_uid=2&amount=5000")
    response_10_json = json.loads(response_10.data)

    # Wrong receiver_uid
    response_11 = test_client.put("api/v1.0/transfer/users?sender_uid=1&receiver_uid=0&amount=5000")
    response_11_json = json.loads(response_11.data)
    response_12 = test_client.put("api/v1.0/transfer/users?sender_uid=1&receiver_uid=-1&amount=5000")
    response_12_json = json.loads(response_12.data)
    response_13 = test_client.put("api/v1.0/transfer/users?sender_uid=1&receiver_uid=zzz&amount=5000")
    response_13_json = json.loads(response_13.data)

    # Wrong amount
    response_14 = test_client.put("api/v1.0/transfer/users?sender_uid=1&receiver_uid=2&amount=0")
    response_14_json = json.loads(response_14.data)
    response_15 = test_client.put("api/v1.0/transfer/users?sender_uid=1&receiver_uid=2&amount=-1")
    response_15_json = json.loads(response_15.data)
    response_16 = test_client.put("api/v1.0/transfer/users?sender_uid=1&receiver_uid=2&amount=zzz")
    response_16_json = json.loads(response_16.data)

    # Correct arguments. sender_uid not in DB
    response_17 = test_client.put("api/v1.0/transfer/users?sender_uid=11&receiver_uid=2&amount=5000")
    response_17_json = json.loads(response_17.data)

    # Correct arguments. receiver_uid not in DB
    response_18 = test_client.put("api/v1.0/transfer/users?sender_uid=1&receiver_uid=22&amount=5000")
    response_18_json = json.loads(response_18.data)

    # Correct arguments. sender_uid and receiver_uid not in DB
    response_19 = test_client.put("api/v1.0/transfer/users?sender_uid=11&receiver_uid=22&amount=5000")
    response_19_json = json.loads(response_19.data)

    # Correct arguments. Amount > sender's balance
    response_20 = test_client.put("api/v1.0/transfer/users?sender_uid=1&receiver_uid=2&amount=7000")
    response_20_json = json.loads(response_20.data)

    assert response_1.status_code == 400
    assert response_2.status_code == 400
    assert response_3.status_code == 400
    assert response_4.status_code == 400
    assert response_5.status_code == 400
    assert response_6.status_code == 400
    assert response_7.status_code == 400
    assert response_8.status_code == 400 and \
           response_8_json["data"]["sender"]["id"] is None and \
           response_8_json["data"]["receiver"]["id"] is None and \
           response_8_json["data"]["amount"] is None and \
           response_8_json["data"]["currency"] == "RUB"
    assert response_9.status_code == 400 and \
           response_9_json["data"]["sender"]["id"] is None and \
           response_9_json["data"]["receiver"]["id"] is None and \
           response_9_json["data"]["amount"] is None and \
           response_9_json["data"]["currency"] == "RUB"
    assert response_10.status_code == 400 and \
           response_10_json["data"]["sender"]["id"] is None and \
           response_10_json["data"]["receiver"]["id"] is None and \
           response_10_json["data"]["amount"] is None and \
           response_10_json["data"]["currency"] == "RUB"
    assert response_11.status_code == 400 and \
           response_11_json["data"]["sender"]["id"] == 1 and \
           response_11_json["data"]["sender"]["balance"] == float(5000) and \
           response_11_json["data"]["receiver"]["id"] is None and \
           response_11_json["data"]["amount"] is None and \
           response_11_json["data"]["currency"] == "RUB"
    assert response_12.status_code == 400 and \
           response_12_json["data"]["sender"]["id"] == 1 and \
           response_12_json["data"]["sender"]["balance"] == float(5000) and \
           response_12_json["data"]["receiver"]["id"] is None and \
           response_12_json["data"]["amount"] is None and \
           response_12_json["data"]["currency"] == "RUB"
    assert response_13.status_code == 400 and \
           response_13_json["data"]["sender"]["id"] == 1 and \
           response_13_json["data"]["sender"]["balance"] == float(5000) and \
           response_13_json["data"]["receiver"]["id"] is None and \
           response_13_json["data"]["amount"] is None and \
           response_13_json["data"]["currency"] == "RUB"
    assert response_14.status_code == 400 and \
           response_14_json["data"]["sender"]["id"] == 1 and \
           response_14_json["data"]["sender"]["balance"] == float(5000) and \
           response_14_json["data"]["receiver"]["id"] == 2 and \
           response_14_json["data"]["receiver"]["balance"] == float(20000) and \
           response_14_json["data"]["amount"] is None and \
           response_14_json["data"]["currency"] == "RUB"
    assert response_15.status_code == 400 and \
           response_15_json["data"]["sender"]["id"] == 1 and \
           response_15_json["data"]["sender"]["balance"] == float(5000) and \
           response_15_json["data"]["receiver"]["id"] == 2 and \
           response_15_json["data"]["receiver"]["balance"] == float(20000) and \
           response_15_json["data"]["amount"] is None and \
           response_15_json["data"]["currency"] == "RUB"
    assert response_16.status_code == 400 and \
           response_16_json["data"]["sender"]["id"] == 1 and \
           response_16_json["data"]["sender"]["balance"] == float(5000) and \
           response_16_json["data"]["receiver"]["id"] == 2 and \
           response_16_json["data"]["receiver"]["balance"] == float(20000) and \
           response_16_json["data"]["amount"] is None and \
           response_16_json["data"]["currency"] == "RUB"
    assert response_17.status_code == 400 and \
           response_17_json["data"]["sender"]["id"] == 11 and \
           response_17_json["data"]["sender"]["balance"] is None and \
           response_17_json["data"]["receiver"]["id"] == 2 and \
           response_17_json["data"]["receiver"]["balance"] == float(20000) and \
           response_17_json["data"]["amount"] is None and \
           response_17_json["data"]["currency"] == "RUB"
    assert response_18.status_code == 400 and \
           response_18_json["data"]["sender"]["id"] == 1 and \
           response_18_json["data"]["sender"]["balance"] == float(5000) and \
           response_18_json["data"]["receiver"]["id"] == 22 and \
           response_18_json["data"]["receiver"]["balance"] is None and \
           response_18_json["data"]["amount"] is None and \
           response_18_json["data"]["currency"] == "RUB"
    assert response_19.status_code == 400 and \
           response_19_json["data"]["sender"]["id"] == 11 and \
           response_19_json["data"]["sender"]["balance"] is None and \
           response_19_json["data"]["receiver"]["id"] == 22 and \
           response_19_json["data"]["receiver"]["balance"] is None and \
           response_19_json["data"]["amount"] is None and \
           response_19_json["data"]["currency"] == "RUB"
    assert response_20.status_code == 400 and \
           response_20_json["data"]["sender"]["id"] == 1 and \
           response_20_json["data"]["sender"]["balance"] == float(5000) and \
           response_20_json["data"]["receiver"]["id"] == 2 and \
           response_20_json["data"]["receiver"]["balance"] == float(20000) and \
           response_20_json["data"]["amount"] == float(7000) and \
           response_20_json["data"]["currency"] == "RUB"


def test_detailed_transactions_valid_arguments(test_client):
    """
    GIVEN GET request to api/v1.0/transactions/users
    WHEN user_id is valid
    THEN check the response
    """
    # Correct user_id. The users is in DB
    response_1 = test_client.get("api/v1.0/transactions/users?user_id=1")
    response_1_json = json.loads(response_1.data)
    response_2 = test_client.get("api/v1.0/transactions/users?user_id=2")
    response_2_json = json.loads(response_2.data)
    response_3 = test_client.get("api/v1.0/transactions/users?user_id=3")
    response_3_json = json.loads(response_3.data)
    response_4 = test_client.get("api/v1.0/transactions/users?user_id=4")
    response_4_json = json.loads(response_4.data)

    # Correct user_id. The users is not in DB
    response_5 = test_client.get("api/v1.0/transactions/users?user_id=5")
    response_5_json = json.loads(response_5.data)

    assert response_1.status_code == 200 and \
           response_1_json["data"]["userId"] == 1 and \
           len(response_1_json["data"]["transactions"]) == 4
    assert response_2.status_code == 200 and \
           response_2_json["data"]["userId"] == 2 and \
           len(response_2_json["data"]["transactions"]) == 2
    assert response_3.status_code == 200 and \
           response_3_json["data"]["userId"] == 3 and \
           len(response_3_json["data"]["transactions"]) == 1
    assert response_4.status_code == 200 and \
           response_4_json["data"]["userId"] == 4 and \
           len(response_4_json["data"]["transactions"]) == 1
    assert response_5.status_code == 200 and \
           response_5_json["data"]["userId"] == 5 and \
           len(response_5_json["data"]["transactions"]) == 0


def test_detailed_transactions_invalid_arguments(test_client):
    """
    GIVEN GET request to api/v1.0/transactions/users
    WHEN user_id is invalid
    THEN check the response
    """
    # No arguments
    response_1 = test_client.get("api/v1.0/transactions/users")

    # Wrong user ID
    response_2 = test_client.get("api/v1.0/transactions/users?user_id=-1")
    response_2_json = json.loads(response_2.data)
    response_3 = test_client.get("api/v1.0/transactions/users?user_id=0")
    response_3_json = json.loads(response_3.data)
    response_4 = test_client.get("api/v1.0/transactions/users?user_id=abc")
    response_4_json = json.loads(response_4.data)

    assert response_1.status_code == 400
    assert response_2.status_code == 400 and \
           response_2_json["data"]["userId"] is None and \
           len(response_2_json["data"]["transactions"]) == 0
    assert response_3.status_code == 400 and \
           response_3_json["data"]["userId"] is None and \
           len(response_3_json["data"]["transactions"]) == 0
    assert response_4.status_code == 400 and \
           response_4_json["data"]["userId"] is None and \
           len(response_4_json["data"]["transactions"]) == 0
