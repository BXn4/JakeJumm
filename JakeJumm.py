# ╦┌─┐┬┌─┌─┐ ╦┬ ┬┌┬┐┌┬┐
# ║├─┤├┴┐├┤  ║│ │││││││
#╚╝┴ ┴┴ ┴└─┘╚╝└─┘┴ ┴┴ ┴
#----------------------

import curses
from curses import wrapper
from curses.textpad import Textbox
import shutil
import string
import sys
import chardet

fajlNeve = ""
szoveg = []

def main(stdscr):
	global fajlNeve
	space = " "
	spacek = ""
	fajlKiterjesztes = ""
	hosszuFajlNev = False
	vanFajlKiterjesztes = False
	if fajlNeve:
		try:
			fajl = fajlNeve.rsplit('.', 1)
			vanFajlKiterjesztes = True
			fajlKiterjesztes = "." + fajl[1]
			fajlNeve = fajl[0][:15]
			if len(fajl[0]) > 15:
				hosszuFajlNev = True
		except:
			if len(fajlNeve) > 15:
				hosszuFajlNev = True
			fajlNeve = fajlNeve[:15]
	console_Y = shutil.get_terminal_size().lines
	console_X = shutil.get_terminal_size().columns
	console_C = int(console_X / 2)
	hossz = console_X // len(space) - 5
	for i in range(console_X // 1):
		spacek = space * hossz
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
	menubar = curses.color_pair(1)
	stdscr.refresh()
	stdscr.keypad(True)
	stdscr.clear()
	stdscr.addstr(console_Y - 1 , 0, "Menu{}".format(spacek), menubar)
	stdscr.addstr(console_Y - 1 , 5, "|", menubar)
	stdscr.addstr(console_Y - 1 , 7, "ln(1:0)", menubar)
	if hosszuFajlNev == True:
		stdscr.addstr(console_Y - 1 , console_C, "{}..".format(fajlNeve) + "{}".format(fajlKiterjesztes), menubar)
	else:
		stdscr.addstr(console_Y - 1 , console_C, "{}".format(fajlNeve) + "{}".format(fajlKiterjesztes), menubar)
	for i, sorok in enumerate(szoveg):
		stdscr.addstr(i , 0, "{} ".format(i))
		stdscr.addstr(i, 2, sorok)
	stdscr.refresh()
	stdscr.getch()

if len(sys.argv) < 2:
    fajlNeve = "NewFile"
else:
    fajlNeve = sys.argv[1]
    try:
    	with open(fajlNeve, "rb") as olvas:
    		szoveg = olvas.read(8192)
    		eredmeny = chardet.detect(szoveg)
    		kodolas = eredmeny['encoding']
    	with open(fajlNeve, encoding=kodolas) as olvas:
    		szoveg = [sorok.strip() for sorok in olvas]
    except (FileNotFoundError):
    	pass
wrapper(main)
