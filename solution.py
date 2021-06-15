# Import CSV to work with csv files
import csv
# storing filename in an object to append txids in later  stage
outputfile = open('block_sample.txt', 'r+')
# set initial weight of block to 0, and create an empty transaction block
total_weight = [0]
transactions_block = []

"""
Class Transaction
METHODS:-  
        check_weight- check if max_weight of block condition is satisfied
        check_parent- check if transaction have a prent of not
        validate_transaction- final check if transaction is valid or not
"""


class Transaction:

    def __init__(self, txid, fee, weight, parents):
        self.txid = txid
        self.fee = int(fee)
        self.weight = int(weight)
        self.parents = parents

    def check_weight(self):
        if total_weight[0]+self.weight <= 4000000:
            total_weight[0] += self.weight
            return True

    def check_parent(self):
        if self.parents:
            if self.parents in transactions_block:
                return True
        else:
            return True

    def validate_transaction(self):
        if self.check_weight() and self.check_parent():
            return self.txid
        else:
            return False

# read and parse CSV


def parse_mempool_csv():
    with open("mempool.csv") as f:
        data = [line.strip().split(',') for line in f.readlines()]
# validating each transaction
    for x, y in enumerate(data):

        if x != 0:
            # Object Creation for each transaction
            transaction_object = Transaction(*data[x])
            taxid = transaction_object.validate_transaction()

            if taxid:
                # Writing the Validated transaction id into the output file
                outputfile.writelines(taxid+'\n')
                transactions_block.append(taxid)


parse_mempool_csv()
lines = len(transactions_block)
print(f'Parsed {lines} lines')
outputfile.close()
