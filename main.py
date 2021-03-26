import json

genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': [],
    'proof': 100
}
# Initializing our (empty) blockchain list
blockchain = [genesis_block]
# Unhandled transactions
open_transactions = []