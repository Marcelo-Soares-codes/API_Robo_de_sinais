import api_signals as signals
import API_Scraping.api_blaze as blaze
from telebot import TeleBot

def menssagem_signal(times):
    return f"""🤑⚪️ VikingBot Lista de Brancas ⚪️🤑

{times[0]["hour"]}:{times[0]["minute"]} ⚪
{times[1]["hour"]}:{times[1]["minute"]} ⚪
{times[2]["hour"]}:{times[2]["minute"]} ⚪
{times[3]["hour"]}:{times[3]["minute"]} ⚪

🪓 𝗣𝗿𝗼𝗯𝗮𝗯𝗶𝗹𝗶𝗱𝗮𝗱𝗲 𝗱𝗲 𝗕𝗿𝗮𝗻𝗰𝗮:
𝗱𝗮𝘀 {times[0]["hour"]}:{times[0]["minute"]} 𝗮𝘁𝗲́ {times[3]["hour"]}:{times[3]["minute"]} ⚪"""

 
def menssage_victory(hour, min):
    return f"""{hour}:{min} ⚪ = WIN BRANCO! ✅✅✅"""


token = "6060820498:AAFQJy1ol0TZdIegzFfbrneMIVPM5Iumu4o"  # Aqui deve ser inserido o token do seu bot
chat_id = "5065618545"  # Aqui deve ser inserido o chat id do seu bot
bot = TeleBot(token=token)
bot.send_message(chat_id, "🤖 Robot Starting")

ApiDouble = blaze.DoubleApi()
ApiBranco = signals.Signals_Branco()

while True:
    ApiDouble.wait_rolling()
    last_number = ApiDouble.last_number_current()
    last_color = ApiDouble.last_color_current()
    last_numbers, last_colors = ApiDouble.limit_lists(last_number, last_color)
    check_white = ApiBranco.generate_times(last_colors=last_colors)

    if check_white["signal"]:
        bot.send_message(chat_id, menssagem_signal(check_white["times"]))
        check_victory = ApiBranco.check_victory(last_colors=last_colors, last_minute=check_white["last_minute"])
        while True:
            ApiDouble.wait_rolling()
            last_number = ApiDouble.last_number_current()
            last_color = ApiDouble.last_color_current()
            last_numbers, last_colors = ApiDouble.limit_lists(last_number, last_color)
            check_victory = ApiBranco.check_victory(last_colors=last_colors, last_minute=check_white["last_minute"])
            if check_victory["break"]:
                break
            elif check_victory["victory"]:
                bot.send_message(chat_id, menssage_victory(check_victory["hour"], check_victory["minute"]))
                