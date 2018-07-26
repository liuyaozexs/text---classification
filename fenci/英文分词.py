import nltk
from nltk.tokenize import WordPunctTokenizer
from nltk.stem import SnowballStemmer


flist = []
# 词干化还原
stemmer = SnowballStemmer("english")  # Choose a language
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# 将一段文本分割成句子
f = open("delete_html.txt").read()
# 停用词
stopwords = nltk.corpus.stopwords.words('english')
# 小写
f = f.lower()
sentences = tokenizer.tokenize(f)
words = []
# 将每个句子分词，词汇集合加入到列表中
for sentence in sentences:
    fword = []
    words = WordPunctTokenizer().tokenize(sentence)
    print(words)
    for word in words:
        if word not in stopwords:
            word = stemmer.stem(word)
            fword.append(word)
    print("---------")
    print(fword)
    flist.append(fword)
with open("fencihou.txt", "w") as nf:
    nf.write(str(flist))