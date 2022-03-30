CREATE DATABASE avito;

USE avito;

CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    balance FLOAT(32)
);

CREATE TABLE transactions (
    id VARCHAR(40) NOT NULL PRIMARY KEY,
    sender_uid INT,
    receiver_uid INT,
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

