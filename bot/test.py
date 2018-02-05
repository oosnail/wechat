#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

from wxpy import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer

chatbot = ChatBot("deepThought")
chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("chatterbot.wcorpus.chinese")  # 使用该库的中文语料库
chatbot.set_trainer(ListTrainer)

def train(question, answer):
    print("old： " + chatbot.get_response(question).text)
    chatbot.train([question, answer])
    print("new： " + chatbot.get_response(question).text)


if __name__ == '__main__':
    train("吃了吗", "吃的汉堡王")
    embed()
