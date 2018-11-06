import itchat

@itchat.msg_register(itchat.content.TEXT)
def reply_msg(msg):
    print(msg['Content'])
    print(msg['FromUserName'])
    itchat.send_msg(msg['User']['NickName'] + "你好啊！", msg['FromUserName'])

if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.run()