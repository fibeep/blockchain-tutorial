class Blockchain(object):
  
    def __init__(self):

        self.chain = []

        self.current_transactions = []

    def new_block(self):

        #this function creates blocks and adds them to the chain
        ''' This function will create a new transaction that will be sent to next block. It will include
        the following info: sender, recipient, amount'''
        pass


    def new_transaction(self):

        #This function adds a new transaction to already existing transactions
        
        pass


    @staticmethod

    def hash(block):
        # This function hashes blocks
        pass

    @property

    def last_block(self):

        #Calls and returns the last block of a chain

        pass



