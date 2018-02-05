#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

from wxpy import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer


class xiaobei:
    def __init__(self):
        self.chatbot = ChatBot("deepThought")
        self.chatbot.set_trainer(ChatterBotCorpusTrainer)
        self.chatbot.train("chatterbot.wcorpus.chinese")  # 使用该库的中文语料库
        self.chatbot.set_trainer(ListTrainer)

        # bot = Bot()  # 用于接入微信的机器人
        # self.friend = self.bot.friends().search('张小贝')[0]
        self.friends = self.bot.friends()
        self.group = self.bot.groups("群")  # 进行测试的群

    # @self.bot.register(self.group)
    def reply_my_friend(self, msg):
        print(msg)
        if "@张小贝" in msg.text:
            return self.reply_message(msg.text)  # 使用机器人进行自动回复
        return ""

    def reply_message(self, msg):
        flag = "学习"
        if msg.find(flag) == 0:
            return self.learn_response(msg)
        respmsg = self.chatbot.get_response(msg)  # 使用机器人进行自动回复
        print(self.chatbot.get_response(msg))
        return respmsg.text

    def learn_response(self, msg):
        arr = msg.split("&")
        if len(arr) == 3:
            question = arr[1]
            answer = arr[2]
            self.train(question, answer)
            return "好的，我学习了"
        else:
            return "我学习不聊。格式不对。格式类似于 学习&你吃饭了吗&吃了"

    def train(self, question, answer):
        self.chatbot.train([question, answer])


bot = Bot()
friend = bot.friends().search('张小贝')[0]
xiaobei = xiaobei()


@bot.register(friend)
def reply_my_friend(msg):
    print(msg)
    return xiaobei.reply_message(msg.text)  # 使用机器人进行自动回复


if __name__ == '__main__':
    embed()
