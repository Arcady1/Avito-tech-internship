<h1 align="center">
    <img src="https://m.foolcdn.com/media/affiliates/images/Bank_to_bank_GettyImages-900917830_QB3CjfS.width-1200.jpg" alt="" width="200px"></img>
</h1>

This is a [test assignment for an internship in Avito][1].
Developed an API with Flask to work with the balance of the user.

## Fundamental requirements
- Git
- Pip
- Python 3.8.10
- MySQL 8.0.28
- Docker (optional)
- Docker-compose (optional)

## How to use 
Clone the repository and open it:
```shell
$ git clone https://github.com/Arcady1/Avito-tech-internship.git
$ cd Avito-tech-internship/
```

#### Without Docker

Copy `.env.example` file and rename it to `.env`. Fill in the blank fields:
```commandline
APP_PORT=5000

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

Start the MySQL script from `/init_db/main.sql` file to generate a new schema and tables.

Create and activate a new virtual environment.

Install all the requirements with `pip`:
```shell
$ pip install -r requirements.txt
```
Start the server:
```shell
$ export FLASK_APP=run.py && flask run
```

#### With Docker

Copy `.env.docker` file and rename it to `.env`.
```commandline
APP_PORT=5000

SECRET_KEY_DEV=Xkai60d4-09x0-4792-Mlzd-KJio7a9179C3
SECRET_KEY_TEST=29aPLuI0-pd90-9172-mN9a-08akxP28xka8

MYSQL_LOCAL_HOST_DEV=database
MYSQL_LOCAL_USER_DEV=root
MYSQL_LOCAL_PASSWORD_DEV=root
MYSQL_LOCAL_DB_DEV=avito
MYSQL_LOCAL_PORT_DEV=3306

MYSQL_LOCAL_DB_TEST=avito_test

CURRENCY_CONVERTER_API_KEY=2daf17a0533b9f07c90721646ef5963ce6a5f3ea
```

Start docker:
```shell
$ docker-compose up --build
```

## Testing 

#### Without Docker

Start the MySQL script from `/init_db/tests.sql` file to generate the test schema and tables.

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

#### With Docker

Start the docker server as shown above.

Run the command:
```shell
$ docker-compose exec server python -m pytest --cov-report term --cov=.
```

**Note:** if you run the tests again, you have to rerun the MySQL script from `/init_db/tests.sql`.

## API endpoints

Use `http://127.0.0.1:5000` host.

### Get the user balance by ID 

Endpoint:

```HTTP GET /api/v1.0/balance/users```

Example request:

```
HTTP GET /api/v1.0/balance/users
?user_id={UserID}
&currency=RUB
```

Request parameters:

| Parameter | Description                                                            | Required |
|-----------|------------------------------------------------------------------------|----------|
| user_id   | The ID of the user whose balance you want to check.                    | True     |
| currency  | Currency in which you need to receive the balance: RUB, EUR, USD, etc. | False    |

The example of the response for the user_id **1**

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

Response object:

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

Endpoint:

```HTTP PUT /api/v1.0/refill/users```

Example request:

```
HTTP PUT /api/v1.0/refill/users
?user_id={UserID}
&amount=5000
```

Request parameters:

| Parameter | Description                                          | Required |
|-----------|------------------------------------------------------|----------|
| user_id   | The ID of the user whose balance you want to refill. | True     |
| amount    | The amount to be credited to the user account.       | True     |

The example of the response for the user_id **1**

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

Response object:

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

Endpoint:

```HTTP PUT /api/v1.0/writeoff/users```

Example request:

```
HTTP PUT /api/v1.0/writeoff/users
?user_id={UserID}
&amount=2500
```

Request parameters:

| Parameter | Description                                                 | Required |
|-----------|-------------------------------------------------------------|----------|
| user_id   | The user ID from whose balance you want to write off money. | True     |
| amount    | Amount to be debited from the user's balance.               | True     |

The example of the response for the user_id **1**

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

Response object:

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

Endpoint:

```HTTP PUT /api/v1.0/transfer/users```

Example request:

```
HTTP PUT /api/v1.0/transfer/users
?sender_uid={SenderUserID}
&receiver_uid={ReceiverUserID}
&amount=15000
```

Request parameters:

| Parameter    | Description           | Required |
|--------------|-----------------------|----------|
| sender_uid   | The sender user ID.   | True     |
| receiver_uid | The receiver user ID. | True     |
| amount       | The transfer amount.  | True     |

The example of the response for the sender_uid **2**, receiver_uid **1**

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

Response object:

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

Endpoint:

```HTTP GET /api/v1.0/transactions/users```

Example request:

```
HTTP GET /api/v1.0/transactions/users
user_id={UserID}
```

Request parameters:

| Parameter | Description                                                      | Required |
|-----------|------------------------------------------------------------------|----------|
| user_id   | The ID of the user whose transactions list you want to retrieve. | True     |

The example of the response for the user_id **1**

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

Response object:

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

Error response example:

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

Error codes:

| Code | Description                                             | 
|------|---------------------------------------------------------|
| 400  | Bad request.                                            |
| 404  | Resource is not found or requested format is incorrect. |
| 405  | Method is not allowed.                                  |
| 500  | Server error.                                           |

## License
MIT

[1]: https://github.com/avito-tech/job-backend-trainee-assignment
