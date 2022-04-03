## Доработать

* Написать скрипт с командами для создания всех файлов
* В том чсисле установка зависимостей
* Написать документацию
    * Весь код должен быть выложен на Github с Readme файлом с инструкцией по запуску и примерами запросов/ответов (
      можно просто описать в Readme методы, можно через Postman, можно в Readme curl запросы скопировать, вы поняли
      идею...)
* Сделать пагинацию при возврате ответа
* Обновить requrements.txt
* Подготовиться к вопросам по Go

---

Запуск тестов: ```python -m pytest --cov-report html:cov_html --cov-report term --cov=.```

Команды:
* ```--cov-report html:cov_html``` - генерация cov_html папки. Открыть index.html для просмотра подробого отчета
* ```--cov-report term``` - отобразить покрытие тестами каждого файла в консоли
* ```--cov=.``` - указание проекта 

1. В .env_dev изменить:
   1. MYSQL_LOCAL_HOST_PROD на имя хоста (обчно localhost) 
   2. MYSQL_LOCAL_USER_PROD на имя пользователя
   3. MYSQL_LOCAL_PASSWORD_PROD на пароль хоста
   4. MYSQL_LOCAL_PORT_PROD на порт
2. Переименовать .env_dev в .env



## API endpoints

---

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
| status              | The status of the request.                           |
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
| status              | The status of the request.                                     |
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
| status              | The status of the request.                                     |
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
| status                      | The status of the request.                                     |
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
| status                                  | The status of the request.                        |
| message                                 | Status description.                               |
| description                             | Additional information about the response.        |
| data -> userId                          | The requested user ID.                            |
| data -> transactions -> transactionName | The name of the transaction.                      |
| data -> transactions -> amount          | The amount that was processed in the transaction. |
| data -> transactions -> date            | The transaction date.                             |
| data -> transactions -> senderUid       | The ID of the user who sent money.                |
| data -> transactions -> receiverUid     | The ID of the user who received money.            |













---

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




