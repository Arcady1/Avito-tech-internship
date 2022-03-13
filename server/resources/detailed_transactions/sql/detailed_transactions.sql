WITH user_trans AS (
	SELECT * FROM (
		SELECT users.id as uid, user_transactions.tid as tid
		FROM users JOIN user_transactions
		ON users.id = user_transactions.uid) AS Tmp
		WHERE uid = $user_id
)

SELECT transactions.sender_uid, transactions.reciever_uid, transactions.date_, transactions.type_, transactions.amount
FROM user_trans JOIN transactions
ON user_trans.tid = transactions.id
ORDER BY date_ DESC, amount DESC;