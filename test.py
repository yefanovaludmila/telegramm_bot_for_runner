import telepot
import time
from telepot.loop import MessageLoop

TOKEN = '673300038:AAGRn7-ObHoL5PeubyLymZ_AtjjO5h1ejkc'
bot = telepot.Bot(TOKEN)

def handle(msg):
    print(msg)
    text = (msg['text'])
    bot.sendMessage(msg['chat']['id'], text)

MessageLoop(bot, handle).run_as_thread()

# import logging
print('I am ready to work ...')

while 1:
    time.sleep(10)