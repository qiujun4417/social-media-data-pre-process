import pymongo

class MongodbCorpusReader(object):

    def __init__(self, url='localhost', collection='corpus'):
        self.client = pymongo.MongoClient(url)
        self._db = self.client['mydatabase']
        self._collection = self._db[collection]

    def __iter__(self, fields_to_iterate):
        for item in self._collection.find():
            yield {field: item[field] for field in fields_to_iterate}

    def getCollection(self):
        return self._collection

    