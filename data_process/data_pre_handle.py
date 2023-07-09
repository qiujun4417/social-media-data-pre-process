import jieba
from mongo_corpus_reader import MongodbCorpusReader
from mongodbUtil import MongodbUtil


def remove_pre_fix_for_source_field():
    reader = MongodbCorpusReader('mongodb://nick_2014:nick_2088_21@localhost:32774/?authMechanism=DEFAULT', 'user')
    result = reader.__iter__(['_id', 'source'])
    for field_dict in result:
        field_id = field_dict['_id']
        field_source = field_dict['source']
        process_count = 0
        if field_source:
            field_source = field_source.replace('来自', '')
            value_fields = {'field': 'source', 'value': field_source}
            mongodbUtil = MongodbUtil()
            mongodbUtil.replace_data(reader.getCollection(), field_id, value_fields)
            process_count += 1

# 先把user表中的source字段的前缀去掉 如来自上海 变为上海
remove_pre_fix_for_source_field()


            
