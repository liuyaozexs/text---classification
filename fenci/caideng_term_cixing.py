# _*_coding:utf-8_*_
import csv
import nltk
from nltk.corpus import wordnet as wn


#num 是3种不同的分词的方式
def op_file(fi_path,list,num):
    with open(fi_path, 'r') as f:
        line = f.readline()
        if num == 1:
            while line:
                cutlist = line.split("\t")
                list.append(cutlist[0])
                line = f.readline()
        if num == 2:
            while line:
                cutlist = line.split(" ")
                list.append(cutlist[0])
                line = f.readline()
        if num == 3:
            while line:
                cutlist = line.split("\n")
                list.append(cutlist[0])
                line = f.readline()
        # print(list)
    return list


if __name__ == '__main__':
    readlist = []
    readlist = op_file("E:\\项目开发\\词性数据集\\词性net表.txt", readlist, 2)

    termlist = []
    # termlist = op_file("E:\\项目开发\\词性数据集\\20news-19997(1).txt", termlist, 3)
    # termlist = op_file("E:\\项目开发\\词性数据集\\20news-19997(2).txt", termlist, 1)
    # termlist = op_file("E:\\项目开发\\词性数据集\\Reuters-21578.txt", termlist, 1)
    # termlist = op_file("E:\\项目开发\\词性数据集\\TDT2.txt", termlist, 1)
    termlist = op_file("E:\\项目开发\\词性数据集\\20news-18846.txt", termlist, 1)

    # termlist = op_file("C:\\Users\\Administrator\\Desktop\\词性\\测试.txt", termlist, 1)
    termsize = len(termlist)

    termcount = 0
    savelist = []
    for aimterm in termlist:
        termcount += 1
        print("该文档共有{}个词，开始处理第{}个词。".format(str(termsize),str(termcount)))
        row_list = []
        row_list.append(aimterm)
        for k in range(0,4):
            row_list.append("0")
        #list为同义词表
        list = wn.synsets(aimterm)
        # print(list)
        for cixing in list:
            single_syn = "wn." + str(cixing).lower() + ".name()"
            print(single_syn)
            try:
                single_syn_list = eval(single_syn).split(".")
            except:
                continue
            else:
                # print(single_syn_list)
                if single_syn_list[0] == aimterm:
                    i = 0
                    for term in readlist:
                        i += 1
                        if single_syn_list[1] == term:
                            # print("---词性---"+aimterm+"的词性是"+term)
                            row_list[i] = "1"
        savelist.append(row_list)



    # with open('E:\\项目开发\\词性数据集\\cai_result\\20news-19997(1).csv', 'w', newline='') as csv_file:
    # with open('E:\\项目开发\\词性数据集\\cai_result\\20news-19997(2).csv', 'w', newline='') as csv_file:
    # with open('E:\\项目开发\\词性数据集\\cai_result\\Reuters-21578.csv', 'w', newline='') as csv_file:
    # with open('E:\\项目开发\\词性数据集\\cai_result\\TDT2.csv', 'w', newline='') as csv_file:
    with open('E:\\项目开发\\词性数据集\\cai_result\\20news-18846.csv', 'w', newline='') as csv_file:
    # with open('E:\\项目开发\\词性数据集\\all_result\\20_newsgroups_19997(1).csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, dialect='excel')
        writer.writerow([" "] + readlist)
        for row in savelist:
            writer.writerow(row)