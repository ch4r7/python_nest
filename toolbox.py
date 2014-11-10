# -*- coding: ascii -*-

import code
import base64
import random
import rlcompleter
import readline


# hex editor
# multibase (de)encoder 
# TCP/http network crafter
# adb scripter
# multi-os scripter

class Hexedit:
	"""Hexadecimal file editor class
	"""
	def __init__(self):
		

class Compress:
	"""Class used to compress files
	"""

def launch_interpreter():
	"""Launch python interpreter with autocompletion
	"""
	readline.parse_and_bind('tab:complete')
	vars = globals().copy()
	vars.update(locals())
	shell = code.InteractiveConsole(vars)
	shell.interact()

def main():
	launch_interpreter()

if __name__ == "__main__":
	main()
