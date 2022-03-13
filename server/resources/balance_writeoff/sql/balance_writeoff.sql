UPDATE users
SET balance = $current_balance - $amount
WHERE id = $user_id;
