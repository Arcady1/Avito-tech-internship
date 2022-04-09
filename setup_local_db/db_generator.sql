CREATE DATABASE IF NOT EXISTS avito;

USE avito;

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    balance FLOAT(32)
);

CREATE TABLE IF NOT EXISTS transactions (
    id VARCHAR(40) NOT NULL PRIMARY KEY,
    sender_uid INT,
    receiver_uid INT,
    date_ TIMESTAMP NOT NULL,
    type_ VARCHAR(20) NOT NULL,
    amount FLOAT(32) NOT NULL
);

CREATE TABLE IF NOT EXISTS user_transactions (
    uid INT NOT NULL,
    tid VARCHAR(40) NOT NULL,
    FOREIGN KEY (uid) REFERENCES users(id),
    FOREIGN KEY (tid) REFERENCES transactions(id)
);

SET FOREIGN_KEY_CHECKS=0;
TRUNCATE TABLE avito.users;
TRUNCATE TABLE avito.transactions;
TRUNCATE TABLE avito.user_transactions;
SET FOREIGN_KEY_CHECKS=1;
