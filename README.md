# linebot

### 機器人訓練部分
直接呼叫chatbottrain.py就可以將裡面簡易的對話資料以及歌詞資料輸出成機器人能夠使用的語料庫。

在chatbottrain.py中，簡單的列了幾個能夠回應使用者的對話，以及兩首歌曲的歌詞作為訓練資料，執行後會產生出一個talk.json作為機器人的語料庫

### 機器人實作部分
將Linebot物件化，透過from botObject import chatbot引用物ｅｘ
再將物件實體化，即可呼叫回應用的函式，會根據訓練模型中的語句回傳有關的語句。

Ex: 
bot = chatbot();
message //假設為取得的使用者輸入型態為str　
bot.chat_bot_response(message) //根據使用者輸入，取得回應

而機器人的server是使用heroku，在資料夾有個heroku的目錄，引用了網路上的教學，可以參考
