import nltk
from nltk.stem import SnowballStemmer
from bs4 import BeautifulSoup
from nltk.tokenize import WordPunctTokenizer
import string


fencilist = []
finalist = []
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# 词干化还原
stemmer = SnowballStemmer("english")  # Choose a language
# 停用词
stopwords = nltk.corpus.stopwords.words('english')
with open('c12 (1).txt' 'r',errors="ignore") as f:
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

with open("cicingyuchuli.txt", "w") as finf:
    finf.write(str(finalist))

