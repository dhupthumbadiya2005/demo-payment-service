import logging

logger = logging.getLogger("payments")

def log_transaction(transaction_id, amount, status):
    logger.info(f"Transaction {transaction_id}: {amount} - {status}")
