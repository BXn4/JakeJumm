# ╦┌─┐┬┌─┌─┐ ╦┬ ┬┌┬┐┌┬┐
# ║├─┤├┴┐├┤  ║│ │││││││
#╚╝┴ ┴┴ ┴└─┘╚╝└─┘┴ ┴┴ ┴
#----------------------

import curses
from curses import wrapper
from curses.textpad import Textbox
import shutil
import string

def main(stdscr):
	space = " "
	spacek = ""
	fajlNeve = "ezegyfile1234567.py"
	fajlKiterjesztes = ""
	hosszuFajlNev = False
	vanFajlKiterjesztes = False
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
	stdscr.addstr(0 , 0, "1 ")
	stdscr.refresh()
	stdscr.getch()

wrapper(main)