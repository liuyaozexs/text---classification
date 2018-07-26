# _*_coding:utf-8_*_
import os
import nltk
from nltk.stem import SnowballStemmer
from bs4 import BeautifulSoup
from nltk.tokenize import WordPunctTokenizer


def read_path(path_name):


    for dir_item in os.listdir(path_name):
        # 从初始路径开始叠加，合并成可识别的操作路径
        full_path = os.path.abspath(os.path.join(path_name, dir_item))
        if os.path.isdir(full_path):  # 如果是文件夹，继续递归调用
            read_path(full_path)
        else:  # 文件
            if dir_item:
                print(full_path)
                print(type(full_path))
                fintext = ''
                with open(full_path, 'r', encoding="latin-1") as f:
                    line = f.readline()
                    while line:
                        i = "1"
                        if len(line) > 0:
                            trans = str.maketrans("", "", '1234567890')
                            soup = BeautifulSoup(line, 'html.parser')
                            print(soup.get_text())
                            fencilist = WordPunctTokenizer().tokenize(soup.get_text())
                            for word in fencilist:

                                word = word.replace(" ", "")
                                if word:
                                    # 去标点
                                    word = word.translate(trans)
                                    if len(word) > 0:
                                        word = stemmer.stem(word)
                                        fintext = fintext + word + ' '
                                        print("啥" + word)
                                        i = "0"
                        line = f.readline()

                with open(full_path, "w",encoding='utf-8') as finf:
                    finf.write(fintext)
    return 0
if __name__ == '__main__':
    i = "0"
    trans = str.maketrans('', '',
                          '/"/n":-<>@[]->.+!_,$%^*()"\'?]+|[+——！，。？、~@#￥%……&*]+1234567890')
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    # 词干化还原
    stemmer = SnowballStemmer("english")  # Choose a language
    # 停用词
    stopwords = nltk.corpus.stopwords.words('english')

    read_path(r"E:\项目开发\zz")
