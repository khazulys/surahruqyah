#!/bin/usr/python

import os, sys
from time import sleep

def banner():
	try:
		os.system('cls' if os.name =='nt' else 'clear')
		print ("\033[1;33m  	  ╔═╗┬ ┬┬─┐┌─┐┬ ┬")
		print ("\033[1;34m  	  ╚═╗│ │├┬┘├─┤├─┤")
		print ("\033[1;35m  	  ╚═╝└─┘┴└─┴ ┴┴ ┴")
		print ("\033[1;35m	╦═╗┬ ┬┌─┐ ┬ ┬┌─┐┬ ┬")
		print ("\033[1;34m	╠╦╝│ ││─┼┐└┬┘├─┤├─┤")
		print ("\033[1;33m	╩╚═└─┘└─┘└ ┴ ┴ ┴┴ ┴")
		print ("\033[1;31m    We must be remember Allah ")
	except KeyboardInterrupt:
		print ("\033[1;31m[×]\033[1;32m Selamat membaca kembali, semoga hal tadi bermanfaat ")
banner()

def menu():
	try:
		print ("\n\033[1;31m[√]\033[1;34m Pilihan surah tersedia dibawah:")
		print ("\n\033[1;32m[01]\033[1;36m Surah Al-Fatihah ")
		print ("\033[1;32m[02]\033[1;36m Surah Yasin ")
		print ("\033[1;32m[03]\033[1;36m Surah Al-Baqarah ")
		print ("\033[1;32m[04]\033[1;36m Surah Al-Falaq ")
		print ("\033[1;32m[05]\033[1;36m Surah An-Nass ")
		pilih = str(input("\n\033[1;31m[+]\033[1;35m Pilih mau baca yang mana: "))
		if pilih == "1" or pilih == "01":
			os.system('cls' if os.name == 'nt' else 'clear')
			print ("\033[1;31m  ╔═╗┬   ╔═╗┌─┐┌┬┐┬┬ ┬┌─┐┬ ┬ ")
			print ("\033[1;33m  ╠═╣│───╠╣ ├─┤ │ │├─┤├─┤├─┤ ")
			print ("\033[1;35m  ╩ ╩┴─┘ ╚  ┴ ┴ ┴ ┴┴ ┴┴ ┴┴ ┴ ")

			print ("\033[1;36m[*]\033[1;35m Membuka Al-Qur'an dalam 10 detik...")
			sleep(0.10)
			os.system("termux-open https://litequran.net/al-fatihah")
		elif pilih == "2" or pilih == "02":
			os.system('cls' if os.name =='nt' else 'clear')
			print ("\033[1;32m	╦ ╦┌─┐┌─┐┬┌┐┌ ")
			print ("\033[1;33m	╚╦╝├─┤└─┐││││ ")
			print ("\033[1;31m	 ╩ ┴ ┴└─┘┴┘└┘ ")

			print ("\033[1;36m[*]\033[1;35m Membuka Al-Qur'an dalam 10 detik..")
			sleep(0.10)
			os.system("termux-open https://litequran.net/yasin")
		elif pilih == "3" or pilih == "03":
			os.system('cls' if os.name=='nt' else 'clear')
			print ("\033[1;36m	╔═╗┬   ╔╗ ┌─┐┌─┐ ┌─┐┬─┐┌─┐┬ ┬ ")
			print ("\033[1;37m	╠═╣│───╠╩╗├─┤│─┼┐├─┤├┬┘├─┤├─┤ ")
			print ("\033[1;34m	╩ ╩┴─┘ ╚═╝┴ ┴└─┘└┴ ┴┴└─┴ ┴┴ ┴ ")

			print ("\033[1;36m[*]\033[1;35m Membuka Al-Qur'an dalam 10 detik..")
			sleep(0.10)
			os.system("termux-open https://litequran.net/al-baqarah")
		elif pilih == "4" or pilih == "04":
			os.system('cls' if os.name == 'nt' else 'clear')
			print ("\033[1;31m	╔═╗┬   ╔═╗┌─┐┬  ┌─┐┌─┐ ")
			print ("\033[1;33m	╠═╣│───╠╣ ├─┤│  ├─┤│─┼┐ ")
			print ("\033[1;30m	╩ ╩┴─┘ ╚  ┴ ┴┴─┘┴ ┴└─┘└ ")

			print ("\033[1;36m[*]\033[1;35m Membuka Al-Qur'an dalam 10 detik..")
			os.system("termux-open https://litequran.net/al-falaq")
		elif pilih == "5" or pilih == "05":
			os.system('cls' if os.name == 'nt' else 'clear')
			print ("\033[1;30m	╔═╗┬   ╔╗╔┌─┐┌─┐┌─┐ ")
			print ("\033[1;31m	╠═╣│───║║║├─┤└─┐└─┐ ")
			print ("\033[1;32m	╩ ╩┴─┘ ╝╚╝┴ ┴└─┘└─┘ ")

			print ("\033[1;36m[*]\033[1;35m Membuka Al-Qur'an dalam 10 detik.. ")
			os.system("termux-open https://litequran.net/an-nas")
		else:
			sys.exit("[×] Pilihan tidak tersedia ")

	except KeyboardInterrupt:
		print ("\033[1;31m[+]\033[1;32m Goodbye. semoga bermanfaat..")
menu()
