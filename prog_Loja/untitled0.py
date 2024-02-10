# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 23:32:45 2023

@author: S_Ronaldh
"""

import requests
import tkinter as tk

cot_dol = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

print(cot_dol)

janela = tk.Tk()

janela.title("Loja")

texto_orientação = tk.Label(janela, text="Clique no botão para ver as cotações!")
texto_orientação.grid(column=5, row=5)

janela.mainloop()