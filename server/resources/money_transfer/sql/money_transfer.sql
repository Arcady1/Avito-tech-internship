UPDATE users
SET balance = $sender_balance - $amount
WHERE id = $sender_uid;

UPDATE users
SET balance = $receiver_balance + $amount
WHERE id = $receiver_uid;