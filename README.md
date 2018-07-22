# linebot

將Linebot物件化，from botObject import chatbot引用物件
在將物件實體化(Ex: bot = cahtbot() )，即可呼叫回應用的函式（chat_bot_response(str) )，會根據訓練模型中的語句回傳有關的語句。

在chatbottrain.py中，簡單的列了幾個能夠回應使用者的對話，以及兩首歌曲的歌詞作為訓練資料，執行後會產生出一個talk.json作為機器人的語料庫

而機器人的server是使用heroku，在資料夾有個heroku的目錄，引用了網路上的教學
