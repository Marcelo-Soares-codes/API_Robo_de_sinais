import api_signals as signals
from telebot import TeleBot
from time import sleep as sl
import random


token = ""  # Aqui deve ser inserido o token do seu bot
chat_id = ""  # Aqui deve ser inserido o chat id do seu bot
bot = TeleBot(token=token)
# bot.send_message(chat_id, "🤖 Robot Starting")

ApiMines = signals.Signals_Mines()

while True:
    mines = ApiMines.main(size_mines=25, num_diamonds=random.randint(3, 6))
    msg = f"""✅ 𝗦𝗶𝗻𝗮𝗹 𝗰𝗼𝗻𝗳𝗶𝗿𝗺𝗮𝗱𝗼 ✅ 
💣 𝗠𝗶𝗻𝗮𝘀 : 3
⏰ 𝗩𝗮𝗹𝗶𝗱𝗮𝗱𝗲 2 𝗺𝗶𝗻𝘂𝘁𝗼𝘀  
🔸 𝗡° 𝗱𝗲 𝗲𝗻𝘁𝗿𝗮𝗱𝗮 𝟯 

{mines["mines"]}"""
    bot.send_message(chat_id, msg)
    sl(random.randint(130, 500)) # uma pausa aleatoria entre 2min a 5min
