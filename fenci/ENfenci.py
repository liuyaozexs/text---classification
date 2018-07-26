from nltk.tokenize import WordPunctTokenizer
from bs4 import BeautifulSoup
import nltk


alist = []
d = {}
fencilist = []
soup = BeautifulSoup("i like you", 'html.parser')
fencilist = WordPunctTokenizer().tokenize(soup.get_text())
for word,flag in nltk.pos_tag(fencilist):
    if flag == "NN":
        print(word)