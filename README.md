# 社交媒体数据预处理
* 文本分词
* 词性分析
* 聚类分析，进行情感标签处理

## 文本分词
本项目为社交媒体评论数据情感分析的预处理模块，在数据搜集环节中[数据爬虫](https://github.com/qiujun4417/social-media-data-extracter)，做了一些基础的数据清洗，比如把收集到的数据中的性别类型转换成0 女 1 男这样的数据类型，并且对于搜集到的文本数据进行了初步的清洗，比如去除标点符号以及特殊字符，表情等，但是这样的数据对于机器学习来说仍然还是非常高维的数据，所以首先我们需要进行分词和去除停用，对于中文文本，分词的目的是将连续的中文文本切分成一个个有意义的词语。通过分词，我们可以将文本转化为更小的语义单元，有助于进一步的语义分析和特征提取。分词后的词语能够帮助我们更好地理解文本中的信息，抓取关键信息，并更精确地进行后续的文本分析任务。它为我们提供了一种将复杂的文本数据转化为可处理的单元的方式。而去除停用词的目的是减少对分析无帮助的常用词的影响。停用词是指在文本分析中没有实际含义和词语权重较低的常见词语，如“的”、“是”、“我”等。这些停用词在分析过程中可能引入噪声，并对分析结果产生负面影响。通过去除停用词，我们可以减少分析的干扰和噪声，提高结果的准确性。同时，去除停用词还可以提高分析的效率，因为这些常用词语出现频率较高，但对分析任务的贡献较低。因此，去除停用词可以减少分析的计算量，提高分析的效率和性能。在本文中我将使用使用开源的中文分词工具，如jieba（结巴分词）库进行分词处理。

## 词性分析、标注

## 聚类分析