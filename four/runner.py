import sys, os
from msvcrt import getch
from operator import add, sub, mul, truediv


def putc(value):
	if not isinstance(value, str):
		value = chr(value)
	sys.stdout.write(value)
	sys.stdout.flush()

def getc():
	return ord(sys.stdin.read(1))

def exit(exit_code):
	os._exit(exit_code)

grid = [0] * 100

