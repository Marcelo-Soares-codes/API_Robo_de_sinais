import api_signals as signals
import API_Scraping.api_blaze as blaze
from telebot import TeleBot

patterns = {
    "black":[["black", "red", "red", "red", "red", "red"],
["black", "red", "black", "black", "red", "black"],
["black", "red", "red", "red", "black", "red"],
["black", "black", "black", "red", "red", "red"],
["red", "red", "black", "black", "red", "red"],
["red", "red", "black", "red", "black", "red"],
["black", "red", "black", "red", "black", "red"],
["black", "black", "red", "black", "black", "red"],
["black", "red", "black", "black", "black", "red"],
["red", "black", "red", "black", "red", "red"],
["black", "black", "black", "black", "red", "red"],
["black", "black", "black", "black", "black", "red"],
["black", "black", "red", "red", "black", "red"],
["black", "black", "red", "black", "red", "red"],
["black", "black", "black", "red", "black", "red"],
["black", "red", "black", "black", "red", "red"],
["black", "black", "white", "red", "red"],
["black", "white", "white", "black"],
["black", "red", "white", "black"],
["black", "black", "red", "white"],
["black", "white", "red", "white"]],

"red": [["red", "black", "black", "black", "black", "black"],
["red", "black", "red", "red", "black","red"], 
["red", "black", "black", "black", "red", "black"], 
["red", "red", "red", "black", "black", "black"],
["black", "black", "red", "red", "black", "black"],
["black", "black", "red", "black", "red", "black"],
["red", "black", "red", "black", "red", "black"],
["red", "red", "black", "red", "red", "black"],
["red", "black", "red", "red", "red", "black"],
["black", "red", "black", "red","black", "black"],
["red", "red", "red", "red", "black", "black"],
["red", "red", "red", "red", "red", "black"],
["red", "red", "black", "black", "red", "black"],
["red", "red", "black", "red", "black", "black"],
["red", "red", "red", "black", "red", "black"],
["red", "black", "red", "red", "black", "black"],
["red", "red", "white", "black", "black"],
["red", "white", "white", "red"],
["red", "black", "white", "red"],
["red", "red", "black", "white"],
["red", "white", "black", "white"]]

}

def menssagem_signal(signal_color, last_colors, last_numbers):
    last_color = last_colors[len(last_colors) - 1]
    last_number = last_numbers[len(last_numbers) - 1]
    if signal_color == "red":
        return f"""🔥 Sinal Viking Confirmado 🔥
Após o --> {last_number}[{last_color}]

⚔️ Entre na cor 🔴 [Vermelho]
⚪️ Faça proteção no Branco 🛡️"""

    if signal_color == "black":
        return f"""🔥 Sinal Viking Confirmado 🔥
Após o --> {last_number}[{last_color}]

⚔️ Entre na cor ⚫ [Preto]
⚪️ Faça proteção no Branco 🛡️"""
    if signal_color == "white":
        return f"""🔥 Sinal Viking Confirmado 🔥
Após o --> {last_number}[{last_color}]

⚔️ Entre na cor ⚪️ [White]
⚪️ Faça proteção no Branco 🛡️"""


def menssage_victory(victory, loss, martingale, victory_color):
    if victory:
        if victory_color == "white":
            return "⚪⚪⚪ White ⚪⚪⚪"
        else:
            if martingale == 0:
                return "✅✅✅ VITORIA SG, VAMO LUCRAR ✅✅✅"
            
            elif martingale == 1:
                return "✅✅✅ VITORIA G1, VAMO LUCRAR ✅✅✅"
            
            elif martingale == 2:
                return "✅✅✅ VITORIA G2, VAMO LUCRAR ✅✅✅"
    
    elif loss:
        return "🔺𝗥𝗲𝗱, 𝗩𝗢𝗟𝗧𝗘 𝗠𝗔𝗜𝗦 𝗧𝗔𝗥𝗗𝗘 !"


token = ""  # Aqui deve ser inserido o token do seu bot
chat_id = ""  # Aqui deve ser inserido o chat id do seu bot
bot = TeleBot(token=token)
bot.send_message(chat_id, "🤖 Robot Starting")

ApiDouble = blaze.DoubleApi()
ApiSignal = signals.Signals_Double()
while True:
    ApiDouble.wait_rolling()
    last_number = ApiDouble.last_number_current()
    last_color = ApiDouble.last_color_current()
    last_numbers, last_colors = ApiDouble.limit_lists(last_number, last_color)
    check_pattern = ApiSignal.check_patterns(patterns=patterns, last_numbers=last_numbers, last_colors=last_colors)

    if check_pattern["signal"]:
        bot.send_message(chat_id, menssagem_signal(signal_color=check_pattern["signal_color"], last_colors=last_colors, last_numbers=last_numbers))
        max_martingale = 2
        for martingale in range(max_martingale + 1):
            ApiDouble.wait_rolling()
            last_number = ApiDouble.last_number_current()
            last_color = ApiDouble.last_color_current()
            last_numbers, last_colors = ApiDouble.limit_lists(last_number, last_color)
            check_victory = ApiSignal.check_victory(signal_color=check_pattern["signal_color"], victory_white=True, last_colors=last_colors, martingale=martingale, max_martingale=max_martingale)
            print(check_victory)
            if check_victory["victory"] or check_victory["loss"]:
                bot.send_message(chat_id, menssage_victory(victory=check_victory["victory"], loss=check_victory["loss"], martingale=martingale, victory_color=check_victory["last_color"]))
                break
            

