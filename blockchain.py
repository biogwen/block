from hashlib import sha256
import json

#genesis
genesis ={
'previous_hash': '',
    'index': 0,
    'transactions': []
}


#definition du block
blockchain = [genesis]
#definition de la chaine
open_transactions = []

#split des blockchain entre formation et experience
class BlockFormation:
    def __init__(self, user, orga, title, start, end, description, diplome, verify, verify_who):
        self.type = "f"
        self.user = user
        self.orga = orga
        self.title = title
        self.start = start
        self.end = end
        self.description = description
        self.diplome = diplome
        self.verified = verify
        self.verify_who = verify_who



class BlockExperience:
    def __init__(self, user, entreprise, title, start, end, description, verified, verify_who, type):
        self.type = "e"
        self.user = user
        self.entreprise = entreprise
        self.title = title
        self.start = start
        self.end = end
        self.description = description
        self.verify_who = verify_who
        self.verified = verified
        self.type = type

def hash_block (self):
    block_string = json.dumps(self.__dict__, sort_keys=True)
    return sha256(block_string.encode()).hexdigest()

def mine_block():
    """Create a new block and add open transactions to it."""
    # Fetch the currently last block of the blockchain
    last_block = blockchain[-1]
    # Hash the last block (=> to be able to compare it to the stored hash value)
    hashed_block = hash_block(last_block)

    # Copy transaction instead of manipulating the original open_transactions list
    # This ensures that if for some reason the mining should fail, we don't have the reward transaction stored in the open transactions
    copied_transactions = open_transactions[:]
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': copied_transactions
    }
    blockchain.append(block)
    return True
