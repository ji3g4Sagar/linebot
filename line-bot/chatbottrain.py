# 引入 ChatBot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import json

# 建立一個 ChatBot 物件
chatbot = ChatBot(
    'sagar',
    database = './talk.json'
)


def getOntLyric(filename):
    with open('lyrics_list/'+ filename, 'r', encoding="utf8") as f:
        data = json.load(f)
    return data

conversation = [
"hey there", "hi",
"今天是陰天","不會曬傷的天氣",
"今天是晴天","天氣真好",
"今天是雨天","適合一些室內的活動",
"涼爽的天氣","適合出去走一走",
"工作很忙","忙碌之餘可以放鬆一下",
"閒閒沒事做","哈哈可以找人出去晃晃",
"今天放假", "放假真好呢!",
"你好", "你好啊~今天怎麼樣呢?",
"天氣如何啊", "今天天氣很舒服呢"
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

path = "./lyrics_list" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称

for filename in files:
    trainArray = getOntLyric(filename)
    print(trainArray)
    chatbot.train(trainArray)