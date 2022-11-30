import telebot
from config import keys, header, TOKEN
from extentions import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help_me(message: telebot. types . Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате: \n<В какую валюту> \
<ИЗ какой валюты> \
<количество переводимой валюты> \nНапример: "рубль авс.доллар 1000" выведет "Курс: 41082.841 RUB за 1000 AUD"\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot. types .Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types. Message):
    try:
        con_values = message.text.split(' ')
        if len(con_values) != 3:
            raise ConversionException('Неправильное количество параметров.')
        to_cur, from_cur, amount = con_values

        result = Converter.get_price(to_cur, from_cur, amount)
    except ConversionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'не удалось обработать команду\n{e}')
    else:
        bot.send_message(message.chat.id, f'Курс: {result} {keys[to_cur]} за {amount} {keys[from_cur]}')


bot.polling(none_stop=True)
