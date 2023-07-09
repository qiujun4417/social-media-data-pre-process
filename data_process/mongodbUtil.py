# from pymongo import MongoClien
from bson.objectid import ObjectId

class MongodbUtil(object):

    def replace_data(self, collection, document_id, values):
        query = {'_id': ObjectId(document_id)}
        new_value = {'$set': {values['field']: values['value']}}
        collection.update_one(query, new_value)