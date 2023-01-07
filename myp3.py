import telebot
import re
bot = telebot.TeleBot("5056731306:AAHZDKfF-Kp1f8qid8AilyWQ_OOuW-Mt6Mk")
from time import sleep





ADMIN_ID = 1287589438
pattern1 = re.compile(r'\b(Рамуля|Ramulya)\b', re.IGNORECASE)
pattern2 = re.compile(r'[РАМУЛЯрамуля]+', re.IGNORECASE)




@bot.message_handler(commands=['snow'])
def sends(message):
    msg = bot.reply_to(message,"☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁ \n \n \n \n \n \n \n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️")
    sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text='☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁   \n  ❄️      ❄️    ❄️  ❄️      ❄️  ❄️ \n \n \n \n \n \n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄  ')
    sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text='☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁   \n  ❄️      ❄️    ❄️  ❄️      ❄️  ❄️\n❄️      ❄️    ❄️  ❄️      ❄️  ❄\n    ❄️      ❄️    ❄️  ❄️      ❄️  ❄️️ \n \n \n \n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄  ')
    sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text='☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁   \n  ❄️      ❄️    ❄️  ❄️      ❄️  ❄️\n❄️      ❄️    ❄️  ❄️      ❄️  ❄\n    ❄️      ❄️    ❄️  ❄️      ❄️  ❄\n❄️      ❄️    ❄️  ❄️      ❄️  ❄ \n    ❄️      ❄️    ❄️  ❄️      ❄️  ❄️️ \n \n⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄  ')
    sleep(1)
    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text='☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁   \n  ❄️      ❄️    ❄️  ❄️      ❄️  ❄ ️\n❄️      ❄️    ❄️  ❄️      ❄️  ❄\n    ❄️      ❄️    ❄️  ❄️      ❄️  ❄\n❄️      ❄️    ❄️  ❄️      ❄️  ❄ \n    ❄️      ❄️    ❄️  ❄️      ❄️  ❄️️ \n \nH️☃️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄  ')
    sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text='☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁   \n  ❄️      ❄️    ❄️  ❄️      ❄️  ❄ ️\n❄️      ❄️    ❄️  ❄️      ❄️  ❄\n    ❄️      ❄️    ❄️  ❄️      ❄️  ❄\n❄️      ❄️    ❄️  ❄️      ❄️  ❄ \n    ❄️      ❄️    ❄️  ❄️      ❄️  ❄️️ \n \nH ️A️⛄️☃️⛄️☃️⛄️☃️⛄️☃️⛄  ')
    sleep(0.1)
    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text='☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁   \n    💥🎉🥳💥🎉\n❄️      ❄️    ❄️  ❄️      ❄️  ❄\n    ❄️      ❄️    ❄️  ❄️      ❄️  ❄\n❄️      ❄️    ❄️  ❄️      ❄️  ❄ \n    ❄️      ❄️    ❄️  ❄️      ❄️  ❄️️ \n \nH ️A ️P ️P️⛄️☃️⛄️☃️⛄️☃️⛄  ')
    sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text='☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁   \n    💥🎉🥳💥🎉🎈🎁🎊💥\n❄️      ❄️    ❄️  ❄️      ❄️  ❄\n    ❄️      ❄️    ❄️  ❄️      ❄️  ❄\n❄️      ❄️    ❄️  ❄️      ❄️  ❄ \n    ❄️      ❄️    ❄️  ❄️      ❄️  ❄️️ \n \nH ️A ️P ️P ️Y   ️☃️⛄️☃️⛄️☃️⛄  ')
    sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text='☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁   \n    💥🎉🥳💥🎉🎈🎁🎊💥\n\n    ❄️      ❄️    ❄️  ❄️      ❄️  ❄\n❄️      ❄️    ❄️  ❄️      ❄️  ❄ \n    ❄️      ❄️    ❄️  ❄️      ❄️  ❄️️ \n \nH ️A ️P ️P ️Y    ️N E️☃️⛄️☃️⛄  ')
    sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text='☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁   \n    💥🎉🥳💥🎉🎈🎁🎊💥\n\n\n❄️      ❄️    ❄️  ❄️      ❄️  ❄ \n    ❄️      ❄️    ❄️  ❄️      ❄️  ❄️️ \n \nH ️A ️P ️P ️Y    ️N E W    ️⛄️☃️⛄  ')
    sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text='☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁   \n    💥🎉🥳💥🎉🎈🎁🎊💥\n\n\n\n    ❄️      ❄️    ❄️  ❄️      ❄️  ❄️️ \n \n   🎉   H ️A ️P ️P ️Y    ️N E W    D️⛄  ')
    sleep(0.2)
    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text='☁️🌨☁️🌨☁️🌨☁️🌨☁️🌨☁   \n    💥🎉🥳💥🎉🎈🎁🎊💥\n\n\n\n    ❄️      ❄️    ❄️  ❄️      ❄️  ❄️️ \n \n 🎉   H ️A ️P ️P ️Y    ️N E W    D A Y 🎉')




    
@bot.message_handler(content_types=['text'])
def send(message):
   msg = message.text.lower()
   if pattern1.search(message.text) or pattern2.search(text):
    bot.delete_message(message.chat.id, message.message_id)
   elif msg == 'ау':
    bot.reply_to(message, 'Нанпалааау🤣')
   elif msg =='au':
    bot.reply_to(message, 'Nanpalaaau🤣')
   elif msg == '-смс' and message.from_user.id==ADMIN_ID:
    bot.delete_message(message.chat.id, message.reply_to_message.id)
    bot.delete_message(message.chat.id,message.id)
   elif message.from_user.id==2106692657:
       bot.delete_message(message.chat.id, message.id)
   elif message.text.lower()=='нет':
       bot.reply_to(message, 'минет')
   elif message.text.lower()=='ага':
       bot.reply_to(message,'курага')

 
    


  
   


bot.infinity_polling()
