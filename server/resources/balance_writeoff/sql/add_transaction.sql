INSERT INTO transactions (id, sender_uid, date_, type_)
VALUES ("$transaction_id", $user_id, CURRENT_TIMESTAMP, "$type_");