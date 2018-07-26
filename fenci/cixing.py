# -*- coding:utf-8 -*-
import jieba
import jieba.posseg as pseg
import gensim


if __name__=='__main__':

    # step 1 读取停用词
    stop_words = []
    with open('中文停用词库.txt',encoding= 'utf-8') as f:
        line = f.readline()
        while line:
            stop_words.append(line[:-1])
            line = f.readline()
    stop_words = set(stop_words)
    print('停用词读取完毕，共{n}个单词'.format(n=len(stop_words)))

    # step2 读取文本，预处理，分词，得到词典
    d = {}
    sentence_list = []
    with open('数据1.txt',encoding='gb18030') as f:
        line = f.readline()
        while line:
            while '\n' in line:
                line = line.replace('\n',' ')
            while ' ' in line:
                line = line.replace(' ','')
            if len(line)>0: # 如果句子非空
                raw_word = list(jieba.cut(line, cut_all=False))
                raw_words = pseg.cut(line)
                for word, flag in raw_words:
                    d[word] = flag
                dealed_words = []
                for word in raw_word:
                    if word not in stop_words and word not in ['www','com','http']:
                        dealed_words.append(word)
                sentence_list.append(dealed_words)
            line = f.readline()
    with open("d.txt", "a") as f:
        f.write(str(d))
    with open("chulihou.txt", "a") as f:
        f.write(str(sentence_list))
    model = gensim.models.Word2Vec(sentence_list, min_count=1,workers=4)
    model.save('word2model')
    print("测试扶贫和救灾两个词的相似度")
    print(model.similarity('扶贫', '救灾'))
    print("它们的词性是")
    print(d['扶贫'],d['救灾'])



