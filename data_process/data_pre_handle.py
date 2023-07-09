import jieba
import logging
from mongo_corpus_reader import MongodbCorpusReader
from mongodbUtil import MongodbUtil


def remove_pre_fix_for_source_field():
    reader = MongodbCorpusReader('mongodb://nick_2014:nick_2088_21@localhost:32774/?authMechanism=DEFAULT', 'users')
    result = reader.__iter__(['_id', 'source'])
    process_count = 0
    for field_dict in result:
        field_id = field_dict['_id']
        field_source = field_dict['source']
        if field_source:
            field_source = field_source.replace('来自', '')
            value_fields = {'field': 'source', 'value': field_source}
            mongodbUtil = MongodbUtil()
            mongodbUtil.replace_data(reader.getCollection(), field_id, value_fields)
            process_count += 1
    return process_count

def main():
    # 先把user表中的source字段的前缀去掉 如来自上海 变为上海
    processed_count = remove_pre_fix_for_source_field()
    logging.info("processed_count: %d", processed_count)
    # 把comment collection中的content里面的内容删除‘回复‘两个字
    # 对content进行分词、词性标记
    # 对文本内容进行聚类

if __name__ == '__main__':
    main()
    logging.info("process done")
            
