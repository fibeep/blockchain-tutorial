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
        pass

    @property

    def last_block(self):

        #Calls and returns the last block of a chain

        pass



