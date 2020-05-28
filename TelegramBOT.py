import telepot
import time
import random
from telepot.loop import MessageLoop

bot = telepot.Bot('1180280159:AAGt0lOrPGmvoMLDE_7S2CHm43i72Gc8ATw')
f = open("users.txt", "r")
userstxt = f.readline()
users = list(userstxt.split(" "))
usersstring = str(' ')
gays = ["https://www.guiagaysaopaulo.com.br/public/uploads/imagens/originais/major_oficial_exercito_gay_homofobia_mi"
        "litar_emerson_cordeiro_marido.jpg","https://conteudo.imguol.com.br/c/parceiros/fc/2019/09/07/felipe-neto-foto-"
        "reproducaoinstagram-1567885288184_v2_450x450.jpg","https://http2.mlstatic.com/quadro-league-of-legends-lol-ta"
        "ric-D_NQ_NP_965149-MLB32899026504_112019-F.jpg","https://4.bp.blogspot.com/-TV1U1U2gwAU/T-C2UwFyhlI/AAAAAAAAA"
        "n4/Gj243HnHQtM/s1600/kid-bengala73704.jpg"]
dener = 'https://uploaddeimagens.com.br/images/002/611/945/full/dener.jpg?1587793340'


def listtostr():
    usersstring = str(' '.join(users))
    with open("users.txt", "w") as output:
        output.write(usersstring)


def newuser():
    for i in bot.getUpdates(offset=100000001, timeout=5):
        firstname = i['message']['from']['first_name']
        if firstname not in users:
            users.append(firstname)
            bot.sendMessage(-1001155258682, '{} foi adicionado aos usuários.'.format(firstname))
            listtostr()


def handle(msg):
    rusers = random.choice(users)
    chat = msg['from']['first_name']
    message_id = msg['message_id']
    newuser()
    try:
        command = msg['text']
    except KeyError:
        command = 'Sticker'
    user_id = msg['from']['id']
    print('ID:', user_id, 'Usuário:', chat, ':', command)

    if command == '/users' or command == '/users@fockythebot':
        bot.sendMessage(-1001155258682, 'Usuários do grupo : {}'.format('\n'.join(users)),
                        reply_to_message_id=message_id)

    if command.lower() == 'cu':
        bot.sendMessage(-1001155258682, 'Agora eu to puto e vo comer teu cu', reply_to_message_id=message_id)
    
    if 'gay' in command.lower():
        bot.sendMessage(-1001155258682, 'Hoje, o gay é o {}, certeza que chupa pau'
                                        ' '.format(rusers), reply_to_message_id=message_id)
        if rusers == 'Dener':
            bot.sendPhoto(-1001155258682, photo=dener)
        else:
            bot.sendPhoto(-1001155258682, photo=random.choice(gays))
    
    if command == '/autoscript' or command == '/autoscript@fockythebot':
        bot.sendDocument(-1001155258682, document="BQACAgEAAxkBAAOWXs_HDNo1CdMpIa7439o9DxTULGcAAtgAA6iHeEYhG"
                                                  "SlHeQZRXRkE", reply_to_message_id=message_id)
        bot.sendVideo(-1001155258682,video='BAACAgEAAxkBAAOaXtAFnbjRObz2ohx4BI3QyEWoX5cAAs4AA6iHgEa_-kwXd6-o7BkE')

    if command == '/comandos' or command == '/comandos@fockythebot':
        bot.sendMessage(-1001155258682, 'Comandos até o momento:\n"cu"\n"gay"\nusers\nautoscript\ncomandos'
                        , reply_to_message_id=message_id)


MessageLoop(bot, handle).run_as_thread()
while 1:
    time.sleep(5)

