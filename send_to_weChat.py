#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import sys
import os
import json
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s, %(filename)s, %(levelname)s, %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=os.path.join('/tmp', 'weixin.log'),
                    filemode='a')

corpid = 'ww4024acaa94419893'
appsecret = 'jloaixVbGfDNNMcZ6i9xIhqVnmJJ59lqTtb8Q2o5OeY'
agentid = '1000002'

# 获取accesstoken
token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid + '&corpsecret=' + appsecret
req = requests.get(token_url)
accesstoken = req.json()['access_token']

# 发送消息
msgsend_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + accesstoken
touser = sys.argv[1]
subject = sys.argv[2]
message = sys.argv[2] + "\n\n" + sys.argv[3]
params = {
    "touser": touser,
    "msgtype": "text",
    "agentid": agentid,
    "text": {
        "content": message
    },
    "safe": 0
}

req = requests.post(msgsend_url, data=json.dumps(params))
logging.info('sendto:' + touser + ';;subject:' + subject + ';;message:' + message)
