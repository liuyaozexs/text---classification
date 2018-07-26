import jieba.posseg as pseg
words = pseg.cut("我是一只小喵")
d = {}
for word, flag in words:
    d[word] = flag
with open("chulihou.txt", "w") as f:
    f.write(str(d))
