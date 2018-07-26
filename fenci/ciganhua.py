from nltk.stem import WordNetLemmatizer


wnl = WordNetLemmatizer()
ciganlist = []
with open("fencihou.txt") as f:
    line = f.readline()
    while line:
        if len(line) > 0:  # 如果句子非空
            for word in line:
                word = wnl.lemmatize(word)
