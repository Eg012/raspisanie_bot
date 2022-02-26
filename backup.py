# # import random
# # import tkinter
# # from random import randint
# #
# # SCREEN_WIDTH = 500
# # BUTTON_WIDTH = 120
# #
# #
# # class MainFrame(tkinter.Frame):
# #     def __init__(self, root):
# #         super(MainFrame, self).__init__(root)
# #         self.root = root
# #         self.startUI()
# #         self.main_min = 0
# #         self.user_win = 0
# #         self.none = 0
# #         self.prog = 0
# #
# #     def startUI(self):
# #         center_button_x = SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2
# #         left_button_x = center_button_x - 10 - BUTTON_WIDTH
# #         btn2 = tkinter.Button(self.root, text="Ножницы", command=lambda x=2: self.click_btn(x))
# #         btn2.place(x=center_button_x, y=20, width=BUTTON_WIDTH, height=50)
# #         btn = tkinter.Button(self.root, text="Камень", command=lambda x=1: self.click_btn(x), font=("Rubik Beastly", 10))
# #         btn.place(x=left_button_x, y=20, width=BUTTON_WIDTH, height=50)
# #         btn3 = tkinter.Button(self.root, text="Бумага", command=lambda x=3: self.click_btn(x))
# #         btn3.place(x=center_button_x + 10 + BUTTON_WIDTH, y=20, width=BUTTON_WIDTH, height=50)
# #
# #         self.result_label = tkinter.Label(self.root, text='start game')
# #         self.result_label.place(x=left_button_x, y=100, width=BUTTON_WIDTH*3 + 10*2, height=70)
# #         self.win_label = tkinter.Label(self.root, text='win:')
# #         self.win_label.place(x=left_button_x, y=200, width=BUTTON_WIDTH*3 + 10*2, height=70)
# #         self.lose_label = tkinter.Label(self.root, text='lose')
# #         self.lose_label.place(x=left_button_x, y=300, width=BUTTON_WIDTH*3 + 10*2, height=70)
# #         self.none_label = tkinter.Label(self.root, text='none')
# #         self.none_label.place(x=left_button_x, y=400, width=BUTTON_WIDTH*3 + 10*2, height=70)
# #
# #     def click_btn(self, num):
# #         n = random.randint(1, 3)
# #         win = False
# #         if num == 1 and n == 2 or num == 2 and n == 3 or num == 3 and n == 1:
# #             win = True
# #             self.user_win += 1
# #         elif num == n:
# #             self.none += 1
# #             win = None
# #         else:
# #             self.main_min += 1edium spring green"
# #     root.geometry(f"{SCREEN_WIDTH}x600")
# #     root.resizable(False, False)
# #     app = MainFrame(root)
# #     app.pack()
# #     root.mainloop()
# # mas = [1, 2, 3, 4, 5, 6, 7]
# # x = int(input(">"))
# # if x in mas:
# #     print("win", x)
# # else:
# #     print("no", x)
# # for index in range(mas):
# #     pass
# #     _sum = 0
# #     left_right_sum = mas[0] + mas[-1]
# #     for index in range(len(mas)):
# #         if index % 2 > 0 and mas[index] > left_right_sum:
# #             _sum += mas[index]
# #     print(_sum)
# # n = int(input("n>"))
# # nums = list(range(2, n + 1))
# # mas = [2, 5, 6, 7, 2, 3, 4, 8, 9]
# #
# #         self.result_label.configure(text="result:win" if win else "result:none" if win is None else "result:lose")
# #         self.win_label.configure(text=f"user: {self.user_win},   prog: {self.main_min}")
# #         self.lose_label.configure(text=f"lose: {self.main_min}")
# #         self.none_label.configure(text=f"none: {self.none}")
# #
# #
# # if __name__ == '__main__':
# #     root = tkinter.Tk()
# #     root.title('KHБ')
# #     root["bg"] = "medium spring green"
# #     root.geometry(f"{SCREEN_WIDTH}x600")
# #     root.resizable(False, False)
# #     app = MainFrame(root)
# #     app.pack()
# #     root.mainloop()
# # mas = [1, 2, 3, 4, 5, 6, 7]
# # x = int(input(">"))
# # if x in mas:
# #     print("win", x)
# # else:
# #     print("no", x)
# # for index in range(mas):
# #     pass
# #     _sum = 0
# #     left_right_sum = mas[0] + mas[-1]
# #     for index in range(len(mas)):
# #         if index % 2 > 0 and mas[index] > left_right_sum:
# #             _sum += mas[index]
# #      print(_sum)
# # # n = int(input("n>"))
# # # nums = list(range(2, n + 1))
# # # mas = [2, 5, 6, 7, 2, 3, 4, 8, 9]
# # a = [1, 2, 3, 4, 7, 10]
# # vozrost = True
# # ubivaushii= True
# # for index in range(len(a) -1):
# #     if a[index] > a[index +1]:
# #         vozrost = False
# #     if a[index] < a[index +1]:
# #         ubivaushii = False
# #
# # if vozrost:
# #     print('vozrost')
# # elif ubivaushii:
# #     print('ubivaushii')
# a = [120, 10, 9, 8, 7, 6, 6, 6, 6, 9, 9, 9, 9, 9, 9, 77, 7, 7, 7]
# f = set(a)
# print(f)
# print(len(f))
# # f, a = a, f
# # print(type(f))
# # print(type(a))
# # print(f)
# # v = sorted(a)
# # print(v)
# # b = sorted(a, reverse=True)
# # print(b)
# # if a == v:
# #     print('vozros')
# # elif a == b:
# #     print('ne vozros')
from aiogram import Bot, types, Dispatcher, executor
#
# # Создаём переменную хронящую токет бота
# TOKEN = '5081083524:AAHgLEg2SCzabY8-H8dp5A9rMi8MEsio4D8'
#
# # Создание(инициализирование) переменных бота и диспетчера
# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)
#
#
# # Создание командв start
# @dp.message_handlers(['start'])
# async def process_command_start(message: types.Message):
#     await message.reply("Hi\n I'm SchoolBot")
#
#  # Этот обработчик будет вызван, когда пользователь отправит команду /start or /help
#
# # Создание команды help
# @dp.message_handlers(['help'])
# async def process_commad_start(message: types.Message):
#     await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")
#
#
# @dp.message_handlers()# обрабочик текстовых сообщений (Если вы хотите обрабатывать все текстовые сообщения в чате, оствьте обработчик без фильтров)
# async def school_Bot(message: types.Message):
#     await bot.send_message(message.from_user.id, message.text)
#
# if __name__ == '__main__':
#     executor.start_polling(dp)
#     #для того чтобы запустить проект нужно записать в кс python bot.py








#
# check_raspisaniay()