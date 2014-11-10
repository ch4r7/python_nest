# -*- coding: ascii -*-

import code
import os
import base64
import random
import rlcompleter
import readline

#	TODO :
# hex editor
# multibase (de)encoder 
# TCP/http network crafter
# adb scripter
# multi-os scripter

class Hxf:
	"""Hexadecimal file editor class
	"""
	def __init__(self, filepath=None):
		if filepath:
			self.filepath = filepath
			self.f = open(filepath,'rb')
			self.f.seek(0, os.SEEK_END)
			self.filelength = self.f.tell()
			self.f.seek(0, os.SEEK_SET)
			
		
	def __del__(self):
		if self.filepath and self.f:
			self.f.close()
	
	def rdisp(self, size=32, offset=0,  enable_ascii_repr = True):
		"""Display size file's bytes from len(file) - offset in hexadecimal representation
		"""
		return self.disp(size, self.filelength - offset,  enable_ascii_repr)
		
	def disp(self, size=0,  offset=0,enable_ascii_repr = True):
		"""Display size file's bytes from offset in hexadecimal representation
		"""
		sep_char = " "
		line_byte_length = 16
	
		# default file size
		if size == 0:
			size = self.filelength
		
		# size fix if too long
		if size + offset > self.filelength:
			size = self.filelength - offset
		
		ret = "%05X%s%s"%(0,sep_char,sep_char.join(["%02X"%d for d in range(line_byte_length)]))
		
		if self.f:
			self.f.seek(offset)
			ret += "\n"
			
			for i in range(size/line_byte_length):
				values = self.f.read(line_byte_length)
				ret += "%05X%s%s"%(i*line_byte_length,sep_char,sep_char.join(["%02X"%ord(d) for d in values]))
				if enable_ascii_repr:
					ret += " | %s |"%("".join([ "%c"%v if (ord(v)<126 and ord(v)>=32) else "." for v in values]))
				ret += "\n"
			
			if size%line_byte_length > 0 :
				values = self.f.read( size%line_byte_length )
				ret += "%05X%s%s"%((size/line_byte_length)*line_byte_length,sep_char,sep_char.join(["%02X"%ord(d) for d in values ]))
				#Space padding
				ret += (line_byte_length - len(values))*"   "
				
				if enable_ascii_repr:
					ret += " | %s |"%("".join([ "%c"%v if (ord(v)<126 and ord(v)>=32) else "." for v in values]))
			
		print ret
		
	#~ def get(self):
	
	
	
class Cp:
	"""Class used to compress bytestring
	"""
	def __init__(self, input_string):
		self.input_string = input_string
		
	
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
