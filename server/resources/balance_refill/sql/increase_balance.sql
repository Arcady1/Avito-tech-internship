UPDATE users
SET balance=balance + $amount
WHERE id=$user_id;
