import telebot
import random
bot = telebot.TeleBot('token')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я - бот, если ты напишешь мне название подкаста, я выдам его тебе')


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Напиши название подкаста, или /random если хочкшь послушать случайный, если хочешь узнать самый популярный подкаст напиши /top')

@bot.message_handler(commands=['random'])
def start_message(message):
    chat_id = message.chat.id

    f = open('text.txt', 'r')
    file = f.read()
    file = file.split('\n')
    fil = random.randint(0, len(file))
    filee = str(file[fil]).split(' h')
    bot.send_message(chat_id, filee)
    bot.send_message(chat_id, filee[1])
    f.close()
    fa = open('top.txt', 'a')
    fa.write(str(filee[0]) + '\n')
    fa.close()



@bot.message_handler(commands=['top'])
def top(message):
    chat_id = message.chat.id
    f = open('top.txt', 'r')

    file = f.read()
    file = file.split('\n')
    top = ''

    score = 0
    top_s = 0
    for i in range(len(file)):
        for j in range(i, len(file)):
            if file[i] == file[j]:
                score += 1
        if score > top_s:
            top_s = score
            top = file[i]
        score = 0
    f.close()
    bot.send_message(chat_id, 'самый популярный подкаст: ' + top)




@bot.message_handler(content_types=['text'])
def text_handler(message):
    text1 = message.text.lower()

    chat_id = message.chat.id
    f = open('text.txt', 'r')
    file = f.read()
    file = file.split('\n')
    for i in range(len(file)):
        file[i] = str(file[i]).split(' h')

    f.close()
    for i in range(len(file)):

        if file[i][0] == text1:

            bot.send_message(chat_id, file[i][1])
            fa = open('top.txt', 'a')

            fa.write(str(file[i][0]) + '\n')
            fa.close()


bot.polling(none_stop=True)

