#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

from wxpy import *
from chatterbot import ChatBot, logic
from chatterbot.logic import logic_adapter
from chatterbot.trainers import ChatterBotCorpusTrainer

# 训练地址 /Users/ztcq/Desktop/wechat/env/lib/python3.6/site-packages/chatterbot_corpus/data/chinese/trivia.yml
logic_adapters = ['chatterbot.logic.LogicAdapter',
                  'chatterbot.logic.BestMatch',
                  'chatterbot.logic.MathematicalEvaluation',
                  'chatterbot.logic.NoKnowledgeAdapter',
                  'chatterbot.logic.TimeLogicAdapter']
chatbot = ChatBot("deepThought",
                  # logic_adapters=logic_adapters,
                  input_adapter='chatterbot.input.VariableInputTypeAdapter',
                  output_adapter='chatterbot.output.OutputAdapter')  # 用于回复消息的机器人
chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("chatterbot.wcorpus.chinese")  # 使用该库的中文语料库

bot = Bot(cache_path=True)  # 用于接入微信的机器人
group_1 = bot.groups("群")[0]  # 进行测试的群
friend1 = bot.friends("琛")[6]
friend2 = bot.friends("倩玉")[1]


@bot.register(friend1)
def reply_my_friend(msg):
    print(msg)
    return reply_message(msg.text)  # 使用机器人进行自动回复


@bot.register(friend2)
def reply_my_friend(msg):
    print(msg)
    return reply_message(msg.text)  # 使用机器人进行自动回复


@bot.register(group_1)
def reply_my_friend(msg):
    print(msg)
    if "@张小贝" in msg.text:
        return reply_message(msg.text)  # 使用机器人进行自动回复
    return ""


def reply_message(msg):
    respmsg = chatbot.get_response(msg)  # 使用机器人进行自动回复
    print(chatbot.get_response(msg))
    return respmsg.text


# 堵塞线程，并进入 Python 命令行
embed()
