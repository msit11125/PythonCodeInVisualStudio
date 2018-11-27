from flask import Flask, request, abort
from FlaskWebProject1 import app
import json

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

line_bot_api = LineBotApi('Your Access Token')
handler = WebhookHandler('Your Secrect')

# WebHook 接收
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

   
# 回傳訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    respMsg = event.message.text + "是也"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=respMsg))



# 測試
@app.route("/test", methods=['GET'])
def test():
    data =  { 'b' : 789 , 'c' : 456 , 'a' : 123 }
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response