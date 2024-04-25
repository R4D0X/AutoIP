#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import colorama
import threading
import pygame
import sys
from tqdm import tqdm
from colorama import Fore, Back, Style
colorama.init()
os.system("clear")
os.system("toilet --metal R4D0X")
print(Style.BRIGHT + Fore.LIGHTCYAN_EX)
print("""
Bu araçla otomatik olarak IP Adres değiştirebilirsiniz, değeri saniye olarak girin.
""")
print(Fore.LIGHTRED_EX)
sure = input("IP Değişim Süre(saniye) : ")
os.system("clear")
os.system("anonsurf start")
os.system("clear")
print(Fore.LIGHTRED_EX)
print("Yeni IP Adres :")
print("-----------------------------")
os.system("curl icanhazip.com")
print(Fore.LIGHTRED_EX)
print("-----------------------------")
print(Style.RESET_ALL)
sure = int(sure)
k = input("Kapatmak için Q'ya basınız. ")
if( k == "q" ):
		print("Kapatılıyor.")
		os.system("anonsurf stop")
		quit()

while True: 
	time.sleep(sure)
	os.system("anonsurf restart")
	os.system("clear")
	print("Yeni IP Adres :")
	print("-----------------------------")
	os.system("curl icanhazip.com")
	print("-----------------------------")	
	k = input("Kapatmak için Q'ya basınız. ")
	if( k == "q" ):
    os.system("clear")
    print(Fore.LIGHTGREEN_EX)
		print("Kapatılıyor...")
		os.system("anonsurf stop")
		quit()
