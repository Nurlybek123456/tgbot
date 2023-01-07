import telebot
import re
import unicodedata
bot = telebot.TeleBot("5056731306:AAHZDKfF-Kp1f8qid8AilyWQ_OOuW-Mt6Mk")
from time import sleep





ADMIN_ID = 1287589438




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

def compare_strings(string1, string2):
    # Convert both strings to lowercase
    string1 = string1.lower()
    string2 = string2.lower()

    # Normalize both strings using NFKD normalization
    string1 = unicodedata.normalize('NFKD', string1)
    string2 = unicodedata.normalize('NFKD', string2)

    # Remove any diacritics and other special characters
    string1 = ''.join(c for c in string1 if not unicodedata.combining(c))
    string2 = ''.join(c for c in string2 if not unicodedata.combining(c))

    # Compare the strings
    if string1 == string2:
        return True
    else:
        return False    
    
@bot.message_handler(func=lambda message: compare_strings(message.text, "Рамуля") or compare_strings(message.text, "Ramulya"))
def delete_message(message):
    if message.from_user.id != ADMIN_ID:
        bot.delete_message(message.chat.id, message.message_id)

    
@bot.message_handler(content_types=['text'])
def send(message):
   msg = message.text.lower()
   text = msg.find("Нарисуй")
   if msg == 'ау':
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
