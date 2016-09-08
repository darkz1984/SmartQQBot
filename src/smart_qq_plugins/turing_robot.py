# coding: utf-8
from random import randint
import requests

from smart_qq_bot.signals import on_all_message

# 使用前请先前往 http://www.tuling123.com/register/index.jhtml
# 申请 API key 谢谢
# 另外需要 requests 支持
# by darkz
# 2016-09-08 18:59:54
# 修改成调用图灵官方接口
url = 'http://www.tuling123.com/openapi/api'
apikey = ''

@on_all_message
def turing_robot(msg, bot):
    """
    :type bot: smart_qq_bot.bot.QQBot
    :type msg: smart_qq_bot.messages.QMessage
    """

    querystring = {
        "key": "",
        "info": msg.content,
        "userid": ""
    }
    request_url = ("%s?key=%s&info=%s")%(url, apikey, msg.content)
    response = requests.request("GET", request_url)

    response_json = response.json()
    bot.reply_msg(msg, response_json.get('text'))
