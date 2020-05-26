import telepot
import time
from telepot.loop import MessageLoop

bot = telepot.Bot('1180280159:AAGt0lOrPGmvoMLDE_7S2CHm43i72Gc8ATw')
f = open("users.txt", "r")
userstxt = f.readline()
users = list(userstxt.split(" "))
usersstring = str(' ')


def listtostr():
    usersstring = str(' '.join(users))
    with open("users.txt", "w") as output:
        output.write(usersstring)


def newuser():
    for i in bot.getUpdates(offset=100000001):
        firstname = i['message']['from']['first_name']
        if firstname not in users:
            users.append(firstname)
            bot.sendMessage(-1001155258682, '{} foi adicionado aos usuários.'.format(firstname))
            listtostr()


def handle(msg):
    chat = msg['from']['first_name']
    message_id = msg['message_id']
    newuser()
    try:
        command = msg['text']
    except KeyError:
        command = 'Sticker'
    user_id = msg['from']['id']
    print('ID:', user_id, 'Usuário:', chat, ':', command)

    if command == '/users':
        bot.sendMessage(-1001155258682, 'Usuários do grupo : {}'.format(' '.join(users)),reply_to_message_id=message_id)
    elif 'cu' in command.lower():
        bot.(-1001155258682, 'Agora eu to puto e vo comer teu cu', reply_to_message_id=message_id)
    if command == '@closeapp':
        bot.sendMessage(-1001155258682,'Finalizando....')
        time.sleep(2)
        quit()




MessageLoop(bot, handle).run_as_thread()
while True:
    time.sleep(5)
