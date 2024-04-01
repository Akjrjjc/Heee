from telebot import TeleBot

bot=TeleBot("yourAPIBOT")

@bot.message_handler()
def delete(msg):
  bot.delete_message(msg.chat.id,msg.id)

bot.polling()
