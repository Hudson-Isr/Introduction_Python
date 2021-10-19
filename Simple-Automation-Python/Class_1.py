import pyautogui as pa
import pyperclip as pp
import pandas as pd
import time
import numpy
import openpyxl
import datetime as dt

hora = dt.datetime()


tabela = pd.read_excel (r"C:\Users\Hudson Israel\Downloads\Vendas - Dez.xlsx")

Faturamento = tabela["Valor Final"].sum()

Quantidade = tabela["Quantidade"].sum()

# Abertura do programa
pa.press("win")
time.sleep(3)
pa.write("google chrome")
pa.press("enter") 

# Seleção da aba
time.sleep(3)
pa.click(x=2014, y=450, clicks=2)
time.sleep(3)
pa.hotkey("ctrl", "t")  
pp.copy("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
pa.hotkey("ctrl","v")
pa.press("enter")
time.sleep(8)
pa.click(x=92, y=201, clicks=2)
time.sleep(10)

# Escrevendo um e-mail
pa.write("hudson.israel716@gmail.com")
pa.PAUSE = 2
pa.press("tab")
pa.press("tab")
pa.write("teste")
pa.press("tab")
texto = f"""olá, este é o teste para saber a quantidade {Quantidade:,.2f} e o {Faturamento:,.2f}""" #f antes do """ trás o valor da variavel dentro das CHAVES {}
pp.copy(texto)
pa.hotkey("ctrl","v")
pa.hotkey("ctrl", "enter")









