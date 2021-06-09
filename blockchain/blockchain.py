import hashlib
import json
from time import time




class Blockchain(object):
  
    def __init__(self):

        self.chain = []
        
        self.current_transactions = []

        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):

        #this function creates blocks and adds them to the chain
        '''This method will contain two parameters proof, previous hash'''
        block = {
            'index': len(self.chain)+1,
            'timestamp': time(), #time is CLEARLY not right!
            'proof': proof,
            previous_hash: previous_hash or self.hash(self.chain[-1])
        }

        # Set current transaction list to empty
        self.current_transactions = []
        self.chain.append(block)
        return block


    def new_transaction(self):

        #This function adds a new transaction to already existing transactions
        ''' This function will create a new transaction that will be sent to next block. It will include
        the following info: sender, recipient, amount'''
        
        self.current_transactions.append(
            {
                'sender': sender,
                'recipient': recipient,
                'amount': amount
            }
        )

        return self.last_block['index'] + 1


    @staticmethod
    def hash(block):
        # This function hashes blocks
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexidigest()

    @property
    def last_block(self):

        #Calls and returns the last block of a chain

        return self.chain[-1]

    
    def proof_of_work(self, last_proof):
        '''This method is where the consensus algo is implemented.
        It takes two parameters, self and last_proof'''

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof
    
    @staticmethod
    def valid_proof(last_proof, proof):
        '''This method validates the block'''

        guess = f'{last_proof}{proof}'.encode()

        guess_hash = hashlib.sha256(guess).hexigest()

        return guess_hash[:4] == "0000"



