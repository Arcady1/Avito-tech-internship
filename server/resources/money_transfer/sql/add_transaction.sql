INSERT INTO transactions (id, sender_uid, reciever_uid, date_, type_)
VALUES ("$transaction_id", $sender_uid, $reciever_uid, CURRENT_TIMESTAMP, "$type_");