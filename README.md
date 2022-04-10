## Fundamental requirements
- Git 
- Pip
- Python 3.8

## How to use (without Docker)
Clone the repository and open it:
```shell
$ git clone https://github.com/Arcady1/Eye-tracker.git
$ cd Avito-tech-internship/
```

Copy `.env.example` file and rename it to `.env`. Fill in the blank fields:
```commandline
APP_PORT=8080

SECRET_KEY_DEV=7eb160d4-09x0-4792-pbzd-5909ba7a78c3
SECRET_KEY_TEST=21lm8460-e590-4943-9099-011z823242a8

MYSQL_LOCAL_HOST_DEV=localhost
MYSQL_LOCAL_USER_DEV=___
MYSQL_LOCAL_PASSWORD_DEV=___
MYSQL_LOCAL_DB_DEV=avito
MYSQL_LOCAL_PORT_DEV=3306

MYSQL_LOCAL_DB_TEST=avito_test

CURRENCY_CONVERTER_API_KEY=2daf17a0533b9f07c90721646ef5963ce6a5f3ea
```

Start the MySQL script from `/init/init.sql` file to generate a new schema and tables.

Create and activate a new virtual environment.

Install all the requirements with `pip`:
```shell
$ pip install -r requirements.txt
```
Start the server.
```shell
$ python run.py
```


## Testing

Start the MySQL script from `/tests/tests_db/init.sql` file to generate the tests schema and tables.

Start tests without coverage:
```shell
$ python -m pytest
```

Or start tests with coverage:
```shell
$ python -m pytest --cov-report html:cov_html --cov-report term --cov=.
```

`--cov-report html:cov_html` generates `cov_html` folder. Open `cov_html/index.html` to view the detailed report.

`--cov-report term` allows to display the test coverage of each file in the terminal.

`--cov=.` indicates the project path.

## API endpoints

### Get the user balance by ID 

_Endpoint:_

```GET: http://127.0.0.1:8080/api/v1.0/balance/users```

_Example request:_

```
GET: http://127.0.0.1:8080/api/v1.0/balance/users
?user_id={UserID}
&currency=RUB
```

_Request parameters:_

| Parameter | Description                                                            | Required |
|-----------|------------------------------------------------------------------------|----------|
| user_id   | The ID of the user whose balance you want to check.                    | True     |
| currency  | Currency in which you need to receive the balance: RUB, EUR, USD, etc. | False    |

_The example of the response for the user_id **1**_

```json
{
    "status": 200,
    "message": "Success: getting a users' balance in the database by ID",
    "description": "",
    "data": {
        "userId": 1,
        "userBalance": 5000.0,
        "currency": "RUB"
    }
}
```

_Response object:_

| Property            | Description                                          | 
|---------------------|------------------------------------------------------|
| status              | The status of the response.                          |
| message             | Status description.                                  |
| description         | Additional information about the response.           |
| data -> userId      | The requested user ID.                               |
| data -> userBalance | The current user balance.                            |
| data -> currency    | The selected currency in which the balance is shown. |

---
### Refill the user balance by ID

_Endpoint:_

```PUT: http://127.0.0.1:8080/api/v1.0/refill/users```

_Example request:_

```
PUT: http://127.0.0.1:8080/api/v1.0/refill/users
?user_id={UserID}
&amount=5000
```

_Request parameters:_

| Parameter | Description                                          | Required |
|-----------|------------------------------------------------------|----------|
| user_id   | The ID of the user whose balance you want to refill. | True     |
| amount    | The amount to be credited to the user account.       | True     |

_The example of the response for the user_id **1**_

```json
{
    "status": 200,
    "message": "Success: user balance increase",
    "description": "",
    "data": {
        "userId": 1,
        "userBalance": 10000.0,
        "currency": "RUB",
        "amount": 5000.0
    }
}
```

_Response object:_

| Property            | Description                                                    | 
|---------------------|----------------------------------------------------------------|
| status              | The status of the response.                                    |
| message             | Status description.                                            |
| description         | Additional information about the response.                     |
| data -> userId      | The requested user ID.                                         |
| data -> userBalance | The current user balance.                                      |
| data -> currency    | The currency in which the user balance is indicated. Only RUB. |
| data -> amount      | The credit amount.                                             |

---
### Write-off money from the user's balance by ID

_Endpoint:_

```PUT: http://127.0.0.1:8080/api/v1.0/writeoff/users```

_Example request:_

```
PUT: http://127.0.0.1:8080/api/v1.0/writeoff/users
?user_id={UserID}
&amount=2500
```

_Request parameters:_

| Parameter | Description                                                 | Required |
|-----------|-------------------------------------------------------------|----------|
| user_id   | The user ID from whose balance you want to write off money. | True     |
| amount    | Amount to be debited from the user's balance.               | True     |

_The example of the response for the user_id **1**_

```json
{
    "status": 200,
    "message": "Success: write-off was successful",
    "description": "",
    "data": {
        "userId": 1,
        "userBalance": 7500.0,
        "currency": "RUB",
        "amount": 2500.0
    }
}
```

_Response object:_

| Property            | Description                                                    | 
|---------------------|----------------------------------------------------------------|
| status              | The status of the response.                                    |
| message             | Status description.                                            |
| description         | Additional information about the response.                     |
| data -> userId      | The requested user ID.                                         |
| data -> userBalance | The current user balance.                                      |
| data -> currency    | The currency in which the user balance is indicated. Only RUB. |
| data -> amount      | The write-off amount.                                          |

---
### Transfer money between the users accounts

_Endpoint:_

```PUT: http://127.0.0.1:8080/api/v1.0/transfer/users```

_Example request:_

```
PUT: http://127.0.0.1:8080/api/v1.0/transfer/users
?sender_uid={SenderUserID}
&receiver_uid={ReceiverUserID}
&amount=15000
```

_Request parameters:_

| Parameter    | Description           | Required |
|--------------|-----------------------|----------|
| sender_uid   | The sender user ID.   | True     |
| receiver_uid | The receiver user ID. | True     |
| amount       | The transfer amount.  | True     |

_The example of the response for the sender_uid **2**, receiver_uid **1**_

```json
{
    "status": 200,
    "message": "Success: money transfer",
    "description": "",
    "data": {
        "currency": "RUB",
        "sender": {
            "id": 2,
            "balance": 5000.0
        },
        "receiver": {
            "id": 1,
            "balance": 22500.0
        },
        "amount": 15000.0
    }
}
```

_Response object:_

| Property                    | Description                                                    | 
|-----------------------------|----------------------------------------------------------------|
| status                      | The status of the response.                                    |
| message                     | Status description.                                            |
| description                 | Additional information about the response.                     |
| data -> currency            | The currency in which the user balance is indicated. Only RUB. |
| data -> sender -> id        | The user ID who is sending money.                              |
| data -> sender -> balance   | The user balance who is sending money.                         |
| data -> receiver -> id      | The user ID who is receiving money.                            |
| data -> receiver -> balance | The user balance who is receiving money.                       |
| data -> amount              | The amount of transfer between accounts.                       |

---
### Get a list of user transactions by ID

_Endpoint:_

```GET: http://127.0.0.1:8080/api/v1.0/transactions/users```

_Example request:_

```
GET: http://127.0.0.1:8080/api/v1.0/transactions/users
user_id={UserID}
```

_Request parameters:_

| Parameter | Description                                                      | Required |
|-----------|------------------------------------------------------------------|----------|
| user_id   | The ID of the user whose transactions list you want to retrieve. | True     |

_The example of the response for the user_id **1**_

```json
{
    "status": 200,
    "message": "Success: getting users' detailed transactions",
    "description": "",
    "data": {
        "userId": 1,
        "transactions": [
            {
                "transactionName": "Money transfer",
                "amount": 15000.0,
                "date": "2022-03-30, 21:00:25",
                "senderUid": 2,
                "receiverUid": 1
            },
            {
                "transactionName": "Write-off",
                "amount": 2500.0,
                "date": "2022-03-30, 20:58:12"
            },
            {
                "transactionName": "Refill",
                "amount": 5000.0,
                "date": "2022-03-30, 20:53:58"
            },
            {
                "transactionName": "Refill",
                "amount": 5000.0,
                "date": "2022-03-30, 20:53:36"
            }
        ]
    }
}
```

_Response object:_

| Property                                | Description                                       | 
|-----------------------------------------|---------------------------------------------------|
| status                                  | The status of the response.                       |
| message                                 | Status description.                               |
| description                             | Additional information about the response.        |
| data -> userId                          | The requested user ID.                            |
| data -> transactions -> transactionName | The name of the transaction.                      |
| data -> transactions -> amount          | The amount that was processed in the transaction. |
| data -> transactions -> date            | The transaction date.                             |
| data -> transactions -> senderUid       | The ID of the user who sent money.                |
| data -> transactions -> receiverUid     | The ID of the user who received money.            |

## Errors

In case the request fails an error will be returned in JSON format.

_Error response example:_

```json
{
    "status": 400,
    "message": "Error: transfering user balance to 'ASD'",
    "description": "Check the query parameters",
    "data": {
        "userId": 1,
        "userBalance": 5000.0,
        "currency": "RUB"
    }
}
```

_Error codes:_

| Code | Description                                             | 
|------|---------------------------------------------------------|
| 400  | Bad request.                                            |
| 404  | Resource is not found or requested format is incorrect. |
| 405  | Method is not allowed.                                  |
| 500  | Server error.                                           |
