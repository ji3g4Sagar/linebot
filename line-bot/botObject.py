# 引入 ChatBot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# 建立一個 ChatBot 物件

class chatbot():

    def __init__(self):
        self.chatbot = ChatBot('Ron Obvious', database = './talk.json', read_only = True)

    def chat_bot_response(self, msg):
        response = self.chatbot.get_response(msg)
        return response.text

"""
print("歌詞接龍，ready go!")

for i in range(10):
    msg = input("請輸入：")
    response = chatbot.get_response(msg)
    print("> " + response.text)"""