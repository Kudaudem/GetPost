from pyrogram import Client

#----------------------------------

#api_id и api_hash аккаунта можно получить на my.telegram.org

api_id = 1293791 #только цифры

api_hash = "de4812fb8fbd03a20440c21e644d18aa" #должен быть в скобках

take_from = ["neotchislen", -1001298621390] #откуда хотите брать посты? (юзернейм (в кавычках, без @) или айди канала (без кавычек) ); через запятую

send_to = ["neotchislen"] #айди канала (без кавычек) или юзернейм (в кавычках, без @), куда хотите пересылать посты; через запятую

client = Client("getpost", api_id, api_hash) #если хотите сменить аккаунт, смените getpost на любое другое слово или просто удалите .session файл в папке со скриптом

#----------------------------------
client.start()

@client.on_message()
def handle_messages(app, m):
    try:
        if m.chat.username in take_from or m.chat.id in take_from:
            for channel in send_to:
                m.forward(channel, as_copy=True)
    except Exception as e:
        print(e)
