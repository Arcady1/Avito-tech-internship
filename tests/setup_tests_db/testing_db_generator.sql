-- Creating "avito_test" DB
DROP DATABASE IF EXISTS avito_test;
CREATE DATABASE avito_test;
USE avito_test;

-- Creating tables
CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    balance FLOAT(32)
);

CREATE TABLE transactions (
    id VARCHAR(40) NOT NULL PRIMARY KEY,
    sender_uid INT,
    reciever_uid INT,
    date_ TIMESTAMP NOT NULL,
    type_ VARCHAR(20) NOT NULL,
    amount FLOAT(32) NOT NULL
);

CREATE TABLE user_transactions (
    uid INT NOT NULL,
    tid VARCHAR(40) NOT NULL,
    FOREIGN KEY (uid) REFERENCES users(id),
    FOREIGN KEY (tid) REFERENCES transactions(id)
);

-- Filling the tables
INSERT INTO users (id, balance)
VALUES (1, 10000),
VALUES (2, 15000),
VALUES (3, 5000);

INSERT INTO transactions (id, sender_uid, reciever_uid, date_, type_, amount)
VALUES ("736af6fa-15ac-4a3f-9640-58c18214f259", NULL, 1, "2022-03-22 17:21:57", "Refill", 10000),
VALUES ("f2efff3a-08d7-42b8-b0f2-9bdc94a86a7a", NULL, 2, "2022-03-22 17:22:11", "Refill", 15000),
VALUES ("ac0979c2-96ef-4867-ac08-f1c527cb19c1", NULL, 3, "2022-03-22 17:22:19", "Refill", 5000);

INSERT INTO user_transactions (uid, tid)
VALUES (1, "736af6fa-15ac-4a3f-9640-58c18214f259"),
VALUES (2, "f2efff3a-08d7-42b8-b0f2-9bdc94a86a7a"),
VALUES (3, "ac0979c2-96ef-4867-ac08-f1c527cb19c1");