'''
 # @ Author: Mauricio Menezes
 # @ Email: mauriciosm95@gmail.com
 # @ Github: https://github.com/mau-me
 # @ Create Time: 2023-04-18 19:29:15
 # @ Description: Obtém um texto do clipboard,
 '''

import pyperclip

text = pyperclip.paste()

lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

newText = ('\n').join(lines)

print(newText)

pyperclip.copy(text)