import jieba
import logging
import nltk
from mongo_corpus_reader import MongodbCorpusReader
from mongodbUtil import MongodbUtil
from nltk.corpus import stopwords


def remove_pre_fix_for_source_field(field_filter, collection_name, prefix, target_field):
    reader = MongodbCorpusReader('mongodb://nick_2014:nick_2088_21@localhost:32774/?authMechanism=DEFAULT', collection_name)
    result = reader.__iter__(field_filter)
    process_count = 0
    for field_dict in result:
        field_id = field_dict['_id']
        field_content = field_dict['content']
        if field_content:
            field_content = field_content.replace(prefix, '')
            value_fields = {'field': target_field, 'value': field_content}
            mongodbUtil = MongodbUtil()
            mongodbUtil.replace_data(reader.getCollection(), field_id, value_fields)
            process_count += 1
    return process_count

def fenci_and_stop_words(collection_name):
    reader = MongodbCorpusReader('mongodb://nick_2014:nick_2088_21@localhost:32774/?authMechanism=DEFAULT', collection_name)
    result = reader.find_all()
    nltk.download('stopwords')
    stop_words = set(stopwords.words('chinese'))
    for item in result:
        content = item['content']
        # 分词
        seg_list = jieba.cut(content)

        # 去除停用词
        filtered_words = [word for word in seg_list if word not in stop_words]
        item['tokenized_content'] = filtered_words
        collection = reader.getCollection()
        collection.update_one({'_id': item['_id']}, {'$set': {'tokenized_content': filtered_words}}) 

def main():
    # 先把user表中的source字段的前缀去掉 如来自上海 变为上海
    users_processed_count = remove_pre_fix_for_source_field(['_id', 'source'], 'users', '来自', 'source')
    logging.info("users processed_count: %d", users_processed_count)
    # 把comment collection中的content里面的内容删除‘回复‘两个字
    comments_processed_count = remove_pre_fix_for_source_field(['_id', 'content'], 'comments', '回复', 'content')
    logging.info("comments processed_count: %d", comments_processed_count)
    # 对content进行分词、停词处理
    fenci_and_stop_words('comments')


if __name__ == '__main__':
    main()
    logging.info("process done")
            
