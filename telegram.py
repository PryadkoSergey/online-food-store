import telebot
from telebot import types
import sqlite3
import time

client = telebot.TeleBot('1954889691:AAEIVjuvH2jofswxG_1wj4-zzRwl88LDYhs')

def message_step1(mes):
    markup_inline = types.InlineKeyboardMarkup()
    item3 = types.InlineKeyboardButton(text = '☆', callback_data = '3')
    item4 = types.InlineKeyboardButton(text = '☆☆', callback_data = '4')
    item5 = types.InlineKeyboardButton(text = '☆☆☆', callback_data = '5')
    item6 = types.InlineKeyboardButton(text = '☆☆☆☆', callback_data = '6')
    item7 = types.InlineKeyboardButton(text = '☆☆☆☆☆', callback_data = '7')
    markup_inline.add(item3,item4,item5,item6,item7)
    client.send_message(mes.chat.id,'Замовлення №1 > Готовий \n\nБлин "Рубленное мясо в красном соусе"\n\nДо сплати: 100.00₴\n\nМелітополь, Запорізька область, Украина, 72300')
    client.send_message(mes.chat.id,'Дякуємо за замовлення!\nВам все сподобалось по замовленню №1?\n\nМелітополь, Запорізька область, Украина, 72300')
    client.send_message(mes.chat.id,'Оцініть якщо не складно)',reply_markup=markup_inline)
    
#start
@client.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Меню')
    markup.add(item1)
    number = message.text.split()[-1] #разбить на слова и выбрать последнее
    print(number) #id заказа
    
    sqlite_connection = sqlite3.connect('db.sqlite3')
    cursor = sqlite_connection.cursor()
    print("База данных успешно подключена к SQLite")
    
    name = ""
    for row in cursor.execute('SELECT * FROM main_order'):
        if str(row[0]) == str(number): 
            name = ", " + str(row[1])
        
    cursor.close()
    client.send_message(message.chat.id, ('Добрый день'+ name+'. Ваш номер заказа ' + str(number) + '. \n Мы сообщим Вам когда ваш заказ будет готов. Ожидайте!'), reply_markup = markup)
    time.sleep(10)
    message_step1(message)
    

#Menu
@client.message_handler(content_types = ['text'])
def bot_menu(message):
    if message.chat.type=='private':
        if message.text=='Меню':
            markup_inline = types.InlineKeyboardMarkup()
            item2 = types.InlineKeyboardButton(text = 'Ссылка', callback_data = '2')
            markup_inline.add(item2)
            client.send_message(message.chat.id, 'Натисніть кнопку, щоб перейти у меню', reply_markup = markup_inline)

        elif message.text=='1':
           message_step1(message)

@client.callback_query_handler(func = lambda call: True)
def callback(call):
    if call.message:
        if call.data =='3':
            client.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,text= 'Дякую, ви оцінили на 1.')
        elif call.data =='4':
            client.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,text= 'Дякую, ви оцінили на 2.')
        elif call.data =='5':
            client.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,text= 'Дякую, ви оцінили на 3.')
        elif call.data =='6':
            client.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,text= 'Дякую, ви оцінили на 4.')
        elif call.data =='7':
            client.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,text= 'Дякую, ви оцінили на 5.')
        elif call.data =='2':
            client.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,text= 'http://127.0.0.1:8000/')


#client.polling(none_stop=True, interval=0)
client.polling(interval=0)