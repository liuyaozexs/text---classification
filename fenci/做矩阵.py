import nltk
import csv

cutlist = []
readlist = []
savelist = []
cixinglist = []
with open("C:\\Users\\Administrator\\Desktop\\词性\\词性对照表.txt", 'r') as f:
    line = f.readline()
    while line:
        cutlist = line.split("\t")
        readlist.append(cutlist[0])
        line = f.readline()
    print(readlist)
with open("C:\\Users\\Administrator\\Desktop\\词性\\测试.txt", 'r') as f:
    line = f.readline()
    while line:
        savelist = []
        cutlist = line.split("\t")
        savelist.append(cutlist[0])
        pos_result = nltk.pos_tag(cutlist[0])
        print(pos_result[0][1])
        pt = pos_result[0][1]
        for word in readlist:
            if pt == word:
                print("1")
                savelist.append("1")
            else:
                print("0")
                savelist.append("0")
        cixinglist.append(savelist)
        line = f.readline()
with open('C:\\Users\\Administrator\\Desktop\\词性\\词性结果.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, dialect='excel')
    writer.writerow([" "]+readlist)
    for row in cixinglist:
        writer.writerow(row)


