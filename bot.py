from telegram import Update
from telegram.ext import CallbackContext
from telegram import ReplyKeyboardMarkup
from telegram import KeyboardButton
from telegram import ReplyKeyboardRemove
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler

#наши подробности
#создаем кнопку помощь
button_help = 'Помощь'
def button_help_handler(update : Update, context: CallbackContext):
    update.message.reply_text(
        text='Я бот-мизантроп. Справься как-нибудь сам со своей проблемой! Еще можешь написать @mary_v_q или Кате Новицкой(самой лучшей старосте во вселенной). Что-то еще нужно?',
        reply_markup=ReplyKeyboardRemove(),
    )
#создаем менюшку-новости
button_menu = 'Новости'
def button_menu_handler(update : Update, context: CallbackContext):
    update.message.reply_text(
        text='Последние новости: скоро будет телеграм-бот!',
        reply_markup=ReplyKeyboardRemove(),
    )
#кнопка, чтоб перейти к предмету(в будущем), а пока общая инфа + Введи название и тд.

button_subs = 'Курсы'
def button_subs_handler(update : Update, context: CallbackContext):
    update.message.reply_text(
        text='Введи название предмета/фамилию препода. Если хочешь узнать общую информацию о предметах напиши "инфа" (без кавычек, разумеется)',
        reply_markup=ReplyKeyboardRemove(),
    )
#общая инфа по предметам
button_inf = 'Инфа'
def button_inf_handler(update : Update, context: CallbackContext):
    update.message.reply_text(
        text='Здесь будет общая информация по предметам. Что как где куда.',
        reply_markup=ReplyKeyboardRemove(),
    )



#пошли предметы
    
button_rodionov = 'Матстат лекции'
def button_rodionov_handler(update : Update, context: CallbackContext):
        update.message.reply_text(
            text='Математическая статистика. Лекции.\n Занятия в онлайн-формате Родионов проводить не будет, потому что по четвергам (нам, соответственно, лекции будут попадать после) проводит точно такие же лекции в ШАДе и большой разницы между просмотром в Ютубе и лекцией онлайн не будет.\n Если возникают вопросы по ходу лекции – пишите их мне, буду отсылать ему на почту кучей. \n 2) Смотрите файлы MSPS_2020_1.pdf, MSPS_2020_2.pdf, MSPS_2020_3.pdf, MSPS_2020_4_1.pdf, MSPS_2020_4_2.pdf, MSPS_2020_5.pdf, MSPS_2020_6.pdf, MSPS_2020_7.pdf \n 3) Плейлист с лекциями: https://www.youtube.com/playlist?list=PLs-BvBCvcJRXXaS64uJOgx6G8t7kTE_x',
            reply_markup=ReplyKeyboardRemove(),
        )
button_muromskaya= 'Матстат лекции'
def button_muromskaya_handler(update : Update, context: CallbackContext):
        update.message.reply_text(
            text='Математическая статистика. Семинары.',
            reply_markup=ReplyKeyboardRemove(),
        )

button_algebra = 'Алгебра'
def button_algebra_handler(update : Update, context: CallbackContext):
        update.message.reply_text(
            text='Алгебра. "Попозже отправлю, пораньше сделают"\n Домашние задания он проверяет и просит присылать себе на почту. Кидаете мне – я скидываю общим архивом. \n 2) Домашнее задание на 17.04.2020: «Теория - задача распределения кредита - лекции раздел 2.2, стр.39 - 46. Здесь изложена постановка задачи и алгоритм. Упражнения. а) Задания 3.4 (1,2) на стр. 53.б) В лекции алгоритм приведен без обоснования. Последняя задача - обосновать алгоритм из лекций». \n 3) Дедлайн: пятница17.04.2020 в 17:00 отсылаю архив. \n 4) Файл с материалами и задачами vavt19a.pdf.',
            reply_markup=ReplyKeyboardRemove(),
        )
button_urchp = 'УРЧП'
def button_urchp_handler(update : Update, context: CallbackContext):
        update.message.reply_text(
            text='УРЧП',
            reply_markup=ReplyKeyboardRemove(),
        )
button_diskra = 'Дискра'
def button_diskra_handler(update : Update, context: CallbackContext):
        update.message.reply_text(
            text='Дискра. "Это я не рассказываю в этом курсе" by Гашков ',
            reply_markup=ReplyKeyboardRemove(),
        )
button_death = 'Актуарка'
def button_death_handler(update : Update, context: CallbackContext):
        update.message.reply_text(
            text='Актуарка. Объявляется конкурс на смешные шутки',
            reply_markup=ReplyKeyboardRemove(),
        )
button_finmath = 'Финансовая'
def button_finmath_handler(update : Update, context: CallbackContext):
        update.message.reply_text(
            text='Финансовая математика. \n 1) Читайте главы книги. Жуленев ЖДЕТ вопросы от нас. \n 2) Попросил собирать вопросы кучей и кому-то одному задавать их ему по телефону. ',
            reply_markup=ReplyKeyboardRemove(),
        )
button_russ = 'Русский'
def button_russ_handler(update : Update, context: CallbackContext):
        update.message.reply_text(
            text='Русский',
            reply_markup=ReplyKeyboardRemove(),
        )






#в хэндлере хранится клавиатура(кнопки)
def message_handler(update : Update, context: CallbackContext):
    text = update.message.text
    if text == button_help:
        return button_help_handler(update=update, context=context)

    if text == 'Инфа' or text == 'инфа':
        return button_inf_handler(update=update, context=context)
    if text == 'Нет' or text == 'нет' or text == 'no' or text == 'nope':
        update.message.reply_text(
        text='Что нет? Если больше ничего не нужно, то пока! Удачи на сессии!)',
        reply_markup=ReplyKeyboardRemove(),
    )
        return text

    if text == 'Ор' or text == 'Лол' or text == 'ахахах' or text == 'Ахах':
        update.message.reply_text(
        text=')))))))))))',
        reply_markup=ReplyKeyboardRemove(),
    )
        return text
    if text == 'Ок' or text == 'ok' or text == 'ок' or text == 'ok':
        update.message.reply_text(
        text='Ну ок и ок',
        reply_markup=ReplyKeyboardRemove(),
    )
        return text

    if text == 'Дифгем' or text == 'Диффгем':
        update.message.reply_text(
        text='Дифгем, дифгем, дифгемчик. Эх, к сожалению, он закончился(. ',
        
        reply_markup=ReplyKeyboardRemove(),
    )
        return text


    if text == 'Матстат':
        update.message.reply_text(
        text='Молодец, что решил позаниматься! Где-то радуется Родионов! А что именно: лекции, семинары? (Набери "Матстат семинары" или "матстат лекции")',
        reply_markup=ReplyKeyboardRemove(),
    )
        return text

    if text == 'Матстат семинары' or text == 'Муромская' or text == 'матстат семинары' or text == 'мирера' or text == 'Мирера':
        return button_muromskaya_handler(update=update, context=context)
    if text == 'Матстат лекции' or text == 'Родионов' or text == 'матстат лекции':
        return button_rodionov_handler(update=update, context=context)
    if text == 'Алгебра' or text == 'Артамонов' or text == 'Артамон' or text == 'артамонов' or text == 'артамон' or text == 'алгебра':
        return button_algebra_handler(update=update, context=context)
    if text == 'УРЧП' or text == 'Капустина' or text == 'Урчп' or text == 'капустина' or text == 'урчп':
        return button_urchp_handler(update=update, context=context)
    if text == 'Дискра' or text == 'Гашков' or text == 'гашков' or text == 'дискра':
        return button_diskra_handler(update=update, context=context)
    if text == 'Актуарка' or text == 'Гнеденко' or text == 'гнеденко' or text == 'актуарка':
        return button_death_handler(update=update, context=context)
    if text == 'Русский' or text == 'Кислова' or text == 'русский' or text == 'русичка':
        return button_russ_handler(update=update, context=context)
    if text == 'Финансовая' or text == 'Финмат' or text == 'Жулик' or text == 'Жуленев':
        return button_finmath_handler(update=update, context=context)
    
    
    
    
    if text == button_menu:
        return button_menu_handler(update=update, context=context)

    if text == button_subs:
        return button_subs_handler(update=update, context=context)


    reply_markup = ReplyKeyboardMarkup(
        keyboard = [
            [
                KeyboardButton(text=button_help),
                KeyboardButton(text=button_menu),
                KeyboardButton(text=button_subs),
            ],
        ],
        resize_keyboard=True,
    )
    update.message.reply_text(
        text = 'Выбери кнопку ниже!',
        reply_markup=reply_markup,
    )







#здесь функция для старта и токен
def main():
    print('Start')

    updater=Updater(
        token='1119911859:AAHtzbMglMX2k3ZdYOTUDJZbm3Kgmi75u1s',  #токен бота в телеге
        use_context=True,  
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))
    # Filters.all - это когда на вход можно принимать любые сообщения. Можно еще например Filters.text

    updater.start_polling()
    #запускает сканчивание обновлений, но один раз
    updater.idle()
#заморозим выаолнение кода, пока не будет новой команды
if __name__ == '__main__':
    main()

