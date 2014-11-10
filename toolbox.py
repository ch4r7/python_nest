# -*- coding: ascii -*-

import code
import os
import base64
import random
import rlcompleter
import readline

#	TODO :
# hex editor [Done]
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
			self.rseek()
			self.filelength = int(self.f.tell())
			self.reset()
	
	def __len__(self):
		return self.filelength
		
	def __del__(self):
		if self.filepath and self.f:
			self.close()
	
	def close(self):
		self.f.close()
		
	def flush(self):
		self.f.flush()
		
	def seek(self,offset=0):
		self.f.seek(offset, os.SEEK_SET)
		
	def rseek(self,offset=0):
		self.f.seek(offset, os.SEEK_END)
	
	def reset(self):
		"""Reset internal file cursor to the begining
		"""
		if self.f:
			self.seek()
			
	def read(self,size):
		return self.f.read(size)
	
	def write(self,out):
		return self.f.write(out)
	
	def read_list(size , off_start=0):
		"""read size bytes from off_start and return a list containing
		each chars int values
		"""
		self.seek(off_start)
		return [ord(d) for d in self.read(size)]
	
	def get_list(self,off_start,off_stop):
		"""Return byte list from start offset to stop offset
		"""
		self.reset()
		self.seek(off_start)
		return [ord(d) for d in self.read( off_stop - off_start )]
		
	def set(self,off_start,output):
		"""Replace and potentially expand file with byte_array values
		from file's off_start offset
		"""
		self.close()
		self.f = open(self.filepath,'r+')
		
		self.seek(off_start)
		if type(output) == str:
			self.write(output)
		elif type(output) == list:
			if len(output) > 0  and type(output[0])== int:
				self.write("".join([chr(c) for c in output]))
		
		self.flush()
		self.close()
		self.f = open(self.filepath,'rb')
		
	def rdisp(self, size=0, offset=0,  enable_ascii_repr = True):
		"""Display size file's bytes from len(file) - offset in
		hexadecimal representation
		"""
		return self.disp(size, self.filelength - offset,  enable_ascii_repr)
		
	def less(self):
		self.disp(16)
		offset  = 16
		try:
			while(True):
				if offset > len(self):
					break
				self._disp(16,offset,True,False)
				raw_input()
				offset+=16
		except KeyboardInterrupt:
			pass
	
	def disp(self, size=0,  offset=0,enable_ascii_repr = True):
		"""Display size file's bytes from offset in hexadecimal
		representation
		"""
		return self._disp(size,offset,enable_ascii_repr,True)
		
	def _disp(self, size=0,  offset=0,enable_ascii_repr = True, enable_top_border = True):
		sep_char = " "
		line_byte_length = 16
	
		# default file size
		if size == 0:
			size = self.filelength
		
		# size fix if too long
		if size + offset > self.filelength:
			size = self.filelength - offset
			
		ret = "%05X%s%s"%(0,sep_char,sep_char.join(["%02X"%d for d in range(line_byte_length)])) if enable_top_border else ""
		
		if self.f:
			self.f.seek(offset)
			ret += "\n"
			
			for i in range(size/line_byte_length):
				values = self.f.read(line_byte_length)
				ret += "%05X%s%s"%(offset+i*line_byte_length,sep_char,sep_char.join(["%02X"%ord(d) for d in values]))
				if enable_ascii_repr:
					ret += " | %s |"%("".join([ "%c"%v if (ord(v)<126 and ord(v)>=32) else "." for v in values]))
				ret += "\n"
			
			if size%line_byte_length > 0 :
				values = self.f.read( size%line_byte_length )
				ret += "%05X%s%s"%(offset+(size/line_byte_length)*line_byte_length,sep_char,sep_char.join(["%02X"%ord(d) for d in values ]))
				#Space padding
				ret += (line_byte_length - len(values))*"   "
				
				if enable_ascii_repr:
					ret += " | %s |"%("".join([ "%c"%v if (ord(v)<126 and ord(v)>=32) else "." for v in values]))
			
		print ret
	
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
