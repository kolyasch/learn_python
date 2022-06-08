import telebot

bot = telebot.TeleBot('5570588197:AAGaZbp8E2S_YoTlAGE2Tmms_CXJmnrzoPw')


@bot.message_handler(command=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Dobrý den, Nikolay! 🙋\nZískávejte kvalitnější produkty za nižší náklady.\nS '
                                      'čím vám dnes můžeme pomoct? 😊')


bot.polling(none_stop=True)
