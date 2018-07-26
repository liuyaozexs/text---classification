# # ctrl y 是清除当前光标行
# # ctrl d 是将当前行代码快捷复制粘贴到下一行
# # ctrl g 是go to 到代码的哪行中
# # ctrl r 是替换单词键
# # ctrl m 移动到当前光标位置
# # ctrl / 快捷注释选中行（可多行）
#
# a=[]
# aimterm = "meeting"
# i = 0
# fencilist = ['She', 'moved', 'to', 'London', '', 'meeting', 'some', 'of', 'the', 'best', 'minds', 'of', 'her', 'time', '']
# for word in fencilist:
#     print(word + "你给我出来")
#     if word != "":
#         print(i)
#         print(fencilist[i])
#         a.append(word)
#         word = word.lower()
#         if word == aimterm:
#             print("---" + aimterm + "成功找到")
#         i += 1
# print()
# # ctrl y 是清除当前光标行
# # ctrl d 是将当前行代码快捷复制粘贴到下一行
# # ctrl g 是go to 到代码的哪行中
# # ctrl r 是替换单词键
# # ctrl m 移动到当前光标位置
# # ctrl / 快捷注释选中行（可多行）

# import os
# import nltk
# from nltk.tokenize import WordPunctTokenizer
#
#
# def read_path(path_name):
#     for dir_item in os.listdir(path_name):
#         # 从初始路径开始叠加，合并成可识别的操作路径
#         full_path = os.path.abspath(os.path.join(path_name, dir_item))
#         if os.path.isdir(full_path):  # 如果是文件夹，继续递归调用
#             read_path(full_path)
#         else:  # 文件
#             if dir_item:
#                 print(full_path)
#                 with open(full_path, 'r', encoding="latin-1") as f:
#                     line = f.readline()
#                     line = f.readline()
#                     while line:
#                         rowlist = []
#                         if len(line) > 0:
#                             line = line.replace(".", " ")
#                             line = line.replace("\n", " ")
#                             fencilist = line.split(" ")
#                             for word in fencilist:
#                                 word.replace(" ","")
#                                 if word != "" and not word.isdigit():
#                                     word = word.translate(trans)
#                                     word = word.lower()
#                                     rowlist.append(word)
#                             if len(rowlist) > 0:
#                                 doclist.append(rowlist)
#                         line = f.readline()
#     return 0
#
#
# def op_file(fi_path,list):
#     with open(fi_path, 'r') as f:
#         line = f.readline()
#         while line:
#             cutlist = line.split("\t")
#             list.append(cutlist[0])
#             line = f.readline()
#         print(list)
#     return list
#
#
# if __name__ == '__main__':
#
#     termlist = []
#     termlist = op_file("E:\\项目开发\\词性数据集\\ceshi.txt", termlist)
#     termsize = len(termlist)
#
#     doclist = []
#     trans = str.maketrans('', '',
#                           '`~#&{}/";:\<>@\[]+!_,$%^*()"?]=+|·（）{}【】：；“”‘’《》[+——！，。？、~@#￥%……&*]+')
#     read_path(r"E:\项目开发\词性数据集\20_newsgroups_18846")
#     print(doclist)
#
#     termcount = 0
#     for aimterm in termlist:
#         termcount += 1
#         print("该文档共有{}个词，开始处理第{}个词。".format(str(termsize),str(termcount)))
#         out_time = 0
#         for rowlist in doclist:
#             for word in rowlist:
#                 if aimterm == word:
#                     out_time += 1
#         print("{} ----- {}".format(aimterm,str(out_time)))


#判断一个词是否是数字
# a = []
# fencilist = []
# line = "he is a 2 bad boy3 334"
# fencilist = line.split(" ")
# for word in fencilist:
#     if not word.isdigit():
#         a.append(word)
# print(a)


#判断一个独立单词的词性
from nltk.corpus import wordnet as wn
#这种识别不了的词标为名词
c = wn.synsets("net")
print(c)
print(wn.synset('one.s.01').definition())
# print(wn.synset('like.n.02').name())
# d = wn.synset('like.n.01').name()
# f = d.split(".")
# print(f[0])
# print(f[1])
#
# list= wn.synsets('fly')
# print(type(list))
# print(list[0])
#
# a = "wn." + str(list[0]).lower() + ".pos()"
# a = eval(a)
# print(a)
# print(list[1])
#
# b = "wn." + str(list[1]).lower() + ".pos()"
# b = eval(b)
# print(b)
# print(wn.synsets('car'))
# print(wn.synsets('fly'))

