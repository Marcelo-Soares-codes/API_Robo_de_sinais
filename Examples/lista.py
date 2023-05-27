import api_signals as signals
from telebot import TeleBot
from datetime import datetime as dt


token = ""  # Aqui deve ser inserido o token do seu bot
chat_id = ""  # Aqui deve ser inserido o chat id do seu bot
bot = TeleBot(token=token)
# bot.send_message(chat_id, "🤖 Robot Starting")

ApiList = signals.Signals_List()

while True:
    min = int(dt.now().strftime('%M'))
    if min >= 55:
        hour = int(dt.now().strftime('%H')) + 1
        result = ApiList.main(num_doubles=15, num_crashs=15, hour=str(hour).zfill(2))

        crash = result["crash"]

        double = result["double"]

        times_crash = ""
        for time in crash:
            times_crash += f'{time["hour"]}:{time["minute"]} 2x 🚀\n'

        times_double = ""
        for time in double:
            times_double += f'{time["hour"]}:{time["minute"]}{time["color"]}{time["white"]}\n'

        msg_crash = f"""⚔️ Lista VikingBot | Crash ⚔️

🐣 Listinha até G1, o G2 é Opcional 🐣

        ⚠️GERENCIAMENTO⚠️

{times_crash}


Relógio com o horário👇
https://relogioonline.com.br/horario/bras%C3%ADlia/

🛡️NÃO ENTRAR CONTRA TENDÊNCIA!!!🛡️
    EXEMPLO➡️☑☑☑☑👉✅
"""

        msg_double = f"""⚔️ Lista VikingBot | Double ⚔️

🐣 Listinha até G1, o G2 é Opcional 🐣

        ⚠️GERENCIAMENTO⚠️

{times_double}


Relógio com o horário👇
https://relogioonline.com.br/horario/bras%C3%ADlia/

🛡️ NÃO ENTRAR CONTRA TENDÊNCIA!!! 🛡️
    EXEMPLO➡️🔴🔴🔴🔴👉⚫️"""

        bot.send_message(chat_id, msg_crash)
        bot.send_message(chat_id, msg_double)
        while True:
            min = int(dt.now().strftime('%M'))
            if min < 55:
                break