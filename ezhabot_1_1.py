import telebot;
bot = telebot.TeleBot('5111904045:AAGYb83-gjCD0JqsKbRZCRCd-WDP1UYhTCA');

name=""

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global name
    if name=="тоже Ёжик":
        name = message.text
        bot.send_message(message.from_user.id, "Рад с тобой познакомится " + name) 
    elif str(message.text).lower() == "/name":
        bot.send_message(message.from_user.id, "Тебя зовут " + name) 
    elif str(message.text).lower() == "привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif str(message.text).lower() == "/help":
        bot.send_message(message.from_user.id, "Здесь можно написать команду. Например напиши: привет!")
    elif str(message.text).lower() == "ёжик":
        bot.send_message(message.from_user.id, "Да я знаю что я Ёжик! А тебя как зовут?") 
        name="тоже Ёжик"
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)