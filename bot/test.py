#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

from wxpy import *
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer


def train():
    chatbot = ChatBot("deepThought")  # 用于回复消息的机器人
    chatbot.set_trainer(ChatterBotCorpusTrainer)
    key = "I am good"
    print(chatbot.get_response(key).text)
    # chatbot.train([key, '我叫张小贝'])
    # chatbot.train([
    #     "How are you?",
    #     "I am good.",
    #     "That is good to hear.",
    #     "Thank you",
    #     "You are welcome.",
    # ])
    print(chatbot.get_response(key).text)
    # chatbot.train


    # def reply_message(msg):
    #     respmsg = ""
    #     if "爱谁" in msg:
    #         respmsg = "当然是潘小宝啦"  # 使用机器人进行自动回复
    #     else:
    #         respmsg = chatbot.get_response(msg.text).text  # 使用机器人进行自动回复
    #     print(respmsg)
    #     return respmsg


if __name__ == '__main__':
    train()
    pass
        # reply_message("@张小贝 你最爱谁")
