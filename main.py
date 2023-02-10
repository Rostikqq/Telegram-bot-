time_ways = ["Год", "Век"]

main_menu_buttons = ['Подобрать новую литературу 📚', '🏫 Посмотреть не прочитанную школьную 📔']

yesorno = ['Да!', 'Нет, достаточно']

yesorexit = ['Вернуться', 'Нет, пойду читать']

chisla = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

list_choose_how_to_search = ['По автору 🖋', 'По годам ⏱', 'По жанру 📕']

vernutsa = ['Вернуться в меню']

exitout = ["Ещё?", "Вернуться", "Выйти"]

school_searching = ['1-5', '6-9', '10-11']

centuaries = ["XX", 'XIX', 'XVIII']

commandstart = ['/start']

jounre_ways = ["Эпос", "Драма", "Лирика"]

jounre_epos_types = ["Роман", "Рассказ", "Повесть", 'Сказка']
jounre_drama_types = ["Драма", "Комедия"]

school_literature_for_high = ['«ВОЙНА И МИР»', '«МАСТЕР И МАРГАРИТА»', '«КРЫЖОВНИК»', '«ГОСПОДИН ИЗ САН-ФРАНЦИСКО»', '«ЧИСТЫЙ ПОНЕДЕЛЬНИК»', '«ТЕМНЫЕ АЛЛЕИ»', '«ИСТОРИЯ ОДНОГО ГОРОДА»', '«СТАРУХА ИЗЕРГИЛЬ»', '«МАКАР ЧУДРА»', '«НОС»', '«НЕВСКИЙ ПРОСПЕКТ»', '«ОТЦЫ И ДЕТИ»', '«ПРЕСТУПЛЕНИЕ И НАКАЗАНИЕ»', '«ДВЕНАДЦАТЬ»']

school_literature_for_middle = ['«ХАДЖИ-МУРАТ»', '«КАВКАЗСКИЙ ПЛЕННИК»', '«ДУБРОВСКИЙ»', '«ЧЕЛОВЕК В ФУТЛЯРЕ»', '«ИОНЫЧ»', '«ХАМЕЛЕОН»', '«КАПИТАНСКАЯ ДОЧКА»', '«ДАМА С СОБАЧКОЙ»', '«ВИШНЕВЫЙ САД»', '«РЕВИЗОР»', '«ШИНЕЛЬ»', '«МЕРТВЫЕ ДУШИ»', '«МУМУ»', '«АСЯ»', '«ЕВГЕНИЙ ОНЕГИН»', '«ГЕРОЙ НАШЕГО ВРЕМЕНИ»', '«ТАРАС БУЛЬБА»', '«НЕДОРОСЛЬ»', '«ТОЛСТЫЙ И ТОНКИЙ»', '«СМЕРТЬ ЧИНОВНИКА»', '«СТАНЦИОННЫЙ СМОТРИТЕЛЬ»', '«БАРЫШНЯ-КРЕСТЬЯНКА»', '«МЦЫРИ»', '«ПЕСНЯ ПРО ЦАРЯ ИВАНА ВАСИЛЬЕВИЧА, МОЛОДОГО ОПРИЧНИКА И УДАЛОГО КУПЦА КАЛАШНИКОВА»', '«МЕДНЫЙ ВСАДНИК»', '«РУСЛАН И ЛЮДМИЛА»']

school_literature_for_lower = ['«ПОВЕСТЬ О ТОМ, КАК ОДИН МУЖИК ДВУХ ГЕНЕРАЛОВ ПРОКОРМИЛ»', '«ПРЕМУДРЫЙ ПИСКАРЬ»', '«ДИКИЙ ПОМЕЩИК»']

not_school_literature = ['«ПРОПАЛА СОВЕСТЬ»', '«МЕДВЕДЬ НА ВОЕВОДСТВЕ»', '«КОНЯГА»', '«САМООТВЕРЖЕННЫЙ ЗАЯЦ»', '«БОГАТЫРЬ»', '«ДУРАК»', '«ЛИБЕРАЛ»', '«КИСЕЛЬ»']

authors = ['Александр Пушкин', "Михаил Лермонтов", "Лев Толстой", "Денис Фонвизин", "Александр Блок", "Максим Горький",
           "Иван Бунин", "Иван Тургенев", "Федор Достоевский", "Антон Чехов", "Михаил Булгаков", "Николай Гоголь",
           "Михаил Салтыков-Щедрин"]

amount_of_starts = 0

# Импортируем нужные библиотеки и файлы (в нашем случае это библиотека книг, то есть их список и питоновские библиотеки random и telebot)
from books_list import list_of_all_books
import telebot
from telebot import types
import random

# сохраняем токен в переменную

token = "5249526378:AAH68cxVSnbBSFlfYmi0L0AJsW-G-gIkdj4"

bot = telebot.TeleBot(token)

# Блок запуска программы через команду /start + выбор первого действия

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)


    for button in main_menu_buttons:
        markup.add(types.KeyboardButton(button))

    bot.send_message(message.chat.id, 'Привет, <i>{0.first_name}</i>!✨ Я бот по подбору русской классической литературы!\n\n'
                                        'Я помогаю людям знакомиться с новой литературой и обращаю их внимание на не прочитанные в школьные годы книги. С чего начнем?'.format(message.from_user),
                    reply_markup=markup, parse_mode='HTML')

def start1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)


    for button in main_menu_buttons:
        markup.add(types.KeyboardButton(button))

    bot.send_message(message.chat.id, 'Что дальше?'.format(message.from_user),
                    reply_markup=markup, parse_mode='HTML')

# Блок самой программы

# Обработка выбора первого действия и переадрессация в соответсвии с выбором
@bot.message_handler(content_types=['text'])
def choose_how_to_search(message):

    list_choose_how_to_search = ['По автору 🖋', 'По годам ⏱', 'По жанру 📕']


    if message.text == 'Подобрать новую литературу 📚':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button0 in list_choose_how_to_search:
            markup.add(types.KeyboardButton(button0))

        printmessage = bot.send_message(message.chat.id, '{0.first_name}, каким способом будем подбирать новую литературу?\n\n'.format(message.from_user), reply_markup=markup)

        bot.register_next_step_handler(printmessage, choosing_way_in_each_ways)

    elif message.text == '🏫 Посмотреть не прочитанную школьную 📔':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button0 in school_searching:
            markup.add(types.KeyboardButton(button0))

        printmessage = bot.send_message(message.chat.id,
                                        '{0.first_name}, в каком классе вы филонили на литературе?\n\n'.format(
                                            message.from_user), reply_markup=markup)

        bot.register_next_step_handler(printmessage, which_class_you_want_to_search)

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button0 in main_menu_buttons:
            markup.add(types.KeyboardButton(button0))

        printmessage = bot.send_message(message.chat.id,
                                        '{0.first_name}, как-то мы не с того начали.\nДавайте попробуем ещё раз!'.format(
                                            message.from_user), reply_markup=markup)

        bot.register_next_step_handler(printmessage, choose_how_to_search)





#####################################################
# Блок с выбором "Посмотреть непрочитанную школьную"

# Обработка запроса класса
def which_class_you_want_to_search(message):
    if message.text == '1-5':

        bot.send_message(message.chat.id, f'В целом, ничего интересного вы не упустили.\nПочитайте литературу посерьезнее.\nНо если вам сильно хочется: '.format(message.from_user))

        for year_in_school in list_of_all_books:
            year_in_school = year_in_school.split('%')
            if 'СКАЗКА' in year_in_school[-1] and year_in_school[0] not in not_school_literature:
                bot.send_message(message.chat.id, f'Название: {year_in_school[0]} Автор: {year_in_school[1]} Год: {year_in_school[2]}\n---------------------------------------')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button2 in yesorexit:
            markup.add(types.KeyboardButton(button2))

        msd = bot.send_message(message.chat.id, 'Вернуться в меню?'.format(message.from_user),
                               reply_markup=markup)

        bot.register_next_step_handler(msd, end_question)
    elif message.text == '6-9':

        for schoolyearforsearching in list_of_all_books:

            schoolyearforsearching = schoolyearforsearching.split('%')
            if schoolyearforsearching[0] in school_literature_for_middle:

                str_for_sending_school = f'Название: {schoolyearforsearching[0]} Автор: {schoolyearforsearching[1]} Год: {schoolyearforsearching[2]}'
                list_for_sending_school.append(str_for_sending_school)

        if len(list_for_sending_school) <= 5:
            for schoolbooks_for_sending in list_for_sending_school:
                bot.send_message(message.chat.id,
                                 f'{schoolbooks_for_sending}\n---------------------------------------')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button2 in yesorexit:
                markup.add(types.KeyboardButton(button2))

            msd = bot.send_message(message.chat.id, 'Вернуться в меню?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, end_question)

        elif len(list_for_sending_school) > 5:

            having_schoolamount = len(list_for_sending_school)


            for schoolnumber in range(having_schoolamount):
                having_data_amount_school.append(schoolnumber)

            for random_schoolamount in range(1, 6):
                random_schoolnumber = random.choice(having_data_amount_school)
                having_data_amount_school.remove(random_schoolnumber)

                bot.send_message(message.chat.id, f'{list_for_sending_school[random_schoolnumber]}')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button3 in yesorno:
                markup.add(types.KeyboardButton(button3))

            msd = bot.send_message(message.chat.id, 'Ещё?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, cycle_for_middle_school)


    elif message.text == '10-11':

        for schoolyearforsearching in list_of_all_books:

            schoolyearforsearching = schoolyearforsearching.split('%')
            if schoolyearforsearching[0] in school_literature_for_high:
                str_for_sending_school = f'Название: {schoolyearforsearching[0]} Автор: {schoolyearforsearching[1]} Год: {schoolyearforsearching[2]}'
                list_for_sending_school.append(str_for_sending_school)

        if len(list_for_sending_school) <= 5:
            for schoolbooks_for_sending in list_for_sending_school:
                bot.send_message(message.chat.id,
                                 f'{schoolbooks_for_sending}\n---------------------------------------')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button2 in yesorexit:
                markup.add(types.KeyboardButton(button2))

            msd = bot.send_message(message.chat.id, 'Вернуться в меню?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, end_question)

        elif len(list_for_sending_school) > 5:

            having_schoolamount = len(list_for_sending_school)

            for schoolnumber in range(having_schoolamount):
                having_data_amount_school.append(schoolnumber)

            for random_schoolamount in range(1, 6):
                random_schoolnumber = random.choice(having_data_amount_school)
                having_data_amount_school.remove(random_schoolnumber)

                bot.send_message(message.chat.id, f'{list_for_sending_school[random_schoolnumber]}')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button3 in yesorno:
                markup.add(types.KeyboardButton(button3))

            msd = bot.send_message(message.chat.id, 'Ещё?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, cycle_for_high_school)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button2 in school_searching:
            markup.add(types.KeyboardButton(button2))

        msd = bot.send_message(message.chat.id,
                               'Введите данные, пожалуйста, кнопками:'.format(
                                   message.from_user), reply_markup=markup)
        bot.register_next_step_handler(msd, which_class_you_want_to_search)

# Цикл с ещё для старшей школы
def cycle_for_high_school(message):

    if message.text == 'Да!':

        if len(having_data_amount_school) > 5:

            for random_schoolamount in range(1, 6):
                random_schoolnumber = random.choice(having_data_amount_school)
                having_data_amount_school.remove(random_schoolnumber)

                bot.send_message(message.chat.id, f'{list_for_sending_school[random_schoolnumber]}')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button994 in yesorno:
                markup.add(types.KeyboardButton(button994))

            msd = bot.send_message(message.chat.id, 'Ещё?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, cycle_for_high_school)

        elif len(having_data_amount_school) <=5:

            for known_schoolnumbers in having_data_amount_school:

                bot.send_message(message.chat.id, f'{list_for_sending_school[known_schoolnumbers]}')

            list_for_sending_school.clear()
            having_data_amount_school.clear()

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button994 in yesorexit:
                markup.add(types.KeyboardButton(button994))

            msd = bot.send_message(message.chat.id, 'Больше школьных книг для этих классов нет!\nЕсли вы всё прочитали – вы молодец!\nВернуться в главное меню?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, end_question)

    elif message.text == 'Нет, достаточно':

        list_for_sending_school.clear()
        having_data_amount_school.clear()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button995 in yesorexit:
            markup.add(types.KeyboardButton(button995))
        msd = bot.send_message(message.chat.id, 'Вернуться в меню?'.format(message.from_user), reply_markup=markup)

        bot.register_next_step_handler(msd, end_question)

    else:

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button994 in yesorno:
            markup.add(types.KeyboardButton(button994))

        msd = bot.send_message(message.chat.id, 'Я – робот.\nПонимаю только язык команд...\nВведите запрос заново:'.format(message.from_user), reply_markup=markup)
        bot.register_next_step_handler(msd, cycle_for_high_school)

# Цикл с ещё для средней школы
def cycle_for_middle_school(message):


    if message.text == 'Да!':

        if len(having_data_amount_school) > 5:

            for random_schoolamount in range(1, 6):
                random_schoolnumber = random.choice(having_data_amount_school)
                having_data_amount_school.remove(random_schoolnumber)

                bot.send_message(message.chat.id, f'{list_for_sending_school[random_schoolnumber]}')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button995 in yesorno:
                markup.add(types.KeyboardButton(button995))

            msd = bot.send_message(message.chat.id, 'Ещё?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, cycle_for_middle_school)

        elif len(having_data_amount_school) <= 5:

            for known_schoolnumbers in having_data_amount_school:

                bot.send_message(message.chat.id, f'{list_for_sending_school[known_schoolnumbers]}')

            list_for_sending_school.clear()
            having_data_amount_school.clear()

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button995 in yesorexit:
                markup.add(types.KeyboardButton(button995))

            msd = bot.send_message(message.chat.id, 'Больше школьных книг для этих классов нет!\nЕсли вы всё прочитали – вы молодец!\nВернуться в главное меню?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, end_question)

    elif message.text == 'Нет, достаточно':

        list_for_sending_school.clear()
        having_data_amount_school.clear()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        list_for_sending_school.clear()
        having_data_amount_school.clear()

        for button995 in yesorexit:
            markup.add(types.KeyboardButton(button995))
        msd = bot.send_message(message.chat.id, 'Вернуться в меню?'.format(message.from_user), reply_markup=markup)

        bot.register_next_step_handler(msd, end_question)

    else:

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button995 in yesorno:
            markup.add(types.KeyboardButton(button995))

        msd = bot.send_message(message.chat.id, 'Я – робот.\nПонимаю только язык команд...\nВведите запрос заново:'.format(message.from_user), reply_markup=markup)
        bot.register_next_step_handler(msd, cycle_for_middle_school)

# Конец блока с выбором "Посмотреть непрочитанную школьную"
#####################################################





###############################################
# Блок с выбором "Подобрать новую литературу"

# Обработка запроса по типу и переадрессация
def choosing_way_in_each_ways(message):
    if message.text == 'По автору 🖋':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button1 in authors:
            markup.add(types.KeyboardButton(button1))

        msd = bot.send_message(message.chat.id, 'Укажите автора: '.format(message.from_user), reply_markup=markup)
        bot.register_next_step_handler(msd, finding_by_authors)

    elif message.text == 'По годам ⏱':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button1 in time_ways:
            markup.add(types.KeyboardButton(button1))

        msd = bot.send_message(message.chat.id, 'Смотреть по годам или векам? '.format(message.from_user), reply_markup=markup)
        bot.register_next_step_handler(msd, finding_by_time_of_book)

    elif message.text == 'По жанру 📕':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button1 in jounre_ways:
            markup.add(types.KeyboardButton(button1))

        msd = bot.send_message(message.chat.id, 'Какой род литературы вам ближе?'.format(message.from_user),
                               reply_markup=markup)
        bot.register_next_step_handler(msd, type_of_literature)

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button2 in list_choose_how_to_search:
            markup.add(types.KeyboardButton(button2))

        msd = bot.send_message(message.chat.id,
                               'Введите данные кнопками:\nТак ведь удобнее!'.format(
                                   message.from_user), reply_markup=markup)
        bot.register_next_step_handler(msd, choosing_way_in_each_ways)


######################################
# Все списки для перебора книг
list_for_sending_school = []
having_data_amount_school = []

list_for_sending = []
having_data_amount = []

list_for_sending_dramatype = []
having_data_amount_dramatype = []

list_for_sending_epos = []
having_data_amount_epos = []

list_for_sending_jounres = []
having_data_amount_jounres = []

list_for_sending_years = []
having_data_amount_years = []

year_amounts = []
#########################################



#########################################
# Поиск по авторам
def finding_by_authors(message):

    if message.text in authors:
        author = message.text
        author = author.upper()

        for authorforsearching in  list_of_all_books:

            authorforsearching = authorforsearching.split('%')
            if author in authorforsearching[1] and authorforsearching[0] not in school_literature_for_middle and authorforsearching[0] not in school_literature_for_high and authorforsearching[0] not in school_literature_for_lower:

                str_for_sending = f'Название: {authorforsearching[0]} Автор: {authorforsearching[1]} Год: {authorforsearching[2]}'
                list_for_sending.append(str_for_sending)

        if len(list_for_sending) <= 5:
            for books_for_sending in list_for_sending:
                bot.send_message(message.chat.id,
                                 f'{books_for_sending}\n---------------------------------------')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button3 in yesorexit:
                markup.add(types.KeyboardButton(button3))

            msd = bot.send_message(message.chat.id, 'Вернуться в меню?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, end_question)

        elif len(list_for_sending) > 5:

            having_amount = len(list_for_sending)


            for number in range(having_amount):
                having_data_amount.append(number)

            for random_amount in range(1, 6):
                random_number = random.choice(having_data_amount)
                having_data_amount.remove(random_number)

                bot.send_message(message.chat.id, f'{list_for_sending[random_number]}')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button3 in yesorno:
                markup.add(types.KeyboardButton(button3))

            msd = bot.send_message(message.chat.id, 'Ещё?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, cycle_for_authors)

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button997 in authors:
            markup.add(types.KeyboardButton(button997))

        msd = bot.send_message(message.chat.id,
                               'Я – робот.\nПонимаю только язык команд...\nВведите имя автора заново:'.format(
                                   message.from_user), reply_markup=markup)
        bot.register_next_step_handler(msd, finding_by_authors)


# Цикл для поиска по авторам
def cycle_for_authors(message):
    if message.text == 'Да!':

        if len(having_data_amount) > 5:

            for random_amount in range(1, 6):
                random_nuber = random.choice(having_data_amount)
                having_data_amount.remove(random_nuber)

                bot.send_message(message.chat.id, f'{list_for_sending[random_nuber]}')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button3 in yesorno:
                markup.add(types.KeyboardButton(button3))

            msd = bot.send_message(message.chat.id, 'Ещё?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, cycle_for_authors)

        elif len(having_data_amount) <= 5:

            for known_numbers in having_data_amount:

                bot.send_message(message.chat.id, f'{list_for_sending[known_numbers]}')


            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button3 in yesorexit:
                markup.add(types.KeyboardButton(button3))

            msd = bot.send_message(message.chat.id, 'Книг этого автора в нашей библиотеке больше нет :(\nВернуться в главное меню?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, end_question)

    elif message.text == 'Нет, достаточно':

        list_for_sending.clear()
        having_data_amount.clear()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button3 in yesorexit:
            markup.add(types.KeyboardButton(button3))
        msd = bot.send_message(message.chat.id, 'Вернуться в меню?'.format(message.from_user), reply_markup=markup)

        bot.register_next_step_handler(msd, end_question)


    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button997 in yesorno:
            markup.add(types.KeyboardButton(button997))

        msd = bot.send_message(message.chat.id,
                               'Я – робот.\nПонимаю только язык команд...\nВведите запрос заново:'.format(
                                   message.from_user), reply_markup=markup)
        bot.register_next_step_handler(msd, cycle_for_authors)
####################################






#####################################
# Поиск по времени

# Обработка запроса и переадрессация
def finding_by_time_of_book(message):
    if message.text == 'Век':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button5 in centuaries:
            markup.add(types.KeyboardButton(button5))

        msd = bot.send_message(message.chat.id, 'Какой век вам интересен?'.format(message.from_user),
                               reply_markup=markup)
        bot.register_next_step_handler(msd, finding_by_centuary)

    elif message.text == 'Год':

        markup = types.ReplyKeyboardRemove(selective=None)

        msd = bot.send_message(message.chat.id, 'Введите год вручную: '.format(message.from_user), reply_markup=markup)
        bot.register_next_step_handler(msd, year_finding)

    else:

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button5 in time_ways:
            markup.add(types.KeyboardButton(button5))

        msd = bot.send_message(message.chat.id, 'Так все же как будем искать?\nВведите запрос заново: '.format(message.from_user),
                               reply_markup=markup)
        bot.register_next_step_handler(msd, finding_by_time_of_book)

# Поиск по векам
def finding_by_centuary(message):
    if message.text == "XX":

        centuaryyy = '9'

        for yearsearchingin19 in list_of_all_books:

            yearsearchingin19 = yearsearchingin19.split('%')

            if centuaryyy in yearsearchingin19[2][1]:
                if yearsearchingin19[0] not in school_literature_for_high:
                    if yearsearchingin19[0] not in school_literature_for_middle:
                        if yearsearchingin19[-1] != 'СКАЗКА' or yearsearchingin19[0] in not_school_literature:
                            list_for_sending_years.append(
                                f'Название: {yearsearchingin19[0]} Автор: {yearsearchingin19[1]} Год: {yearsearchingin19[2]}')

        if len(list_for_sending_years) <= 5:
            for books_for_sending1 in list_for_sending_years:
                bot.send_message(message.chat.id,
                                 f'{books_for_sending1}\n---------------------------------------')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button5 in yesorexit:
                markup.add(types.KeyboardButton(button5))

            msd = bot.send_message(message.chat.id, 'Вернуться в меню?'.format(message.from_user),
                                   reply_markup=markup)
            bot.register_next_step_handler(msd, end_question)

        elif len(list_for_sending_years) > 5:

            having_amount_years = len(list_for_sending_years)

            for number1 in range(having_amount_years):
                having_data_amount_years.append(number1)

            for random_amount1 in range(1, 6):
                random_number1 = random.choice(having_data_amount_years)
                having_data_amount_years.remove(random_number1)

                bot.send_message(message.chat.id, f'{list_for_sending_years[random_number1]}')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button3 in yesorno:
                markup.add(types.KeyboardButton(button3))

            msd = bot.send_message(message.chat.id, 'Ещё?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, cycle_for_centuaries)

    elif message.text == 'XIX':

        centuaryyy = '8'

        for yearsearchingin19 in list_of_all_books:

            yearsearchingin19 = yearsearchingin19.split('%')

            if centuaryyy in yearsearchingin19[2][1]:
                if yearsearchingin19[0] not in school_literature_for_high:
                    if yearsearchingin19[0] not in school_literature_for_middle:
                        if yearsearchingin19[-1] != 'СКАЗКА' or yearsearchingin19[0] in not_school_literature:
                            list_for_sending_years.append(f'Название: {yearsearchingin19[0]} Автор: {yearsearchingin19[1]} Год: {yearsearchingin19[2]}')

        if len(list_for_sending_years) <= 5:
            for books_for_sending1 in list_for_sending_years:
                bot.send_message(message.chat.id, f'{books_for_sending1}\n---------------------------------------')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button5 in yesorexit:
                markup.add(types.KeyboardButton(button5))

            msd = bot.send_message(message.chat.id, 'Вернуться в меню?'.format(message.from_user),
                               reply_markup=markup)
            bot.register_next_step_handler(msd, end_question)

        elif len(list_for_sending_years) > 5:

            having_amount_years = len(list_for_sending_years)

            for number1 in range(having_amount_years):
                having_data_amount_years.append(number1)

            for random_amount1 in range(1, 6):
                random_number1 = random.choice(having_data_amount_years)
                having_data_amount_years.remove(random_number1)

                bot.send_message(message.chat.id, f'{list_for_sending_years[random_number1]}')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button3 in yesorno:
                markup.add(types.KeyboardButton(button3))

            msd = bot.send_message(message.chat.id, 'Ещё?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, cycle_for_centuaries)


    elif message.text == 'XVIII':

        centuaryyy = '7'

        for centuarypoisk in list_of_all_books:

            centuarypoisk = centuarypoisk.split('%')

            if centuaryyy in centuarypoisk[2][1]:
                list_for_sending_years.append(f'Название: {centuarypoisk[0]} Автор: {centuarypoisk[1]} Год: {centuarypoisk[2]}')

        if len(list_for_sending_years) <= 5:
            for books_for_sending1 in list_for_sending_years:
                bot.send_message(message.chat.id, f'{books_for_sending1}\n---------------------------------------')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button5 in yesorexit:
                markup.add(types.KeyboardButton(button5))

            msd = bot.send_message(message.chat.id, 'Вернуться в меню?'.format(message.from_user),
                               reply_markup=markup)
            bot.register_next_step_handler(msd, end_question)

    else:

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button9 in centuaries:
            markup.add(types.KeyboardButton(button9))

        msd = bot.send_message(message.chat.id, 'Литературы этого века в нашей библиотеке нет...\nВведите век заново: '.format(message.from_user),
                               reply_markup=markup)
        bot.register_next_step_handler(msd, finding_by_centuary)

# Цикл для поиска по векам
def cycle_for_centuaries(message):
    if message.text == 'Да!':

        if len(having_data_amount_years) > 5:

            for random_amount1 in range(1, 6):
                random_nuber1 = random.choice(having_data_amount_years)
                having_data_amount_years.remove(random_nuber1)

                bot.send_message(message.chat.id, f'{list_for_sending_years[random_nuber1]}')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button3 in yesorno:
                markup.add(types.KeyboardButton(button3))

            msd = bot.send_message(message.chat.id, 'Ещё?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, cycle_for_centuaries)

        elif len(having_data_amount_years) <= 5:

            for known_numbers1 in having_data_amount_years:
                bot.send_message(message.chat.id, f'{list_for_sending_years[known_numbers1]}')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button996 in yesorexit:
                markup.add(types.KeyboardButton(button996))

            msd = bot.send_message(message.chat.id,
                                   'Книг этого века в нашей библиотеке больше нет :(\nВернуться в главное меню?'.format(
                                       message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, end_question)


    elif message.text == 'Нет, достаточно':

        list_for_sending_years.clear()
        having_data_amount_years.clear()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button996 in yesorexit:
            markup.add(types.KeyboardButton(button996))

        msd = bot.send_message(message.chat.id, 'Вернуться в меню?'.format(message.from_user), reply_markup=markup)

        bot.register_next_step_handler(msd, end_question)

    else:

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button996 in yesorno:
            markup.add(types.KeyboardButton(button996))

        msd = bot.send_message(message.chat.id, 'Я – робот.\nПонимаю только язык команд...\nВведите запрос заново:'.format(message.from_user),
                               reply_markup=markup)
        bot.register_next_step_handler(msd, cycle_for_centuaries)

# Поиск по конкретному году
def year_finding(message):

    yearproblem = message.text
    if yearproblem[0] == '1' and yearproblem[1] in chisla and yearproblem[2] in chisla and yearproblem[3] in chisla and len(yearproblem) == 4:

        year = message.text
        for searchingyear in list_of_all_books:
            searchingyear = searchingyear.split('%')
            if year in searchingyear[2]:
                year_str = f'Название: {searchingyear[0]} Автор: {searchingyear[1]} Год: {searchingyear[2]}'
                year_amounts.append(year_str)

        if len(year_amounts) == 0:

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button15 in vernutsa:
                markup.add(types.KeyboardButton(button15))

            msd = bot.send_message(message.chat.id, 'Книг такого года в нашей биюлиотеке нет :(\nВведите год повторно или вернитесь в меню'.format(message.from_user),
                                   reply_markup=markup)
            bot.register_next_step_handler(msd, year_finding)

        elif len(year_amounts) > 0:

            for yearnumbers in year_amounts:

                bot.send_message(message.chat.id, f'{yearnumbers}\n---------------------------------------')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button15 in yesorexit:
                markup.add(types.KeyboardButton(button15))

            msd = bot.send_message(message.chat.id, 'Вернуться в меню?'.format(message.from_user),
                                   reply_markup=markup)
            bot.register_next_step_handler(msd, end_question)

            year_amounts.clear()

    elif message.text == 'Вернуться в меню':
        start1(message)


    else:

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        msd = bot.send_message(message.chat.id,
                               'Что-то пошло не так :(\nВведите год заново: '.format(
                                   message.from_user), reply_markup=markup)
        bot.register_next_step_handler(msd, year_finding)
######################################





#####################################
# Поиск по жанру

# Обработка запроса и переадрессация
def type_of_literature(message):
    if message.text == 'Эпос':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button5 in jounre_epos_types:
            markup.add(types.KeyboardButton(button5))

        msd = bot.send_message(message.chat.id, 'Выберете жанр: '.format(message.from_user),
                               reply_markup=markup)
        bot.register_next_step_handler(msd, jounres_of_epos)

    elif message.text == 'Драма':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button5 in jounre_drama_types:
            markup.add(types.KeyboardButton(button5))

        msd = bot.send_message(message.chat.id, 'Выберете жанр: '.format(message.from_user),
                               reply_markup=markup)
        bot.register_next_step_handler(msd, jounres_of_drama)

    elif message.text == 'Лирика':

        lyrica_as_way = message.text
        lyrica_as_way = lyrica_as_way.upper()

        for lyricasearching in list_of_all_books:
            lyricasearching = lyricasearching.split('%')

            if lyrica_as_way in lyricasearching[-2]:

                str_for_sending_lyrica = f'Название: {lyricasearching[0]} Автор: {lyricasearching[1]} Год: {lyricasearching[2]}'
                list_for_sending_jounres.append(str_for_sending_lyrica)

        if len(list_for_sending_jounres) <= 5:
            for books_for_sending_lyrica in list_for_sending_jounres:
                bot.send_message(message.chat.id,
                                 f'{books_for_sending_lyrica}\n---------------------------------------')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button7 in yesorexit:
                markup.add(types.KeyboardButton(button7))

            msd = bot.send_message(message.chat.id, 'Вернуться в меню?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, end_question)

        elif len(list_for_sending_jounres) > 5:

            having_amount_lyrica = len(list_for_sending_jounres)

            for number_lyrica in range(having_amount_lyrica):
                having_data_amount_jounres.append(number_lyrica)

            for random_amount_lyrica in range(1, 6):
                random_number_lyrica = random.choice(having_data_amount_jounres)
                having_data_amount_jounres.remove(random_number_lyrica)

                bot.send_message(message.chat.id, f'{list_for_sending_jounres[random_number_lyrica]}')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button7 in yesorno:
                markup.add(types.KeyboardButton(button7))

            msd = bot.send_message(message.chat.id, 'Ещё?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, cycle_for_lyrica)

    else:

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button7 in jounre_ways:
            markup.add(types.KeyboardButton(button7))

        msd = bot.send_message(message.chat.id, 'Такого рода литературы нет!\nВведите род заново: '.format(message.from_user),
                               reply_markup=markup)
        bot.register_next_step_handler(msd, type_of_literature)

# Цикл для Лирики
def cycle_for_lyrica(message):

    if message.text == 'Да!':

        if len(having_data_amount_jounres) > 5:

            for random_amount_lyrica in range(1, 6):
                random_number_lyrica = random.choice(having_data_amount_jounres)
                having_data_amount_jounres.remove(random_number_lyrica)

                bot.send_message(message.chat.id, f'{list_for_sending_jounres[random_number_lyrica]}')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button993 in yesorno:
                markup.add(types.KeyboardButton(button993))

            msd = bot.send_message(message.chat.id, 'Ещё?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, cycle_for_lyrica)

        elif len(having_data_amount_jounres) <=5:

            for known_lyricanumbers in having_data_amount_jounres:

                bot.send_message(message.chat.id, f'{list_for_sending_jounres[known_lyricanumbers]}')

            list_for_sending_jounres.clear()
            having_data_amount_jounres.clear()

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button993 in yesorexit:
                markup.add(types.KeyboardButton(button993))

            msd = bot.send_message(message.chat.id, 'Больше книг этого жанра в нашей библиотеке нет :(\nВернуться в главное меню?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, end_question)

    elif message.text == 'Нет, достаточно':

        list_for_sending_jounres.clear()
        having_data_amount_jounres.clear()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button993 in yesorexit:
            markup.add(types.KeyboardButton(button993))
        msd = bot.send_message(message.chat.id, 'Вернуться в меню?'.format(message.from_user), reply_markup=markup)

        bot.register_next_step_handler(msd, end_question)

    else:

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button993 in yesorno:
            markup.add(types.KeyboardButton(button993))

        msd = bot.send_message(message.chat.id, 'Я – робот.\nПонимаю только язык команд...\nВведите запрос заново:'.format(message.from_user),
                               reply_markup=markup)
        bot.register_next_step_handler(msd, cycle_for_lyrica)


# Поиск для Эпоса
def jounres_of_epos(message):

    if message.text == 'Роман':

        roman_as_way = message.text
        roman_as_way = roman_as_way.upper()

        for romansearching in list_of_all_books:
            romansearching = romansearching.split('%')

            if roman_as_way in romansearching[-1]:
                str_for_sending_roman = f'Название: {romansearching[0]} Автор: {romansearching[1]} Год: {romansearching[2]}'
                list_for_sending_epos.append(str_for_sending_roman)

        if len(list_for_sending_epos) <= 5:
            for books_for_sending_epos in list_for_sending_epos:
                bot.send_message(message.chat.id,
                                 f'{books_for_sending_epos}\n---------------------------------------')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button11 in yesorexit:
                markup.add(types.KeyboardButton(button11))

            msd = bot.send_message(message.chat.id, 'Вернуться в меню?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, end_question)

        elif len(list_for_sending_epos) > 5:

            having_amount_epos = len(list_for_sending_epos)

            for number_epos in range(having_amount_epos):
                having_data_amount_epos.append(number_epos)

            for random_amount_epos in range(1, 6):
                random_number_epos = random.choice(having_data_amount_epos)
                having_data_amount_epos.remove(random_number_epos)

                bot.send_message(message.chat.id, f'{list_for_sending_epos[random_number_epos]}')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button11 in yesorno:
                markup.add(types.KeyboardButton(button11))

            msd = bot.send_message(message.chat.id, 'Ещё?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, cycle_for_jounres_of_epos)

    elif message.text == 'Рассказ':

        roman_as_way = message.text
        roman_as_way = roman_as_way.upper()

        for romansearching in list_of_all_books:
            romansearching = romansearching.split('%')

            if roman_as_way in romansearching[-1]:
                str_for_sending_roman = f'Название: {romansearching[0]} Автор: {romansearching[1]} Год: {romansearching[2]}'
                list_for_sending_epos.append(str_for_sending_roman)

        if len(list_for_sending_epos) <= 5:
            for books_for_sending_epos in list_for_sending_epos:
                bot.send_message(message.chat.id,
                                 f'{books_for_sending_epos}\n---------------------------------------')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button11 in yesorexit:
                markup.add(types.KeyboardButton(button11))

            msd = bot.send_message(message.chat.id, 'Вернуться в меню?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, end_question)

        elif len(list_for_sending_epos) > 5:

            having_amount_epos = len(list_for_sending_epos)

            for number_epos in range(having_amount_epos):
                having_data_amount_epos.append(number_epos)

            for random_amount_epos in range(1, 6):
                random_number_epos = random.choice(having_data_amount_epos)
                having_data_amount_epos.remove(random_number_epos)

                bot.send_message(message.chat.id, f'{list_for_sending_epos[random_number_epos]}')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button11 in yesorno:
                markup.add(types.KeyboardButton(button11))

            msd = bot.send_message(message.chat.id, 'Ещё?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, cycle_for_jounres_of_epos)

    elif message.text == 'Повесть':

        povest_as_way = message.text
        povest_as_way = povest_as_way.upper()

        for povestsearching in list_of_all_books:
            povestsearching = povestsearching.split('%')

            if povest_as_way in povestsearching[-1]:
                str_for_sending_povest = f'Название: {povestsearching[0]} Автор: {povestsearching[1]} Год: {povestsearching[2]}'
                list_for_sending_epos.append(str_for_sending_povest)

        if len(list_for_sending_epos) <= 5:
            for books_for_sending_epos in list_for_sending_epos:
                bot.send_message(message.chat.id,
                                 f'{books_for_sending_epos}\n---------------------------------------')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button11 in yesorexit:
                markup.add(types.KeyboardButton(button11))

            msd = bot.send_message(message.chat.id, 'Вернуться в меню?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, end_question)

        elif len(list_for_sending_epos) > 5:

            having_amount_epos = len(list_for_sending_epos)

            for number_epos in range(having_amount_epos):
                having_data_amount_epos.append(number_epos)

            for random_amount_epos in range(1, 6):
                random_number_epos = random.choice(having_data_amount_epos)
                having_data_amount_epos.remove(random_number_epos)

                bot.send_message(message.chat.id, f'{list_for_sending_epos[random_number_epos]}')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button11 in yesorno:
                markup.add(types.KeyboardButton(button11))

            msd = bot.send_message(message.chat.id, 'Ещё?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, cycle_for_jounres_of_epos)

    elif message.text == 'Сказка':

        skazka_as_way = message.text
        skazka_as_way = skazka_as_way.upper()

        for skazkasearching in list_of_all_books:
            skazkasearching = skazkasearching.split('%')

            if skazka_as_way in skazkasearching[-1] and skazkasearching[0] in not_school_literature:
                str_for_sending_povest = f'Название: {skazkasearching[0]} Автор: {skazkasearching[1]} Год: {skazkasearching[2]}'
                list_for_sending_epos.append(str_for_sending_povest)

        if len(list_for_sending_epos) <= 5:
            for books_for_sending_epos in list_for_sending_epos:
                bot.send_message(message.chat.id,
                                 f'{books_for_sending_epos}\n---------------------------------------')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button11 in yesorexit:
                markup.add(types.KeyboardButton(button11))

            msd = bot.send_message(message.chat.id, 'Вернуться в меню?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, end_question)

        elif len(list_for_sending_epos) > 5:

            having_amount_epos = len(list_for_sending_epos)

            for number_epos in range(having_amount_epos):
                having_data_amount_epos.append(number_epos)

            for random_amount_epos in range(1, 6):
                random_number_epos = random.choice(having_data_amount_epos)
                having_data_amount_epos.remove(random_number_epos)

                bot.send_message(message.chat.id, f'{list_for_sending_epos[random_number_epos]}')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button11 in yesorno:
                markup.add(types.KeyboardButton(button11))

            msd = bot.send_message(message.chat.id, 'Ещё?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, cycle_for_jounres_of_epos)

    else:

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button11 in jounre_epos_types:
            markup.add(types.KeyboardButton(button11))

        msd = bot.send_message(message.chat.id, 'Такого жанра нет!\nВведите жанр заново: '.format(message.from_user),
                               reply_markup=markup)
        bot.register_next_step_handler(msd, jounres_of_epos)

# Цикл для Эпоса
def cycle_for_jounres_of_epos(message):

    if message.text == 'Да!':

        if len(having_data_amount_epos) > 5:

            for random_amount_epos in range(1, 6):
                random_number_epos = random.choice(having_data_amount_epos)
                having_data_amount_epos.remove(random_number_epos)

                bot.send_message(message.chat.id, f'{list_for_sending_epos[random_number_epos]}')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button992 in yesorno:
                markup.add(types.KeyboardButton(button992))

            msd = bot.send_message(message.chat.id, 'Ещё?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, cycle_for_jounres_of_epos)

        elif len(having_data_amount_epos) <= 5:

            for known_eposnumbers in having_data_amount_epos:

                bot.send_message(message.chat.id, f'{list_for_sending_epos[known_eposnumbers]}')

            list_for_sending_epos.clear()
            having_data_amount_epos.clear()

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button992 in yesorexit:
                markup.add(types.KeyboardButton(button992))

            msd = bot.send_message(message.chat.id, 'Больше книг этого жанра в нашей библиотеке нет :(\nВернуться в главное меню?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, end_question)

    elif message.text == 'Нет, достаточно':

        list_for_sending_epos.clear()
        having_data_amount_epos.clear()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button992 in yesorexit:
            markup.add(types.KeyboardButton(button992))
        msd = bot.send_message(message.chat.id, 'Вернуться в меню?'.format(message.from_user), reply_markup=markup)

        bot.register_next_step_handler(msd, end_question)

    else:

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button992 in yesorno:
            markup.add(types.KeyboardButton(button992))

        msd = bot.send_message(message.chat.id, 'Я – робот.\nПонимаю только язык команд...\nВведите запрос заново:'.format(message.from_user),
                               reply_markup=markup)
        bot.register_next_step_handler(msd, cycle_for_jounres_of_epos)


# Поиск для Драмы
def jounres_of_drama(message):

    if message.text == 'Драма':

        drama_as_way = message.text
        drama_as_way = drama_as_way.upper()

        for dramasearching in list_of_all_books:
            dramasearching = dramasearching.split('%')

            if drama_as_way in dramasearching[-1]:
                str_for_sending_drama = f'Название: {dramasearching[0]} Автор: {dramasearching[1]} Год: {dramasearching[2]}'
                list_for_sending_dramatype.append(str_for_sending_drama)

        if len(list_for_sending_dramatype) <= 5:
            for books_for_sending_drama in list_for_sending_dramatype:
                bot.send_message(message.chat.id,
                                 f'{books_for_sending_drama}\n---------------------------------------')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button13 in yesorexit:
                markup.add(types.KeyboardButton(button13))

            msd = bot.send_message(message.chat.id, 'Вернуться в меню?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, end_question)

        elif len(list_for_sending_dramatype) > 5:

            having_amount_drama = len(list_for_sending_dramatype)

            for number_drama in range(having_amount_drama):
                having_data_amount_dramatype.append(number_drama)

            for random_amount_drama in range(1, 6):
                random_number_drama = random.choice(having_data_amount_dramatype)
                having_data_amount_dramatype.remove(random_number_drama)

                bot.send_message(message.chat.id, f'{list_for_sending_dramatype[random_number_drama]}')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button13 in yesorno:
                markup.add(types.KeyboardButton(button13))

            msd = bot.send_message(message.chat.id, 'Ещё?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, cycle_for_jounres_of_drama)

    elif message.text == 'Комедия':

        komedy_as_way = message.text
        komedy_as_way = komedy_as_way.upper()

        for komedysearching in list_of_all_books:
            komedysearching = komedysearching.split('%')

            if komedy_as_way in komedysearching[-1]:
                str_for_sending_komedy = f'Название: {komedysearching[0]} Автор: {komedysearching[1]} Год: {komedysearching[2]}'
                list_for_sending_dramatype.append(str_for_sending_komedy)

        if len(list_for_sending_dramatype) <= 5:

            for books_for_sending_drama in list_for_sending_dramatype:
                bot.send_message(message.chat.id,
                                 f'{books_for_sending_drama}\n---------------------------------------')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button13 in yesorexit:
                markup.add(types.KeyboardButton(button13))

            msd = bot.send_message(message.chat.id, 'Вернуться в меню?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, end_question)

        elif len(list_for_sending_dramatype) > 5:

            having_amount_drama = len(list_for_sending_dramatype)

            for number_drama in range(having_amount_drama):
                having_data_amount_dramatype.append(number_drama)

            for random_amount_drama in range(1, 6):
                random_number_drama = random.choice(having_data_amount_dramatype)
                having_data_amount_dramatype.remove(random_number_drama)

                bot.send_message(message.chat.id, f'{list_for_sending_dramatype[random_number_drama]}')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button13 in yesorno:
                markup.add(types.KeyboardButton(button13))

            msd = bot.send_message(message.chat.id, 'Ещё?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, cycle_for_jounres_of_drama)

    else:

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button13 in jounre_drama_types:
            markup.add(types.KeyboardButton(button13))

        msd = bot.send_message(message.chat.id, 'Такого жанра нет!\nВведите жанр заново: '.format(message.from_user), reply_markup=markup)
        bot.register_next_step_handler(msd, jounres_of_drama)

# Цикл для драмы
def cycle_for_jounres_of_drama(message):

    if message.text == 'Да!':

        if len(having_data_amount_dramatype) > 5:

            for random_amount_drama in range(1, 6):
                random_number_drama = random.choice(having_data_amount_dramatype)
                having_data_amount_dramatype.remove(random_number_drama)

                bot.send_message(message.chat.id, f'{list_for_sending_dramatype[random_number_drama]}')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button991 in yesorno:
                markup.add(types.KeyboardButton(button991))

            msd = bot.send_message(message.chat.id, 'Ещё?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, cycle_for_jounres_of_drama)

        elif len(having_data_amount_dramatype) <=5:

            for known_dramanumbers in having_data_amount_dramatype:

                bot.send_message(message.chat.id, f'{list_for_sending_dramatype[known_dramanumbers]}')

            list_for_sending_dramatype.clear()
            having_data_amount_dramatype.clear()

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            for button991 in yesorexit:
                markup.add(types.KeyboardButton(button991))

            msd = bot.send_message(message.chat.id, 'Больше книг этого жанра в нашей библиотеке нет :(\nВернуться в главное меню?'.format(message.from_user),
                                   reply_markup=markup)

            bot.register_next_step_handler(msd, end_question)

    elif message.text == 'Нет, достаточно':

        list_for_sending_dramatype.clear()
        having_data_amount_dramatype.clear()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button991 in yesorexit:
            markup.add(types.KeyboardButton(button991))
        msd = bot.send_message(message.chat.id, 'Вернуться в меню?'.format(message.from_user), reply_markup=markup)

        bot.register_next_step_handler(msd, end_question)

    else:

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button991 in yesorno:
            markup.add(types.KeyboardButton(button991))

        msd = bot.send_message(message.chat.id, 'Я – робот.\nПонимаю только язык команд...\nВведите запрос заново:'.format(message.from_user), reply_markup=markup)
        bot.register_next_step_handler(msd, cycle_for_jounres_of_drama)
#######################################






# Завершающий вопрос: выход или продолжение работы
def end_question(message):
    if message.text == 'Да!':
        start1(message)

    elif message.text == 'Вернуться':
        start1(message)

    elif message.text == 'Нет, достаточно':
        bot.send_message(message.chat.id, 'Приятного чтения!'.format(message.from_user))

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button999 in commandstart:
            markup.add(types.KeyboardButton(button999))

        msd = bot.send_message(message.chat.id, 'Для дальнейшей работы нажмите «/start»'.format(message.from_user), reply_markup=markup)
        bot.register_next_step_handler(msd, the_repeated_start)

    elif message.text == 'Нет, пойду читать':

        bot.send_message(message.chat.id, 'Приятного чтения!'.format(message.from_user))

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button999 in commandstart:
            markup.add(types.KeyboardButton(button999))

        msd = bot.send_message(message.chat.id, 'Для дальнейшей работы нажмите «/start»'.format(message.from_user), reply_markup=markup)
        bot.register_next_step_handler(msd, the_repeated_start)

    else:

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button999 in yesorexit:
            markup.add(types.KeyboardButton(button999))

        msd = bot.send_message(message.chat.id, 'Я – робот.\nПонимаю только язык команд...\nВведите запрос заново:'.format(message.from_user), reply_markup=markup)
        bot.register_next_step_handler(msd, end_question)

# Функция ддя повторного старта
def the_repeated_start(message):
    if message.text == '/start':
        start1(message)

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for button998 in commandstart:
            markup.add(types.KeyboardButton(button998))

        msd = bot.send_message(message.chat.id,
                               'Я – робот.\nПонимаю только язык команд...\nВведите запрос заново:'.format(
                                   message.from_user), reply_markup=markup)
        bot.register_next_step_handler(msd, the_repeated_start)

# Функция для постоянного отслеживания сообщений пользователя
bot.polling(none_stop=True)