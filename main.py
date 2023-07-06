import telebot
from telebot import types
from PIL import Image, ImageFilter

bot = telebot.TeleBot('token')


@bot.message_handler(commands=['start'])
def start(message):
    mass = f"👋 Привет {message.from_user.first_name}! Я бот который может исказить любую фотографию. Для того, чтобы изменить фотку просто скинь ее мне"
    bot.send_message(message.from_user.id, mass , parse_mode='html')


@bot.message_handler(commands=['primer'])
def primer(message):
    photo = open('stas.jpg', 'rb')
    markup = types.ReplyKeyboardMarkup()
    primer = types.KeyboardButton('Отправь пример жмыха')
    start = types.KeyboardButton('/start')
    markup.add(primer, start)
    bot.send_message(message.from_user.id, 'Посмотри пример жмыха:', parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['primer_2'])
def get_user_text(message):
    if message.text =="Отправь пример жмыха":
        photo = open('stas.jpg','rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю',parse_mode='html')



@bot.message_handler(content_types=(['photo']))
def get_user_photo(message):
    bot.send_message(message.from_user.id,'Крутое фото, щас жмыхну!', parse_mode='html')
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'C:/Users/Дмитрий/PycharmProjects/telegabot_a/files/' + file_info.file_path
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    blur = types.KeyboardButton('Заблюрить')
    contur = types.KeyboardButton('Выделить контуры')
    detail = types.KeyboardButton('Улучшить качество')
    edge = types.KeyboardButton('Четкость границ')
    edge_more = types.KeyboardButton('Больше четкости границ')
    emboss = types.KeyboardButton('Тиснение')
    find_edges = types.KeyboardButton('Обводка краёв')
    sharpen = types.KeyboardButton('Улучшение резкости')
    smooth =types.KeyboardButton('Сглаживание артефактов')
    smooth_more = types.KeyboardButton('Улучшенное сглаживание артефактов')
    markup.add(blur, contur, detail, edge, edge_more, emboss, find_edges, sharpen, smooth, smooth_more)
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    #original = Image.open('C:/Users/Дмитрий/PycharmProjects/telegabot_a/files/' + file_info.file_path)
    #filtred = original.filter(ImageFilter.FIND_EDGES)
    f = open('C:/Users/Дмитрий/PycharmProjects/telegabot_a/files/'+ str(message.chat.id) +'.txt', 'w')
    f.write(src)
    f.close()
    bot.send_message(message.chat.id, 'Что сделать с фоткой?',parse_mode='html', reply_markup=markup)
    return src

@bot.message_handler(content_types=(['text']))
def user_photo(message):
    f = open('C:/Users/Дмитрий/PycharmProjects/telegabot_a/files/'+ str(message.chat.id) +'.txt', 'r')
    src = f.read()
    f.close()
    original = Image.open(src)
    if message.text == 'Заблюрить':
        filtred = original.filter(ImageFilter.BLUR)
        bot.send_photo(message.chat.id, filtred)
    elif message.text == 'Выделить контуры':
        filtred = original.filter(ImageFilter.CONTOUR)
        bot.send_photo(message.chat.id, filtred)
    elif message.text == 'Улучшить качество':
        filtred = original.filter(ImageFilter.DETAIL)
        bot.send_photo(message.chat.id, filtred)
    elif message.text == 'Четкость границ':
        filtred = original.filter(ImageFilter.EDGE_ENHANCE)
        bot.send_photo(message.chat.id, filtred)
    elif message.text == 'Больше четкости границ':
        filtred = original.filter(ImageFilter.EDGE_ENHANCE)
        bot.send_photo(message.chat.id, filtred)
    elif message.text == 'Тиснение':
        filtred = original.filter(ImageFilter.EMBOSS)
        bot.send_photo(message.chat.id, filtred)
    elif message.text == 'Обводка краёв':
        filtred = original.filter(ImageFilter.FIND_EDGES)
        bot.send_photo(message.chat.id, filtred)
    elif message.text == 'Улучшение резкости':
        filtred = original.filter(ImageFilter.SHARPEN)
        bot.send_photo(message.chat.id, filtred)
    elif message.text == 'Сглаживание артефактов':
        filtred = original.filter(ImageFilter.SMOOTH)
        bot.send_photo(message.chat.id, filtred)
    elif message.text == 'Улучшенное сглаживание артефактов':
        filtred = original.filter(ImageFilter.SMOOTH_MORE)
        bot.send_photo(message.chat.id, filtred)





bot.polling(none_stop=True)