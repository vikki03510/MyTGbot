import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton
import math
import datetime
import random
from math import pi
import os

if not os.path.exists('logs'):
    os.makedirs('logs')

API_TOKEN = '6060090955:AAGEUr71c2HQWDhJo0NYurcJIw5rrSIDlI8'

bot = Bot(token=API_TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Створення клавіатури з предметами
subject_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
subject_keyboard.add(KeyboardButton('Математика'), KeyboardButton('Географія'))
subject_keyboard.add(KeyboardButton('Філологія'), KeyboardButton('Астрономія'))
subject_keyboard.add(KeyboardButton('Фізика'), KeyboardButton('Загальні питання'))
back_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
back_keyboard.add(KeyboardButton('Назад'))


# Клас для створення станів бота
class Subject(StatesGroup):
    subject = State()
    math_topic = State()
    geo_topic = State()
    phil_topic = State()
    astro_topic = State()
    phys_topic = State()
    main_menu = State()
    rock_paper_scissors = State()
    general_topic = State()
    amperes_law = State()
    vector = State()
    vector_next = State()

    @staticmethod
    def add_back_button(keyboard):
        keyboard.add("Назад")
        return keyboard


@dp.message_handler(Text(equals='Допомога'), state=Subject.geo_topic)
async def help_handler(message: types.Message):
    log_chat(message.chat.id, message.text)
    await message.answer(
        "Ви обрали предмет «Географія».\n" \
        "Оберіть тему яка вас цікавить.\n" \
        "Якщо ви хочете повернутись до вибору предмету натисніть «Назад».")
    log_chat(message.chat.id, message.text)


@dp.message_handler(Text(equals='Допомога'), state=Subject.math_topic)
async def help_handler1(message: types.Message):
    log_chat(message.chat.id, message.text)
    await message.answer(
        "Ви обрали предмет «Математика».\n" \
        "Оберіть тему яка вас цікавить.\n" \
        "Якщо ви хочете повернутись до вибору предмету натисніть «Назад».")
    log_chat(message.chat.id, message.text)


@dp.message_handler(Text(equals='Допомога'), state=Subject.phil_topic)
async def help_handler2(message: types.Message):
    log_chat(message.chat.id, message.text)
    await message.answer(
        "Ви обрали предмет «Філологія».\n" \
        "Оберіть тему яка вас цікавить.\n" \
        "Якщо ви хочете повернутись до вибору предмету натисніть «Назад».")
    log_chat(message.chat.id, message.text)


@dp.message_handler(Text(equals='Допомога'), state=Subject.astro_topic)
async def help_handler3(message: types.Message):
    log_chat(message.chat.id, message.text)
    await message.answer(
        "Ви обрали предмет «Астрономія».\n" \
        "Оберіть тему яка вас цікавить.\n" \
        "Якщо ви хочете повернутись до вибору предмету натисніть «Назад».")
    log_chat(message.chat.id, message.text)


@dp.message_handler(Text(equals='Допомога'), state=Subject.phys_topic)
async def help_handler4(message: types.Message):
    log_chat(message.chat.id, message.text)
    await message.answer(
        "Ви обрали предмет «Фізика».\n" \
        "Оберіть тему яка вас цікавить.\n" \
        "Якщо ви хочете повернутись до вибору предмету натисніть «Назад».")

    log_chat(message.chat.id, message.text)


@dp.message_handler(Text(equals='Допомога'), state=Subject.general_topic)
async def help_handler5(message: types.Message):
    log_chat(message.chat.id, message.text)
    await message.answer(
        "Ви обрали варіант «Загальне питання».\n" \
        "Оберіть тему яка вас цікавить.\n" \
        "Якщо ви хочете повернутись до вибору предмету натисніть «Назад».")
    log_chat(message.chat.id, message.text)


# Функція, що відправляє повідомлення з вибором предмета
@dp.message_handler(commands=['start'])
async def choose_subject(message: types.Message):
    log_chat(message.chat.id, message.text)
    await message.answer("Вітаю, мене звати Rubbi. Ви можете задати мені питання з наступних тем:", reply_markup=subject_keyboard)
    await Subject.subject.set()


def log_chat(chat_id, message):
    now = datetime.datetime.now()
    filename = f"logs/dialog-{chat_id}.txt"
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")
    except Exception as e:
        print(f"Error writing to log file {filename}: {e}")


# Функція, що відправляє повідомлення з вибором теми з математики
@dp.message_handler(Text(equals='Математика'), state=Subject.subject)
async def choose_math_topic(message: types.Message):
    log_chat(message.chat.id, message.text)
    math_topic_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    math_topic_keyboard.add(KeyboardButton('Формула розв\'язання квадратного рівняння'))
    math_topic_keyboard.add(KeyboardButton('Формула скалярного добутку векторів'))
    math_topic_keyboard.add(KeyboardButton('Площа кола'), KeyboardButton('Число π'))
    math_topic_keyboard.add(KeyboardButton('Допомога'))
    math_topic_keyboard.add(KeyboardButton('Назад'))
    await message.answer("Виберіть тему:", reply_markup=math_topic_keyboard)
    await Subject.math_topic.set()


@dp.message_handler(Text(equals='Географія'), state=Subject.subject)
async def choose_geo_topic(message: types.Message):
    log_chat(message.chat.id, message.text)
    geo_topic_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    geo_topic_keyboard.add(KeyboardButton('Яке найбільше озеро в світі за площею?'))
    geo_topic_keyboard.add(KeyboardButton('Де знаходиться Сахара - найбільша пустеля в світі?'))
    geo_topic_keyboard.add(KeyboardButton('Яке місто має найбільшу кількість населення в світі?'))
    geo_topic_keyboard.add(KeyboardButton('Знаходження координатів точки'))
    geo_topic_keyboard.add(KeyboardButton('Допомога'))
    geo_topic_keyboard.add(KeyboardButton('Назад'))
    await message.answer("Виберіть тему:", reply_markup=geo_topic_keyboard)
    await Subject.geo_topic.set()


@dp.message_handler(Text(equals='Філологія'), state=Subject.subject)
async def choose_philology_topic(message: types.Message):
    log_chat(message.chat.id, message.text)
    philology_topic_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    philology_topic_keyboard.add(KeyboardButton('Які часи є в англійській мові?'))
    philology_topic_keyboard.add(KeyboardButton('Як утворити Passive Voice в Present Simple?'))
    philology_topic_keyboard.add(KeyboardButton('Які роди іменників існують в українській мові?'))
    philology_topic_keyboard.add(KeyboardButton('Де використовується Past Simple в англійській мові?'))
    philology_topic_keyboard.add(KeyboardButton('Правила вживання неозначеного артикля a/an'))
    philology_topic_keyboard.add(KeyboardButton('У яких групах приголосних відбувається спрощення?'))
    philology_topic_keyboard.add(KeyboardButton('Винятки з правила про «спрощення в групах приголосних»'))
    philology_topic_keyboard.add(KeyboardButton('Допомога'))
    philology_topic_keyboard.add(KeyboardButton('Назад'))
    await message.answer("Виберіть тему:", reply_markup=philology_topic_keyboard)
    await Subject.phil_topic.set()


@dp.message_handler(Text(equals='Астрономія'), state=Subject.subject)
async def choose_astronomy_topic(message: types.Message):
    log_chat(message.chat.id, message.text)
    astronomy_topic_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    astronomy_topic_keyboard.add(KeyboardButton('Що таке космічне випромінювання?'))
    astronomy_topic_keyboard.add(KeyboardButton('Які планети Сонячної системи мають найбільші та найменші орбіти?'))
    astronomy_topic_keyboard.add(KeyboardButton('Скільки планет в Сонячній системі?'))
    astronomy_topic_keyboard.add(KeyboardButton('Що таке магнітна буря?'))
    astronomy_topic_keyboard.add(KeyboardButton('Допомога'))
    astronomy_topic_keyboard.add(KeyboardButton('Назад'))
    await message.answer("Виберіть тему:", reply_markup=astronomy_topic_keyboard)
    await Subject.astro_topic.set()


@dp.message_handler(Text(equals='Фізика'), state=Subject.subject)
async def choose_phys_topic(message: types.Message):
    log_chat(message.chat.id, message.text)
    phys_topic_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    phys_topic_keyboard.add(KeyboardButton('Обчислення індукції магнітного поля за формулою Ампера'))
    phys_topic_keyboard.add(KeyboardButton('Вивести гравітаційну сталу'))
    phys_topic_keyboard.add(KeyboardButton('Допомога'))
    phys_topic_keyboard.add(KeyboardButton('Назад'))
    await message.answer("Виберіть тему:", reply_markup=phys_topic_keyboard)
    await Subject.phys_topic.set()


@dp.message_handler(Text(equals='Загальні питання'), state=Subject.subject)
async def choose_general_topic(message: types.Message):
    log_chat(message.chat.id, message.text)
    general_topic_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    general_topic_keyboard.add(KeyboardButton('Який зараз рік?'))
    general_topic_keyboard.add(KeyboardButton('Скільки днів у ___ році?'))
    general_topic_keyboard.add(KeyboardButton('Пограти у камінь-ножиці-папір'))
    general_topic_keyboard.add(KeyboardButton('Зачитати вірш (рандомний вірш)'))
    general_topic_keyboard.add(KeyboardButton('Допомога'))
    general_topic_keyboard.add(KeyboardButton('Назад'))
    await message.answer("Виберіть тему:", reply_markup=general_topic_keyboard)
    await Subject.general_topic.set()


@dp.message_handler(Text(equals='Який зараз рік?'), state=Subject.general_topic)
async def current_year(message: types.Message):
    log_chat(message.chat.id, message.text)
    year = datetime.datetime.now().year
    await message.answer(f"Зараз {year} рік.")
    log_chat(message.chat.id, f"Зараз {year} рік.")


@dp.message_handler(Text(equals='Скільки днів у ___ році?'), state=Subject.general_topic)
async def days_in_year(message: types.Message):
    log_chat(message.chat.id, message.text)
    await message.answer("У якому році ви бажаєте дізнатись кількість днів?")
    await Subject.subject.next()
    log_chat(message.chat.id, "У якому році ви бажаєте дізнатись кількість днів?")


@dp.message_handler(lambda message: message.text.isdigit(), state=Subject.general_topic)
async def process_year_for_days(message: types.Message):
    log_chat(message.chat.id, message.text)
    year = int(message.text)
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days = 366
    else:
        days = 365
    await message.answer(f"У році {year} є {days} днів.")
    log_chat(message.chat.id, f"У році {year} є {days} днів.")


@dp.message_handler(Text(equals='Пограти у камінь-ножиці-папір'), state=Subject.general_topic)
async def rock_paper_scissors(message: types.Message):
    log_chat(message.chat.id, message.text)
    rps_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    rps_keyboard.add(KeyboardButton('Камінь'))
    rps_keyboard.add(KeyboardButton('Ножиці'))
    rps_keyboard.add(KeyboardButton('Папір'))
    rps_keyboard.add(KeyboardButton('Назад'))
    await message.answer("Оберіть свій вибір:", reply_markup=rps_keyboard)
    await Subject.rock_paper_scissors.set()


@dp.message_handler(lambda message: message.text in ['Камінь', 'Ножиці', 'Папір'], state=Subject.rock_paper_scissors)
async def process_rps_choice(message: types.Message):
    log_chat(message.chat.id, message.text)
    computer_choice = random.choice(['Камінь', 'Ножиці', 'Папір'])
    player_choice = message.text
    result = ''
    if player_choice == computer_choice:
        result = 'Нічия!'
    elif player_choice == 'Камінь':
        result = 'Ви виграли!' if computer_choice == 'Ножиці' else 'Комп’ютер виграв!'
    elif player_choice == 'Ножиці':
        result = 'Ви виграли!' if computer_choice == 'Папір' else 'Комп’ютер виграв!'
    else:  # player_choice == 'Папір'
        result = 'Ви виграли!' if computer_choice == 'Камінь' else 'Комп’ютер виграв!'
    await message.answer(f"Ви обрали: {player_choice}, комп’ютер обрав: {computer_choice}. {result}")
    log_chat(message.chat.id, f"Ви обрали: {player_choice}, комп’ютер обрав: {computer_choice}. {result}")


@dp.message_handler(Text(equals='Назад'), state=Subject.rock_paper_scissors)
async def back_to_general_topic(message: types.Message, state: FSMContext):
    log_chat(message.chat.id, message.text)
    await state.finish()
    await choose_general_topic(message)
    await state.set(None)


verses = [
    "Розкажу тобі думку тайну,\nдивний здогад мене обпік:\nя залишусь у серці твоєму\nна сьогодні, на завтра, навік.\nІ минатиме годину, нанизавши\nсотні ворожень, імен і країн, –\nна сьогодні, на завтра, назавжди! -\nти залишишся в серці моєму.\nА чому? То чудова теорема,\nна яку ти мене прирік.\nТо все разом, а ти – окремо.\nІ сьогодні, і завтра, і навік.\nЛіна Костенко",
    "Польові дзвіночки\nПіднімає джміль фіранку.\nКаже: — Доброго вам ранку!\nЯк вам, бджілко, ночувалось?\nЧи дощу не почувалось?\nВиглядає бджілка з хатки:\n— У дзвіночку добре спатки.\nЦей дзвіночок — як намет.\nТільки дощ як кулемет.\nЛіна Костенко",
    "Сонце гріє, вітер віє\nСонце гріє, вітер віє\nЗ поля на долину,\nНад водою гне з вербою\nЧервону калину,\nНа калині одиноке\nГніздечко гойдає.\nА де ж дівся соловейко?\nНе питай, не знає.",
    "Ти до мене прийшла не із казки чи сну,\nІ здалося мені, що стрічаю весну.\nТи явилась мені — і здалося, що світ\nПомолодшав навколо на тисячу літ.\nСкільки ніс я для тебе тривог і тепла.\nАле ти, як весна, стороною пройшла.\nВасиль Симоненко",
    "Надія(перша поезія Лесі Українки)\nНі долі, ні волі у мене нема,\nЗосталася тільки надія одна:\nНадія вернутись ще раз на Вкраїну,\nПоглянути ще раз на рідну країну,\nПоглянути ще раз на синій Дніпро, –\nТам жити чи вмерти, мені все одно;\nПоглянути ще раз на степ, могилки,\nВостаннє згадати палкії гадки…\nНі долі, ні волі у мене нема,\nЗосталася тільки надія одна."

]


@dp.message_handler(Text(equals='Зачитати вірш (рандомний вірш)'), state=Subject.general_topic)
async def read_random_verse(message: types.Message):
    log_chat(message.chat.id, message.text)
    # Генеруємо випадкове число від 1 до 5
    random_number = random.randint(1, 5)

    # Обираємо відповідний варіант вірша
    if random_number == 1:
        verse = verses[0]
    elif random_number == 2:
        verse = verses[1]
    elif random_number == 3:
        verse = verses[2]
    elif random_number == 4:
        verse = verses[3]
    else:
        verse = verses[4]

    # Відправляємо вірш користовачу
    await message.answer(verse)
    log_chat(message.chat.id, message.answer(verse))


# Функція, що повертає користувача в головне меню
@dp.message_handler(Text(equals='Назад'),
                    state=[Subject.math_topic, Subject.geo_topic, Subject.phil_topic, Subject.astro_topic,
                           Subject.phys_topic, Subject.general_topic])
async def back_to_main_menu(message: types.Message, state: FSMContext):
    log_chat(message.chat.id, message.text)
    await state.finish()
    await choose_subject(message)
    await state.set(None)


@dp.message_handler(Text(equals='Назад'))
async def go_back(message: types.Message):
    log_chat(message.chat.id, message.text)
    await message.answer("Оберіть предмет:", reply_markup=subject_keyboard)
    await Subject.subject.set()


# Функція, що обчислює корені квадратного рівняння
@dp.message_handler(Text(equals='Формула розв\'язання квадратного рівняння'), state=Subject.math_topic)
async def solve_quadratic_equation(message: types.Message, state: FSMContext):
    log_chat(message.chat.id, message.text)
    await state.finish()
    await message.answer("Введіть коефіцієнти a, b та c через пробіл:")
    await Subject.math_topic.set()
    log_chat(message.chat.id, "Введіть коефіцієнти a, b та c через пробіл:")


@dp.message_handler(lambda message: message.text.count(' ') == 2, state=Subject.math_topic)
async def process_quadratic_coefficients(message: types.Message, state: FSMContext):
    log_chat(message.chat.id, message.text)
    coefficients = message.text.split(' ')
    a = float(coefficients[0])
    b = float(coefficients[1])
    c = float(coefficients[2])
    D = b ** 2 - 4 * a * c
    if D < 0:
        await message.answer("Дискримінант менше 0, коренів немає")
        log_chat(message.chat.id, "Дискримінант менше 0, коренів немає")
    elif D == 0:
        x = -b / (2 * a)
        await message.answer(f"Один корінь: x = {x}")
        log_chat(message.chat.id, f"Один корінь: x = {x}")
    else:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        await message.answer(f"Два корені: x1 = {x1}, x2 = {x2}")
        log_chat(message.chat.id, f"Два корені: x1 = {x1}, x2 = {x2}")


@dp.message_handler(Text(equals='Формула скалярного добутку векторів'), state=Subject.math_topic)
async def scalar_product(message: types.Message, state: FSMContext):
    log_chat(message.chat.id, message.text)
    await state.finish()
    await message.answer("Введіть координати першого вектора через кому:")
    await Subject.vector.set()
    log_chat(message.chat.id, "Введіть координати першого вектора через кому:")


@dp.message_handler(lambda message: message.text.count(',') == 2, state=Subject.vector)
async def process_first_vector(message: types.Message, state: FSMContext):
    log_chat(message.chat.id, message.text)
    coordinates = message.text.split(',')
    x1 = float(coordinates[0])
    y1 = float(coordinates[1])
    z1 = float(coordinates[2])
    await message.answer("Введіть координати другого вектора через кому:")
    await Subject.vector_next.set()
    await state.update_data(vector1=[x1, y1, z1])
    log_chat(message.chat.id, "Введіть координати другого вектора через кому:")


@dp.message_handler(lambda message: message.text.count(',') == 2, state=Subject.vector_next)
async def process_second_vector(message: types.Message, state: FSMContext):
    log_chat(message.chat.id, message.text)
    coordinates = message.text.split(',')
    x2 = float(coordinates[0])
    y2 = float(coordinates[1])
    z2 = float(coordinates[2])
    data = await state.get_data()
    vector1 = data['vector1']
    scalar_product = vector1[0] * x2 + vector1[1] * y2 + vector1[2] * z2
    await message.answer(f"Скалярний добуток векторів: {scalar_product}")
    await state.finish()
    log_chat(message.chat.id, f"Скалярний добуток векторів: {scalar_product}")


@dp.message_handler(Text(equals='Площа кола'), state=Subject.math_topic)
async def circle_area(message: types.Message, state: FSMContext):
    log_chat(message.chat.id, message.text)
    await state.finish()
    await message.answer("Введіть радіус кола:")
    await Subject.math_topic.set()
    log_chat(message.chat.id, "Введіть радіус кола:")


@dp.message_handler(lambda message: message.text.isdigit(), state=Subject.math_topic)
async def process_circle_radius(message: types.Message, state: FSMContext):
    log_chat(message.chat.id, message.text)
    radius = int(message.text)
    area = math.pi * radius ** 2
    await message.answer(f"Площа кола: {area}")
    log_chat(message.chat.id, f"Площа кола: {area}")


@dp.message_handler(Text(equals='Число π'), state=Subject.math_topic)
async def output_pi(message: types.Message, state: FSMContext):
    log_chat(message.chat.id, message.text)
    await state.finish()
    await Subject.math_topic.set()
    await message.answer(f"Число π: {math.pi}")
    log_chat(message.chat.id, f"Число π: {math.pi}")


@dp.message_handler(Text(equals='Яке найбільше озеро в світі за площею?'), state=Subject.geo_topic)
async def largest_lake(message: types.Message):
    log_chat(message.chat.id, message.text)
    await message.answer(
        "Найбільше озеро світу за площею – Лох-Несс в Шотландії (площа – 56,4 км²). Але якщо врахувати, що Лох-Несс – прісноводне озеро, то тоді найдовшим озером світу за площею є Каспійське море (площа – 371 000 км²), яке не є настоящим морем, а є найбільшим за площею озером світу.")
    log_chat(message.chat.id,
             "Найбільше озеро світу за площею – Лох-Несс в Шотландії (площа – 56,4 км²). Але якщо врахувати, що Лох-Несс – прісноводне озеро, то тоді найдовшим озером світу за площею є Каспійське море (площа – 371 000 км²), яке не є настоящим морем, а є найбільшим за площею озером світу.")


@dp.message_handler(Text(equals='Де знаходиться Сахара - найбільша пустеля в світі?'), state=Subject.geo_topic)
async def sahara_location(message: types.Message):
    log_chat(message.chat.id, message.text)
    await message.answer("Сахара розташована в Північній Африці.")
    log_chat(message.chat.id, "Сахара розташована в Північній Африці.")


@dp.message_handler(Text(equals='Яке місто має найбільшу кількість населення в світі?'), state=Subject.geo_topic)
async def largest_city(message: types.Message):
    log_chat(message.chat.id, message.text)
    await message.answer("Місто Токіо, Японія, має найбільшу кількість населення в світі.")
    log_chat(message.chat.id, "Місто Токіо, Японія, має найбільшу кількість населення в світі.")


@dp.message_handler(Text(equals='Знаходження координатів точки'), state=Subject.geo_topic)
async def find_point_b(message: types.Message):
    log_chat(message.chat.id, message.text)
    await message.answer(
        "Знайти координати точки В (x2, y2), якщо відомо координати точки А (x1, y1) та відстань між ними (d) і напрямок (азимут) від точки А до точки В (θ).\n\nВведіть координати точки А через пробіл:")
    await Subject.subject.next()
    log_chat(message.chat.id,
             "Знайти координати точки В (x2, y2), якщо відомо координати точки А (x1, y1) та відстань між ними (d) і напрямок (азимут) від точки А до точки В (θ).\n\nВведіть координати точки А через пробіл:")


@dp.message_handler(lambda message: message.text.count(' ') == 1, state=Subject.geo_topic)
async def process_point_a(message: types.Message, state: FSMContext):
    log_chat(message.chat.id, message.text)
    coordinates = message.text.split(' ')
    x1 = float(coordinates[0])
    y1 = float(coordinates[1])
    await message.answer(
        "Введіть відстань між точками та напрямок від точки А до точки В через пробіл (відстань в км, напрямок в градусах за годинниковою стрілкою від північного напрямку):")
    await Subject.subject.next()
    await state.update_data(x1=x1, y1=y1)
    log_chat(message.chat.id,
             "Введіть відстань між точками та напрямок від точки А до точки В через пробіл (відстань в км, напрямок в градусах за годинниковою стрілкою від північного напрямку):")


@dp.message_handler(
    lambda message: message.text.count(' ') == 1 and message.text.split(' ')[0].isdigit() and message.text.split(' ')[
        1].isdigit(), state=Subject.geo_topic)
async def process_distance_and_direction(message: types.Message, state: FSMContext):
    log_chat(message.chat.id, message.text)
    distance, direction = message.text.split(' ')
    distance = float(distance)
    direction = float(direction)
    data = await state.get_data()
    x1 = data['x1']
    y1 = data['y1']
    # Конвертуємо напрямок в радіани
    angle = math.radians(direction)
    # Обчислюємо координати точки B
    x2 = x1 + distance * math.sin(angle)
    y2 = y1 + distance * math.cos(angle)
    await message.answer(f"Координати точки B: ({x2}, {y2})")
    log_chat(message.chat.id, f"Координати точки B: ({x2}, {y2})")


@dp.message_handler(Text(equals='Які часи є в англійській мові?'), state=Subject.phil_topic)
async def english_tenses(message: types.Message):
    log_chat(message.chat.id, message.text)
    await message.answer(
        "У англійській мові є такі часи: Present Simple, Present Continuous, Present Perfect, Present Perfect Continuous, Past Simple, Past Continuous, Past Perfect, Past Perfect Continuous, Future Simple, Future Continuous, Future Perfect, Future Perfect Continuous.")
    log_chat(message.chat.id,
             "У англійській мові є такі часи: Present Simple, Present Continuous, Present Perfect, Present Perfect Continuous, Past Simple, Past Continuous, Past Perfect, Past Perfect Continuous, Future Simple, Future Continuous, Future Perfect, Future Perfect Continuous.")


@dp.message_handler(Text(equals='Як утворити Passive Voice в Present Simple?'), state=Subject.phil_topic)
async def present_simple_passive(message: types.Message):
    log_chat(message.chat.id, message.text)
    await message.answer("Утворення Passive Voice в Present Simple: am/is/are + дієприкметник (3 форма дієслова).")
    log_chat(message.chat.id, "Утворення Passive Voice в Present Simple: am/is/are + дієприкметник (3 форма дієслова).")


@dp.message_handler(Text(equals='Які роди іменників існують в українській мові?'), state=Subject.phil_topic)
async def noun_genders(message: types.Message):
    log_chat(message.chat.id, message.text)
    await message.answer("Українська мова має три роди іменників: чоловічий, жіночий та середній.")
    log_chat(message.chat.id, "Українська мова має три роди іменників: чоловічий, жіночий та середній.")


@dp.message_handler(Text(equals='Де використовується Past Simple в англійській мові?'), state=Subject.phil_topic)
async def past_simple_usage(message: types.Message):
    log_chat(message.chat.id, message.text)
    await message.answer(
        "Past Simple (Past Indefinite) — це простий минулий час в англійській мові, який використовується для передачі інформації про певну подію або дію, яка відбулася у минулому. \nНайчастіше використовуємо в таких випадках:\n1)  Дія або подія трапилася в зазначений момент в минулому.\n2)  Минулі дії, які відбувалися один за одним.\n3)  Дія сталося в зазначений момент в минулому, але його вже не можна повторити, тому що у діяча більш немає такої можливості.")
    log_chat(message.chat.id,
             "Past Simple (Past Indefinite) — це простий минулий час в англійській мові, який використовується для передачі інформації про певну подію або дію, яка відбулася у минулому. \nНайчастіше використовуємо в таких випадках:\n1)  Дія або подія трапилася в зазначений момент в минулому.\n2)  Минулі дії, які відбувалися один за одним.\n3)  Дія сталося в зазначений момент в минулому, але його вже не можна повторити, тому що у діяча більш немає такої можливості.")


@dp.message_handler(Text(equals='Правила вживання неозначеного артикля a/an'), state=Subject.phil_topic)
async def indefinite_article_usage(message: types.Message):
    log_chat(message.chat.id, message.text)
    await message.answer(
        "Неозначений артикль a або an використовується з обчислювальними іменниками у формі однини. A / an – це частка, що утворилася від числівника one (один, єдиний) і означає, що цей предмет – один з множини подібних, такий же, як і інші предмети.\nАртикль a / an використовується, коли певний предмет згадується вперше і не виокремлюється з ряду інших подібних предметів.\nВибір артикля a або an залежить від звуку, яким починається наступне слово після артикля. A використовується перед приголосними звуками. An ставиться перед голосними звуками. Слід зазначити, що неважливо, з якої букви пишеться слово, важливо з якого звуку воно вимовляється.")
    log_chat(message.chat.id,
             "Неозначений артикль a або an використовується з обчислювальними іменниками у формі однини. A / an – це частка, що утворилася від числівника one (один, єдиний) і означає, що цей предмет – один з множини подібних, такий же, як і інші предмети.\nАртикль a / an використовується, коли певний предмет згадується вперше і не виокремлюється з ряду інших подібних предметів.\nВибір артикля a або an залежить від звуку, яким починається наступне слово після артикля. A використовується перед приголосними звуками. An ставиться перед голосними звуками. Слід зазначити, що неважливо, з якої букви пишеться слово, важливо з якого звуку воно вимовляється.")


@dp.message_handler(Text(equals='У яких групах приголосних відбувається спрощення?'), state=Subject.phil_topic)
async def consonant_simplification(message: types.Message):
    log_chat(message.chat.id, message.text)
    await message.answer(
        "У процесі словозміни чи словотворення інколи збігаються три й більше приголосних, що утруднює вимову. Тому в процесі мовлення один із приголосних (переважно середній) випадає і складна для вимови група приголосних спрощується. У групах приголосних -ждн-, -здн-, -стн-, -стл-, -скн-, -зкн- відбувається спрощення, тобто приголосні [д], [т] та [к]  випадають. ")
    log_chat(message.chat.id,
             "У процесі словозміни чи словотворення інколи збігаються три й більше приголосних, що утруднює вимову. Тому в процесі мовлення один із приголосних (переважно середній) випадає і складна для вимови група приголосних спрощується. У групах приголосних -ждн-, -здн-, -стн-, -стл-, -скн-, -зкн- відбувається спрощення, тобто приголосні [д], [т] та [к]  випадають. ")


@dp.message_handler(Text(equals='Винятки з правила про «спрощення в групах приголосних»'), state=Subject.phil_topic)
async def consonant_simplification_exceptions(message: types.Message):
    log_chat(message.chat.id, message.text)
    await message.answer(
        "Винятки з правила про спрощення в групах приголосних: кістлявий, пестливий, хвастливий, зап’ястний, хворостняк, шістнадцять, шістсот, шістдесят, компостний, контрастний, баластний, форпостний, аванпостний, випускний.")
    log_chat(message.chat.id,
             "Винятки з правила про спрощення в групах приголосних: кістлявий, пестливий, хвастливий, зап’ястний, хворостняк, шістнадцять, шістсот, шістдесят, компостний, контрастний, баластний, форпостний, аванпостний, випускний.")


@dp.message_handler(Text(equals='Що таке космічне випромінювання?'), state=Subject.astro_topic)
async def cosmic_radiation(message: types.Message):
    log_chat(message.chat.id, message.text)
    await message.answer(
        "Космічне випромінювання - це потік часток, що походять з космосу, таких як протони, нейтрони, електрони та інші. Воно може бути небезпечним для космонавтів та космічних апаратів.")
    log_chat(message.chat.id,
             "Космічне випромінювання - це потік часток, що походять з космосу, таких як протони, нейтрони, електрони та інші. Воно може бути небезпечним для космонавтів та космічних апаратів.")


@dp.message_handler(Text(equals='Які планети Сонячної системи мають найбільші та найменші орбіти?'),
                    state=Subject.astro_topic)
async def planets_orbits(message: types.Message):
    log_chat(message.chat.id, message.text)
    await message.answer("Найбільшу орбіту має Нептун, а найменшу - Меркурій.")
    log_chat(message.chat.id, "Найбільшу орбіту має Нептун, а найменшу - Меркурій.")


@dp.message_handler(Text(equals='Скільки планет в Сонячній системі?'), state=Subject.astro_topic)
async def planets_count(message: types.Message):
    log_chat(message.chat.id, message.text)
    await message.answer(
        "У Сонячній системі є вісім планет: Меркурій, Венера, Земля, Марс, Юпітер, Сатурн, Уран та Нептун.")
    log_chat(message.chat.id,
             "У Сонячній системі є вісім планет: Меркурій, Венера, Земля, Марс, Юпітер, Сатурн, Уран та Нептун.")


@dp.message_handler(Text(equals='Що таке магнітна буря?'), state=Subject.astro_topic)
async def magnetic_storm(message: types.Message):
    log_chat(message.chat.id, message.text)
    await message.answer(
        "Магнітна буря - це гостра зміна магнітного поля Землі, що може спричинити різноманітні наслідки, такі як збій в електропередачах, супутникових системах, радіозв'язку та інших електронних пристроях. Вона зазвичай виникає під час сонячних вибухів та інших подій на Сонці.")
    log_chat(message.chat.id,
             "Магнітна буря - це гостра зміна магнітного поля Землі, що може спричинити різноманітні наслідки, такі як збій в електропередачах, супутникових системах, радіозв'язку та інших електронних пристроях. Вона зазвичай виникає під час сонячних вибухів та інших подій на Сонці.")


@dp.message_handler(Text(equals='Обчислення індукції магнітного поля за формулою Ампера'), state=Subject.phys_topic)
async def amperes_law(message: types.Message):
    log_chat(message.chat.id, message.text)
    await message.answer(
        'Формула Ампера: B = (μ0 * I) / (2 * π * r), де B - індукція магнітного поля, μ0 - магнітна стала, I - сила струму, r - відстань до провідника. (Обчислити B)\n\nВведіть значення в формулу (μ0, I, r), через кому. Наприклад: 1e-7, 10, 0.05')
    await Subject.amperes_law.set()
    log_chat(message.chat.id,
             'Формула Ампера: B = (μ0 * I) / (2 * π * r), де B - індукція магнітного поля, μ0 - магнітна стала, I - сила струму, r - відстань до провідника. (Обчислити B)\n\nВведіть значення в формулу (μ0, I, r), через кому. Наприклад: 1e-7, 10, 0.05')


@dp.message_handler(state=Subject.amperes_law)
async def calculate_b_field(message: types.Message, state: FSMContext):
    log_chat(message.chat.id, message.text)
    values = message.text.split(',')
    if len(values) != 3:
        await message.answer('Неправильний формат вводу')
        log_chat(message.chat.id, 'Неправильний формат вводу')
        return
    try:
        mu, I, r = [float(value.strip()) for value in values]
        B = (mu * I) / (2 * pi * r)
        await message.answer(f'Значення індукції магнітного поля: {B:.2e} Тл')
        log_chat(message.chat.id, f'Значення індукції магнітного поля: {B:.2e} Тл')
        await state.finish()
    except ValueError:
        await message.answer('Неправильний формат вводу')
        log_chat(message.chat.id, 'Неправильний формат вводу')


@dp.message_handler(Text(equals='Вивести гравітаційну сталу'), state=Subject.phys_topic)
async def gravitational_constant(message: types.Message):
    log_chat(message.chat.id, message.text)
    G = 6.67430e-11
    await message.answer(f"Гравітаційна стала становить {G:.2e} м^3 / (кг * с^2)")
    log_chat(message.chat.id, f"Гравітаційна стала становить {G:.2e} м^3 / (кг * с^2)")


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)

