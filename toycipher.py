#!/usr/bin/env python
# coding: utf-8

from random import randint


class ToyCipher:
	def __init__(self, sBox = [12, 5, 6, 11, 9, 0, 10, 13, 3, 14, 15, 8, 4, 7, 1, 2]):
		self.sBox = sBox
		self.xobs = [sBox.index(i) for i in range(0, 16)]
	
	def round(self, msg, key):
		return self.sBox[msg^key]
    	
	def back_round(self, msg, key):
		return self.xobs[msg]^key
    	
	def enc(self, msg, key):
		return self.round(self.round(msg, key[0]), key[1])
    
	def dec(self, msg, key):
		return self.back_round(self.back_round(msg, key[1]), key[0])
		
	def enc_byte(self, msg, key):
		return self.enc(msg>>4, key)<<4|self.enc(msg&0b1111, key)
		
	def dec_byte(self, msg, key):
		return self.dec(msg>>4, key)<<4|self.dec(msg&0b1111, key)
		
	def enc_char(self, msg, key):
		return chr(self.enc_byte(ord(msg), key))
		
	def dec_char(self, msg, key):
		return chr(self.dec_byte(ord(msg), key))
		
	def enc_string(self, msg, key):
		encrypted = ""
		for char in msg:
			encrypted += self.enc_char(char, key)
		return encrypted
		
	def dec_string(self, msg, key):
		decrypted = ""
		for char in msg:
			decrypted += self.dec_char(char, key)
		return decrypted
		
	def enc_file(self, fileName, encFileName, key):
		encrypted = b""
		with open(fileName, mode='rb') as file: # b is important -> binary
			fileContent = file.read()
		for f in fileContent:
			encrypted += bytes([self.enc_byte(f, key)])
		with open(encFileName, mode='wb') as file:
			file.write(encrypted)
			
	def dec_file(self, encFileName, decFileName, key):
		decrypted = ""
		with open(encFileName, mode='rb') as file:
			fileContent = file.read()
		for f in fileContent:
			decrypted += chr(self.dec_byte(f, key))
		with open(decFileName, mode='w') as file:
			file.write(decrypted)
			
	def enc_cbc_file(self, fileName, encFileName, key):
		iv = randint(0, 255)
		encrypted = bytes([iv])
		with open(fileName, mode='rb') as file:
			fileContent = file.read()
		for f in fileContent:
			iv = self.enc_byte(f^iv, key)
			encrypted += bytes([iv])
		with open(encFileName, mode='wb') as file:
			file.write(encrypted)
			
	def dec_cbc_file(self, encFileName, decFileName, key):
		decrypted = ""
		with open(encFileName, mode='rb') as file: 
			iv = file.read(1)
			iv = iv[0]
			file.seek(1)
			fileContent = file.read()
		for f in fileContent:
			decrypted += chr(self.dec_byte(f, key)^iv)
			iv = f
		with open(decFileName, mode='w') as file:
			file.write(decrypted)
			
	def enc_cfb_file(self, fileName, encFileName, key):
		iv = randint(0, 255)
		encrypted = bytes([iv])
		with open(fileName, mode='rb') as file: 
			fileContent = file.read()
		for f in fileContent:
			iv = self.enc_byte(iv, key)^f
			encrypted += bytes([iv])
		with open(encFileName, mode='wb') as file:
			file.write(encrypted)
			
	def dec_cfb_file(self, encFileName, decFileName, key):
		decrypted = ""
		with open(encFileName, mode='rb') as file:
			iv = file.read(1)
			iv = iv[0]
			file.seek(1)
			fileContent = file.read()
		for f in fileContent:
			decrypted += chr(self.enc_byte(iv, key)^f)
			iv = f
		with open(decFileName, mode='w') as file:
			file.write(decrypted)
			
	def enc_ofb_file(self, fileName, encFileName, key):
		iv = randint(0, 255)
		encrypted = bytes([iv])
		with open(fileName, mode='rb') as file:
			fileContent = file.read()
		for f in fileContent:
			encrypted += bytes([self.enc_byte(iv, key)^f])
		with open(encFileName, mode='wb') as file:
			file.write(encrypted)
			
	def dec_ofb_file(self, encFileName, decFileName, key):
		decrypted = ""
		with open(encFileName, mode='rb') as file:
			iv = file.read(1)
			iv = iv[0]
			file.seek(1)
			fileContent = file.read()
		for f in fileContent:
			decrypted += chr(self.enc_byte(iv, key)^f)
		with open(decFileName, mode='w') as file:
			file.write(decrypted)
			


"""
key = (randint(0,15), randint(0,15))
print('key : k0 = {0}, k1 = {1}'.format(key[0], key[1]))

sBox = [12, 5, 6, 11, 9, 0, 10, 13, 3, 14, 15, 8, 4, 7, 1, 2]
print('sBox = {0}'.format(sBox))
"""
"""
msg = randint(0,15)
print('message = {0}'.format(msg))

TC = ToyCipher(sBox)
print('encrypted message = {0}'.format(TC.enc(msg, key)))
print('dycrypted message = {0}'.format(TC.dec(TC.enc(msg, key), key)))
print(msg == TC.dec(TC.enc(msg, key), key))
"""

"""
msg = 122
print('message = {0}'.format(msg))

TC = ToyCipher(sBox)
print('encrypted message = {0}'.format(TC.enc_byte(msg, key)))
print('dycrypted message = {0}'.format(TC.dec_byte(TC.enc_byte(msg, key), key)))
print(msg == TC.dec_byte(TC.enc_byte(msg, key), key))
"""

"""
msg = 'S'
print('message = {0}'.format(msg))

TC = ToyCipher(sBox)
print('encrypted message = {0}'.format(TC.enc_char(msg, key)))
print('dycrypted message = {0}'.format(TC.dec_char(TC.enc_char(msg, key), key)))
print(msg == TC.dec_char(TC.enc_char(msg, key), key))
"""

"""
msg = 'Hello'
print('message = {0}'.format(msg))

TC = ToyCipher(sBox)
print('encrypted message = {0}'.format(TC.enc_string(msg, key)))
print('dycrypted message = {0}'.format(TC.dec_string(TC.enc_string(msg, key), key)))
print(msg == TC.dec_string(TC.enc_string(msg, key), key))
"""


"""
TC = ToyCipher(sBox)
TC.enc_file("message.txt", "message.enc", key)
TC.dec_file("message.enc", "message.dec", key)
"""
































