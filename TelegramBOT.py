import telepot
import time
from telepot.loop import MessageLoop

bot = telepot.Bot('1180280159:AAEFHdebdPYp6E-HIly7OQsZ_X9trVjcSqk')
f = open("users.txt", "r")
userstxt = f.readline()
users = list(userstxt.split(" "))
usersstring = str(' ')


def listtostr():
    usersstring = str(' '.join(users))
    with open("users.txt", "w") as output:
        output.write(usersstring)

def newuser():
    for i in bot.getUpdates(allowed_updates=True):
        firstname = i['message']['from']['first_name']
        if firstname not in users:
            users.append(firstname)
            bot.sendMessage(-1001155258682, '{} foi adicionado aos usuários.'.format(firstname))
            listtostr()


def handle(msg):
    chat = msg['from']['first_name']
    # chat_id = '1180280159' #Adicionar ID do grupo ou do usuário.
    newuser()
    try:
        command = msg['text']
    except KeyError:
        command = 'Sticker'
    user_id = msg['from']['id']
    print('ID:', user_id, 'Usuário:', chat, ':', command)

    if command == '/users':
        bot.sendMessage(-1001155258682, 'Usuários do grupo : {}'.format(' '.join(users)))
    elif 'cu' in  command.lower():
        bot.sendMessage(-1001155258682, 'Agora eu to puto e vo comer teu cu')


def upbot():
    if bot.getUpdates(allowed_updates=True) == []:
        print('Parametros do getUpdates não foram atualizados.')
        time.sleep(10)


MessageLoop(bot, handle).run_as_thread()
print('Listening ...')
upbot()

while 1:
    time.sleep(10)
