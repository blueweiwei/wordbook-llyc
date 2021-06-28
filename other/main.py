import json
import sys
def readData():
    result=[]
    with open("word.txt",'r') as f:
        for line in f:
            result.append(list(line.strip('\n').split(',')))
    return result

def saveData(num, content, encode='utf-8'):
    file="../chapter/chapter{}.yaml".format(num)
    with open(file, 'a+', encoding=encode) as f:
        f.write(content+"\n")



data=readData()
# print(data)
for i in range(1,31):
    word="#Unit {}".format(i)
    num=0
    status=False
    for getWord in data:
        if getWord[0][:5]=="#Unit":
            if getWord[0] == word :
                status=True
                num=i
                content="""slug: chapter{}
title: "第{}单元-词汇"
summary: ""
words:""".format(i,i)
                saveData(num,content)
            else:
                status=False
        if status:
            if getWord[0][:5]=="#Unit":
                pass
            else:
                content="  - word: {}".format(getWord[0])
                saveData(num,content)


        # if getWord[0] == word :
        #     num=i
        # else:
        #     file="../chapters/chapter{}.yaml".format(num)
        #     content="  - word: {}".format(getWord[0])
        #     saveData(file,content)