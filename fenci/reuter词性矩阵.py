# _*_coding:utf-8_*_
import os
import csv
import nltk
from bs4 import BeautifulSoup
from nltk.tokenize import WordPunctTokenizer


def read_path(path_name):
    for dir_item in os.listdir(path_name):
        # 从初始路径开始叠加，合并成可识别的操作路径
        full_path = os.path.abspath(os.path.join(path_name, dir_item))
        if os.path.isdir(full_path):  # 如果是文件夹，继续递归调用
            read_path(full_path)
        else:  # 文件
            if dir_item.endswith(".sgm"):
                print(full_path)
                with open(full_path, 'r', encoding="latin-1") as f:
                    line = f.readline()
                    while line:
                        rowlist = []
                        if len(line) > 0:
                            soup = BeautifulSoup(line, 'html.parser')
                            fencilist = WordPunctTokenizer().tokenize(soup.get_text())
                            for word in fencilist:
                                word = word.translate(trans)
                                word.replace(" ","")
                                if word != "":
                                    word = word.lower()
                                    rowlist.append(word)
                            if len(rowlist) > 0:
                                doclist.append(rowlist)
                                # print(rowlist)
                        line = f.readline()
    return 0


def op_file(fi_path,list):
    with open(fi_path, 'r') as f:
        line = f.readline()
        while line:
            cutlist = line.split("\t")
            cutlist[0] = cutlist[0].translate(trans)
            if cutlist[0] != "":
                list.append(cutlist[0])
            line = f.readline()
        # print(list)
    return list


if __name__ == '__main__':
    trans = str.maketrans('', '',
                          '`~#&{}/";:-\<>@\[].+!_,$%^*()"\'?]=+|·（）-{}【】：；“”‘’《》[+——！，。？、~@#￥%……&*]+1234567890')
    readlist = []
    readlist = op_file("E:\\项目开发\\词性数据集\\词性对照表.txt",readlist)

    termlist = []
    termlist = op_file("E:\\项目开发\\词性数据集\\Reuters-21578.txt", termlist)
    # termlist = op_file("C:\\Users\\Administrator\\Desktop\\词性\\测试.txt", termlist)
    termsize = len(termlist)
    # print(termlist)

    doclist = []
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    read_path(r"E:\项目开发\词性数据集\Reuters-21578")
    # read_path(r"C:\Users\Administrator\Desktop\图片")
    # read_path(r"C:\Users\Administrator\Desktop\测试")

    termcount = 0
    savelist = []
    for aimterm in termlist:
        termcount += 1
        print("该文档共有{}个词，开始处理第{}个词。".format(str(termsize),str(termcount)))
        samelist = []
        samelist.append(aimterm)
        for k in range(0,36):
            samelist.append("0")
        for list in doclist:
            # 句子中第几个词
            i = 0
            for word in list:
                if word == aimterm:
                    pos_result = nltk.pos_tag(list)
                    sameword_cixing = pos_result[i][1]
                    k = 0
                    for cixing in readlist:
                        k += 1
                        if sameword_cixing == cixing:
                            # print("---词性---"+word+"的词性是"+cixing)
                            j = eval(samelist[k])
                            j += 1
                            samelist[k] = str(j)
                i += 1
        savelist.append(samelist)


    # with open('E:\\项目开发\\词性数据集\\all_result\\b.csv', 'w', newline='') as csv_file:
    with open('E:\\项目开发\\词性数据集\\all_result\\Reuters-21578.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, dialect='excel')
        writer.writerow([" "] + readlist)
        for row in savelist:
            writer.writerow(row)