'''
 # @ Author: Mauricio Menezes
 # @ Email: mauriciosm95@gmail.com
 # @ GitHub: https://github.com/mau-me
 # @ Create Time: 2023-04-11 20:13:58
 # @ Description: Programa para armazenamento de senhas de forma centralizada.
 '''

#! /usr/bin/python3

SENHAS = {
    'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
    'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
    'homepage': 'lsdflkjlASJDKjasfhaskfhaiuqry'
}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('Use: python repo_senhas.py[conta] - Copia a senha da conta')
    sys.exit()

conta = sys.argv[1]

if conta not in SENHAS:
  print('Senha não cadastrada para a conta ' + conta)
  sys.exit()

pyperclip.copy(SENHAS[conta])

print('Senha copiada com sucesso')