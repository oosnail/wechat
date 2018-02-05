#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

from wxpy import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

chatbot = ChatBot("deepThought")
chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("chatterbot.wcorpus.chinese")  # 使用该库的中文语料库
chatbot.set_trainer(ListTrainer)

bot = Bot()  # 用于接入微信的机器人
friend = bot.friends().search('琛')[0]
friends = bot.friends()
group = bot.groups("群") # 进行测试的群


@bot.register(friends)
def reply_my_friend(msg):
    print(msg)
    return reply_message(msg.text)  # 使用机器人进行自动回复


@bot.register(group)
def reply_my_friend(msg):
    print(msg)
    if "@张小贝" in msg.text:
        return reply_message(msg.text)  # 使用机器人进行自动回复
    return ""


def reply_message(msg):
    respmsg = chatbot.get_response(msg)  # 使用机器人进行自动回复
    print(chatbot.get_response(msg))
    return respmsg.text


def train(question, answer):
    print("old： " + chatbot.get_response(question).text)
    chatbot.train([question, answer])
    print("new： " + chatbot.get_response(question).text)

# 堵塞线程，并进入 Python 命令行
embed()
