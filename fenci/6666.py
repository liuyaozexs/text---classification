# coding:utf-8
import nltk
from nltk.stem import SnowballStemmer
from bs4 import BeautifulSoup
from nltk.tokenize import WordPunctTokenizer


fintext = ''
fencilist = []
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# 词干化还原
stemmer = SnowballStemmer("english")  # Choose a language
# 停用词
stopwords = nltk.corpus.stopwords.words('english')
with open('c12 (2).txt', 'r',errors="ignore") as f:
    line = f.readline()
    while line:
        i = "1"
        if len(line) > 0:
            trans = str.maketrans('', '', '/"/n":->>@[]->.+!_,$%^*()"\'?]+|[+——！，。？、~@#￥%……&*]+1234567890')
            soup = BeautifulSoup(line, 'html.parser')
            print(soup.get_text())
            fencilist = WordPunctTokenizer().tokenize(soup.get_text())
            for word in fencilist:

                word = word.replace(" ", "")
                if word not in stopwords:
                    # 去标点
                    word = word.translate(trans)
                    if len(word) > 0:
                        word.lower()
                        word = stemmer.stem(word)
                        fintext = fintext + word + ' '
                        print("啥"+word)
                        i= "0"
        if i == "0":
            fintext = fintext[:-1] + "/n"
        line = f.readline()

with open("try.txt", "w") as finf:
    finf.write(fintext)

