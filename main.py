# noinspection PyUnresolvedReferences
import random
# noinspection PyUnresolvedReferences
import string

import pyautogui

chars = "abcdefghijklmnopqrstuvwxyz0123456789"
chars_list = list(chars)

print("A program by BOSSTECH , Please read the readme.txt file for copyright info and other stuff :) ")
password = pyautogui.password("Enter a password : ")

guess_password = ""

while guess_password != password:
    guess_password = random.choices(chars_list, k=len(password))

    print("<==================" + str(guess_password) + "==================>")

    if guess_password == list(password):
        print("Your password is : " + "".join(guess_password))
        break