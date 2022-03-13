INSERT INTO transactions (id, sender_uid, reciever_uid, date_, type_, amount)
VALUES ("$transaction_id", $sender_uid, $reciever_uid, CURRENT_TIMESTAMP, "$type_", $amount);