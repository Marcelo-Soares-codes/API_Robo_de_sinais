import api_signals as signals
import API_Scraping.api_blaze as blaze
from telebot import TeleBot




token = ""  # Aqui deve ser inserido o token do seu bot
chat_id = ""  # Aqui deve ser inserido o chat id do seu bot
bot = TeleBot(token=token)
bot.send_message(chat_id, "🤖 Robot Starting")

pattern = [['black', 'green', 'green'],
['green', 'black', 'black', 'black', 'black'],
['black', 'green', 'green', 'green', 'green'],
['green', 'black', 'green', 'black'],
['green', 'black', 'black', 'green', 'black', 'black']]


def msg_signal(num):
    bot.send_message(chat_id, f"""
⚔️ Sinal Viking Confirmado ⚔️

✅ Entrada agora ✅
🛡️ Entrada após {num}x

𝗦𝗶𝘁𝗲: blaze.com""")
    
def msg_result(victory):
    if victory:
        bot.send_message(chat_id, "✅✅✅ VITORIA, VAMO LUCRAR ✅✅✅")
    else:
        bot.send_message(chat_id, "🔺𝗥𝗲𝗱, 𝗩𝗢𝗟𝗧𝗘 𝗠𝗔𝗜𝗦 𝗧𝗔𝗥𝗗𝗘 !")

ApiCrash = blaze.CrashApi()
ApiSignal = signals.Signals_Crash()

while True:
    ApiCrash.wait_crash()
    last_crash = ApiCrash.last_crash_current()
    last_color = ApiCrash.last_color_current()
    last_crashes, last_colors = ApiCrash.limit_list_crashes(last_crash, last_color)
    signal = ApiSignal.check_pattern(patterns=pattern, last_numbers=last_crashes, last_colors=last_colors)
    if signal["signal"]:
        msg_signal(signal["last_results"]["last_number"])
        max_martingale = 2
        for martingale in range(max_martingale + 1):
            ApiCrash.wait_crash()
            last_crash = ApiCrash.last_crash_current()
            last_color = ApiCrash.last_color_current()
            last_crashes, last_colors = ApiCrash.limit_list_crashes(last_crash, last_color)
            check_pattern = ApiSignal.check_victory(crash_point=2.0, last_number=last_crash, martingale=martingale, max_martingale=max_martingale)
            if check_pattern["victory"] or check_pattern["loss"]:
                msg_result(check_pattern["victory"])
                break
