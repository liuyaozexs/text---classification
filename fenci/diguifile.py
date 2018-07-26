import os
import nltk
from nltk.stem import SnowballStemmer
from bs4 import BeautifulSoup
from nltk.tokenize import WordPunctTokenizer
import gensim


def read_path(path_name):


    for dir_item in os.listdir(path_name):
        # 从初始路径开始叠加，合并成可识别的操作路径
        full_path = os.path.abspath(os.path.join(path_name, dir_item))
        if os.path.isdir(full_path):  # 如果是文件夹，继续递归调用
            read_path(full_path)
        else:  # 文件
            if dir_item.endswith('.txt'):
                print(full_path)
                print(type(full_path))
                fencilist = []
                with open(full_path, 'r', errors="ignore") as f:
                    line = f.readline()
                    while line:
                        if len(line) > 0:
                            trans = str.maketrans('', '', ':-<>@[]->.+!_,$%^*()"\'?]+|[+——！，。？、~@#￥%……&*]+1234567890')
                            soup = BeautifulSoup(line, 'html.parser')
                            print(soup.get_text())
                            fencilist = WordPunctTokenizer().tokenize(soup.get_text())
                            wordlist = []
                            for word in fencilist:
                                if word not in stopwords:
                                    # 去标点
                                    word = word.translate(trans)
                                    if len(word) > 0:
                                        word = stemmer.stem(word)
                                        wordlist.append(word)
                                    print(word)
                            if len(wordlist) > 0:
                                finalist.append(wordlist)
                        line = f.readline()

    return finalist


if __name__ == '__main__':
    cixingmap = {}
    finalist = []
    dateprocess = []
    trans = str.maketrans('', '',
                          '/"/n":-<>@[]-.+!_,$%^*()"\'?]+|[+——！，。？、~@#￥%……&*]+1234567890')
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    # 词干化还原
    stemmer = SnowballStemmer("english")  # Choose a language
    # 停用词
    stopwords = nltk.corpus.stopwords.words('english')
    dateprocess = read_path(r"C:\Users\Administrator\Desktop\txtchuli")
    model = gensim.models.Word2Vec(dateprocess, min_count=1,workers=4)
    model.save('word2modelEN')
    print("测试两个词的相似度:")
    print(model.similarity('said', 'saw'))

