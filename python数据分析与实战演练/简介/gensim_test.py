import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#logging 用来打印日志

#分好次的句子，每个句子以词列表的形式输入

sentence = [['first', 'sentence'],['second', 'content']]

#用以上句子训练词模型
model = gensim.models.Word2Vec(sentence, min_count=1)

print(model['sentence']) #输出单词sentence的词向量