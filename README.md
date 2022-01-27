# Brute_force_password-cracker
-------Created By Justpowercoding10785-------
This program was created in python using Visual Studio Code . 
Source code of the program will be pasted here . 
You are free to distrubute and reproduce this program in the following conditions :- 
$ You should mention who the original author was ( Me - Justpowercoding10785 ) . 
$ You are also free to add code to contribute and make this project better . 
$ You can also mention the areas you added your own code . 
$ This program is free and shouldn't be sold as a paid software . 
-------Thank you for you Co-operation-------

-------Source Code-------
# Created By Justpowercoding10785
import random
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
