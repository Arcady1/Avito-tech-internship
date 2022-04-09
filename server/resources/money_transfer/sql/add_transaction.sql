INSERT INTO transactions (id, sender_uid, receiver_uid, date_, type_, amount)
VALUES ("$transaction_id", $sender_uid, $receiver_uid, CURRENT_TIMESTAMP, "$type_", $amount);