def getStringList():
    list = []
    file = open('paper.txt', 'r') #读取文件
    for line in file:
        list.append(line) #写入列表
    file.close()

    f = open('result.txt', 'a') # 追加到文件末尾
    sl = sorted(list) #排序
    for i in range(len(list)):
        f.writelines(sl[i]) # 将排序好的文本写入另外一个文件
    f.close()

getStringList()
