'''
DS.get(index) -> value
DS.set(index,value)
DS.setAll(value)

Alll operations O(1)
'''

DataItem = namedtuple("DataItem", ["value", "transaction_id"])

class JournalMap():
    def __init__(self):
        self.data = {}  # (key,value) store of DataItem
        self.journal, self.transaction_id  = [], 0

    def get(self, key):
        value, transaction_id = self.data[key]
        value = self.check_journal(transaction_id, value)
        # Always update the map
        self.data = value 

    def set(self, key, value):
        transaction_id = self.get_transaction_id()
        self.data[key] = DataItem(value, transaction_id)

    def setAll(self, vale):
        transaction_id = self.get_transaction_id()
        self.journal[0] = DataItem(value, transaction_id)

    def check_journal(transaction_id, value):
        if len(self.journal) and self.journal[0].transaction_id < transaction_id:
            return self.journal[0].value
        return value

    def get_transaction_id(self):
        self.transaction_id + 1
        return self.transaction_id
