# import telebot
#
# bot = telebot.TeleBot("971546843:AAERjgQEMuzu8jQhTlfY5TheTzFmqgLyCJU")
#
# @bot.message_handler(content_types=['text'])
# def send_echo(message):
# 	bot.reply_to(message, message.text)
#
# # @bot.message_handler(func=lambda message: True)
# # def echo_all(message):
# # 	bot.reply_to(message, message.text)
#
# bot.polling( none_stop=True)

# test-bot.py
from datetime import datetime, timezone

from simpletelegrambot import telegrambot


def on_message_receive(bot, message):
	utc_time = datetime.utcnow()
	msg_time = utc_time.strftime('%Y-%m-%d %H:%M:%S (UTC)')
	msg_text = message['text']

	print(msg_time, msg_text)

	if msg_text == 'Ping':
		bot.send_message('Pong')


def main():
	bot = telegrambot.TelegramBot('<bot-token>')
	bot.set_message_handler(on_message_receive)
	bot.wait_for_messages()


if __name__ == '__main__':
	main()