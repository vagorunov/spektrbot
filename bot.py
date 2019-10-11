import telebot
bot = telebot.TeleBot("971546843:AAERjgQEMuzu8jQhTlfY5TheTzFmqgLyCJU")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	bot.reply_to(message, message.text)
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)
bot.polling( none_stop=True)

