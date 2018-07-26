from bs4 import BeautifulSoup


chulilist = []
with open("C:\\Users\\Administrator\\Desktop\\测试\\reut2-000.sgm", 'r') as f:
    line = f.readline()
    while line:
        if len(line) > 0:
            soup = BeautifulSoup(line, 'html.parser')
            print(soup.get_text())
            chulilist.append(soup.get_text())
        line = f.readline()
with open("C:\\Users\\Administrator\\Desktop\\测试\\ceshireut2-000.txt", "w") as f:
    f.write(str(chulilist))