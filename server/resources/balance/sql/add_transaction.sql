INSERT INTO transactions (id, $user_column, date_, type_, amount)
VALUES ("$transaction_id", $user_id, CURRENT_TIMESTAMP, "$type_", $amount);