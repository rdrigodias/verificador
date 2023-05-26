import socket
import time
import os
import telegram

bot = telegram.Bot(token='AQUI_SEU_TOKEN')
chat_id = 'AQUI_SEU_ID'

with open("/home/meus-front.txt", "r") as f:
    dominios = f.read().splitlines()

online = 0
offline = 0
offline_dominios = []
last_messages = []  # Armazena os IDs das mensagens enviadas pelo bot

# Envia a mensagem de aviso com delay de 1 minuto
msg_aviso = bot.send_message(chat_id=chat_id, text="⚠️ Em 1 minuto vai acontecer a verificação de CloudFront... ⚠️")
time.sleep(60)
bot.delete_message(chat_id=chat_id, message_id=msg_aviso.message_id)

# Inicia a verificação de CloudFront
msg_inicio = bot.send_message(chat_id=chat_id, text="♻️ Iniciando Verificação de Front... ♻️")

for dominio in dominios:
    if len(dominio) > 0:
        try:
            socket.gethostbyname(dominio)
            print("\033[32mO CloudFront " + dominio + " está online.\033[m")
            # Envia a mensagem e armazena o ID de mensagem retornado
            msg = bot.send_message(chat_id=chat_id, text="O CloudFront {} está online 🟢".format(dominio))
            last_messages.append(msg.message_id)
            online += 1
        except socket.error:
            print("\033[31mO CloudFront " + dominio + " está offline.\033[m")
            # Envia a mensagem e armazena o ID de mensagem retornado
            msg = bot.send_message(chat_id=chat_id, text="O CloudFront {} está offline 🔴".format(dominio))
            last_messages.append(msg.message_id)
            offline += 1
            offline_dominios.append(dominio)
    time.sleep(3)

# Verificação Concluída!
for msg_id in last_messages:
    bot.delete_message(chat_id=chat_id, message_id=msg_id)
bot.delete_message(chat_id=chat_id, message_id=msg_inicio.message_id)
print("Verificação Concluída!")
bot.send_message(chat_id=chat_id, text="✅ Verificação Concluída! ✅")
bot.send_message(chat_id=chat_id, text="📊 Relatório de verificação 📊\n🟢 Fronts Online: {}\n🔴 Fronts Offline: {}".format(online, offline))
if offline_dominios:
    offline_msg = "👉🏻Os seguintes Fronts estão offline🔴:\n"
    for dominio in offline_dominios:
        offline_msg += "- {}\n".format(dominio)
    bot.send_message(chat_id=chat_id, text=offline_msg)
bot.send_message(chat_id=chat_id, text="⏳ A próxima verificação de CloudFront acontecerá em 30 minutos...")
