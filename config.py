TOKEN = '5081083524:AAHgLEg2SCzabY8-H8dp5A9rMi8MEsio4D8'
"""Шаблон написания бота"""
# import logging
# from aiogram import Bot, Dispatcher, executor, types
#
# # cоздаём переменную которая хронит токен бота
# TOKEN = '5081083524:AAHgLEg2SCzabY8-H8dp5A9rMi8MEsio4D8'
#
# logging.basicConfig(level=logging.INFO)
# #Создание(инициализирование) переменных бота и диспетчера
# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)
#
#
# # Создание оброботчика команд
# @dp.message_handlers(['start', 'help'])
# async def send_welcome(message: types.Message):
#     """ Этот обработчик будет вызван, когда пользователь отправит команду /start or /help """
#     await message.reply("Привет!\n I'm SchoolBot!\n")
#
# @dp.message_handlers()#оброботчик сообщений (Если вы хотите обрабатывать все текстовые сообщения в чате, оствьте обработчик без фильтров)
# async def schoolBot(message: types.Message):
#     #await bot.send_message(message.chat.id, message.text)
#     await  bot.send_message(message.chat.id, message.text)
#
#
# if __name__ = '__main__':
#     executor.start_polling(dp, skip_updates=True)
