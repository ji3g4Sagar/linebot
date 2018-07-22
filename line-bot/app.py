from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from botObject import chatbot
#from chatterbot import ChatBot
#from chatterbot.trainers import ListTrainer

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('aAT6S1Z0aA7Ggdosk7H2hFNVowwx08cBwU5pB6igStLHAZsld07mBEfo1QmEsDzQKF1dzStSkxCRTnmorXDaWb2gF2k3WFcuHMsUPdjSF5sNtaVkijdcRkYIMDeTVrCJmXqSp/5EPqd5RGshVdRXngdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('2549c451cbf3b4e6f96e081d6f627bc9')



# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    kkchatbot = chatbot()
    #response = TextSendMessage(text=event.message.text)  
    response = TextSendMessage(text=kkchatbot.chat_bot_response(event.message.text))
    line_bot_api.reply_message(event.reply_token, response)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
