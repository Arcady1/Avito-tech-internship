UPDATE users
SET balance = $sender_balance - $amount
WHERE id = $sender_uid;

UPDATE users
SET balance = $reciever_balance + $amount
WHERE id = $reciever_uid;