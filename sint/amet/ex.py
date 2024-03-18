contract_txn = contract.functions.swapExactETHForTokens(
    amount_out_min,
    path,
    to,
    deadline,
).buildTransaction(
    {
        "from": sender_address,
        "value": amount_in,
        "gas": 200000,
        "gasPrice": w3.toWei("5", "gwei"),
    }
)
