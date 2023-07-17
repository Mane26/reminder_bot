from datetime import datetime
import logging
import threading

import config
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


logging.basicConfig(level=logging.INFO)

# Создаем объект бота и передаем ему токен нашего бота
bot = Bot(token=config.TELEGRAM_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_message(message):
# Отправляем сообщение пользователю
    kb = [
        [
            types.KeyboardButton(text="Выполнено"),
            types.KeyboardButton(text="Не выполнено")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите выполнение"
    )
    await bot.send_message(message.chat.id, 'Привет! Я бот-напоминалка. Чтобы создать напоминание, введите /reminder.')
    await message.answer("Напоминание сотруднику?", reply_markup=keyboard)

# Обработчик команды /reminder
@dp.message_handler(commands=['reminder'])
async def reminder_message(message):
# Запрашиваем у пользователя название напоминания и дату и время напоминания
    await bot.send_message(message.chat.id, 'Запись на массаж:')
    await bot.register_next_step_handler(message, set_reminder_name)


# Функция, которую вызывает обработчик команды /reminder для установки названия напоминания
async def set_reminder_name(message):
    user_data = {}
    user_data[message.chat.id] = {'reminder_name': message.text}
    await bot.send_message(message.chat.id, '2023-07-18 10:10:20.')
    await bot.register_next_step_handler(message, reminder_set, user_data)


# Функция, которую вызывает обработчик команды /reminder для установки напоминания
async def reminder_set(message, user_data):
    try:
        # Преобразуем введенную пользователем дату и время в формат datetime
        reminder_time = datetime.datetime.strptime(message.text, '%Y-%m-%d %H:%M:%S')
        now = datetime.datetime.now()
        delta = reminder_time - now
        # Если введенная пользователем дата и время уже прошли, выводим сообщение об ошибке
        if delta.total_seconds() <= 0:
            bot.send_message(message.chat.id, 'Вы ввели прошедшую дату, попробуйте еще раз.')
        # Если пользователь ввел корректную дату и время, устанавливаем напоминание и запускаем таймер
        else:
            reminder_name = user_data[message.chat.id]['reminder_name']
            await bot.send_message(message.chat.id, 'Напоминание "{}" установлено на {}.'.format(reminder_name, reminder_time))
            reminder_timer = threading.Timer(delta.total_seconds(), send_reminder, [message.CHAT_ID, reminder_name])
            reminder_timer.start()
        # Если пользователь ввел некорректную дату и время, выводим сообщение об ошибке
    except ValueError:
        await bot.send_message(message.chat.id, 'Вы ввели неверный формат даты и времени, попробуйте еще раз.')

# Функция, которая отправляет напоминание пользователю
async def send_reminder(TELEGRAM_CHAT_ID, reminder_name):
    await bot.send_message(TELEGRAM_CHAT_ID, 'Время получить ваше напоминание "{}"!'.format(reminder_name))



# Запускаем бота
if __name__ == '__main__':
    executor.start_polling(dp)