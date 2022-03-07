UPDATE users
SET balance=$balance_after_debit
WHERE id=$uid;