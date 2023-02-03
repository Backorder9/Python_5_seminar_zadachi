'''
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит заданное количество конфет.
Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются
сделавшему последний ход.
a) Добавьте игру против бота
b) Подумайте как наделить бота 'интеллектом'
'''

from random import randint as ri
total_candies = 180
take_candy = 0
player1_candy = 0
bot_candy = 0
def dice_cast():
    random_number = ri(1,2)
    if random_number == 1:
        player1_turn()
    else: print("Игру начинает бот!")
    bot_turn()

def player1_turn():
    global total_candies
    global take_candy
    global player1_candy
    print(f'Игрок 1, ваш ход, сейчас на столе - {total_candies} конфет')
    take_candy = int(input("Сколько конфет Вы хотите взять? Берите не более 28."))
    while take_candy > 28 or take_candy < 0 or take_candy > total_candies:
        take_candy = int(input("Вы берёте слишком много конфет! Играйте по правилам! Возьмите снова:"))
    total_candies -= take_candy
    player1_candy += take_candy
    if total_candies > 0:
        bot_turn()
    else: print("Игрок 1, Вы победили!")


def bot_turn():
    global total_candies
    global take_candy
    global bot_candy
    take_candy = total_candies % 29 if total_candies % 29 != 0 else ri(1, 28)
    total_candies -= take_candy
    bot_candy += take_candy
    print(f"Бот взял {take_candy} конфет. На столе осталось {total_candies} конфет.")
    if total_candies > 0:
        player1_turn()
    else: print("Бот победил!")
    exit()

dice_cast()