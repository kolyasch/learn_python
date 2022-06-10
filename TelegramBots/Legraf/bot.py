from telebot import telebot, types

bot = telebot.TeleBot('5570588197:AAFJtMlt1CIcE47IdyPegeie33OAOOStpzE')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Otevírací doba ⏰')
    item2 = types.KeyboardButton('Adresa 🏘')
    item3 = types.KeyboardButton('Kontakt 📲')
    item4 = types.KeyboardButton('Objednat si 🖼')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, f'Dobrý den, {message.from_user.first_name}! 🙋\n\nZískávejte kvalitnější '
                                      f'produkty za nižší náklady.\nS čím vám dnes můžeme pomoct? 😊')


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Otevírací doba ⏰':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('👈 zpátky')
            markup.add(item1)
            bot.send_message(message.chat.id, 'Pondělí: 08:00 - 16:00\nÚterý: 08:00 - 16:00\nStředa: 08:00 - '
                                              '18:00\nČtvrtek: 08:00 - 16:00\nPátek: 08:00 -14:00\nSobota a neděle: '
                                              'zavřeno 🔒')

        elif message.text == '👈 zpátky':
            start()
        elif message.text == 'Adresa 🏘':
            bot.send_message(message.chat.id, 'Merhautova 182\n613 00 Brno - Sever\nCzech Republic')
            bot.send_message(message.chat.id, 'Kliknite na mapu, a mate to nachistane ve vasi aplikaci 👇')
            bot.send_location(message.chat.id, 49.2133256, 16.6257878)
        elif message.text == 'Kontakt 📲':
            bot.send_message(message.chat.id, 'mob: +420608706710\ntel: +420515541324\n\ninfo@legraf.cz\nPoptávky, '
                                              'dotazy, příjem zakázek\n\ntisk@legraf.cz\nTisková data a '
                                              'kalkulace\n\nfoto@legraf.cz\nFotografie a tisk na '
                                              'plátno\n\nposter@legraf.cz\nPostery a Kapa desky')
            bot.send_message(message.chat.id, 'Nebo napište v telegramu 👉 @kolyash1')
        else:
            bot.send_message(message.chat.id, 'Promiňte, jsem mlady bot, jeste studuju 😁\nNapište mi prosím semka 👉 '
                                              '@kolyash1')


bot.polling(none_stop=True)
