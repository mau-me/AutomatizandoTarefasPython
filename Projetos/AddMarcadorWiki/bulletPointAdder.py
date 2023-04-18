'''
 # @ Author: Mauricio Menezes
 # @ Email: mauriciosm95@gmail.com
 # @ Github: https://github.com/mau-me
 # @ Create Time: 2023-04-18 19:29:15
 # @ Description: Obtém um texto do clipboard,
 '''

import pyperclip

text = pyperclip.paste()

# TODO: Separar as linhas e acrescentar asteriscos

print(text)

pyperclip.copy(text)