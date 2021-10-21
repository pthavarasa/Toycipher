import tkinter as tk
import os.path
from toycipher import ToyCipher
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import ttk
from tkinter import messagebox
from random import randint
from time import sleep, time

debug = False # make it true to see the progresse bar and remining time for smaller file

class ToyCipherApp(ToyCipher): # override methods for the progresse bar and remining time compatibilities
	def enc_cbc_file(self, fileName, encFileName, key):
		iv = randint(0, 255)
		encrypted = bytes([iv])
		with open(fileName, mode='rb') as file:
			fileContent = file.read()
		fileContentSize = len(fileContent)
		mul = 100/fileContentSize
		startTime = time()
		sec2 = 0
		for i, f in enumerate(fileContent):
			sec = int(time() - startTime)
			if i:
				sec = int((fileContentSize - i) * sec / i)
			else:
				sec = 0
			minutes = int(sec/60)
			seconds = sec - (minutes * 60)
			if seconds != sec2:
				sec2 = seconds
				label_rt1.config(text = str(minutes) + " minutes  " + str(seconds) + " seconds")
			if debug:sleep(0.1)
			progress['value'] = int(i*mul)
			app.update_idletasks()
			iv = self.enc_byte(f^iv, key)
			encrypted += bytes([iv])
		progress['value'] = 100
		app.update_idletasks()
		with open(encFileName, mode='wb') as file:
			file.write(encrypted)
			
	def dec_cbc_file(self, encFileName, decFileName, key):
		decrypted = ""
		with open(encFileName, mode='rb') as file: 
			iv = file.read(1)
			iv = iv[0]
			file.seek(1)
			fileContent = file.read()
		fileContentSize = len(fileContent)
		mul = 100/fileContentSize
		startTime = time()
		sec2 = 0
		for i, f in enumerate(fileContent):
			sec = int(time() - startTime)
			if i:
				sec = int((fileContentSize - i) * sec / i)
			else:
				sec = 0
			minutes = int(sec/60)
			seconds = sec - (minutes * 60)
			if seconds != sec2:
				sec2 = seconds
				label_rt1.config(text = str(minutes) + " minutes  " + str(seconds) + " seconds")
			if debug:sleep(0.1)
			progress['value'] = int(i*mul)
			app.update_idletasks()
			decrypted += chr(self.dec_byte(f, key)^iv)
			iv = f
		progress['value'] = 100
		app.update_idletasks()
		with open(decFileName, mode='w') as file:
			file.write(decrypted)
	
	def enc_cfb_file(self, fileName, encFileName, key):
		iv = randint(0, 255)
		encrypted = bytes([iv])
		with open(fileName, mode='rb') as file: 
			fileContent = file.read()
		fileContentSize = len(fileContent)
		mul = 100/fileContentSize
		startTime = time()
		sec2 = 0
		for i, f in enumerate(fileContent):
			sec = int(time() - startTime)
			if i:
				sec = int((fileContentSize - i) * sec / i)
			else:
				sec = 0
			minutes = int(sec/60)
			seconds = sec - (minutes * 60)
			if seconds != sec2:
				sec2 = seconds
				label_rt1.config(text = str(minutes) + " minutes  " + str(seconds) + " seconds")
			if debug:sleep(0.1)
			progress['value'] = int(i*mul)
			app.update_idletasks()
			iv = self.enc_byte(iv, key)^f
			encrypted += bytes([iv])
		progress['value'] = 100
		app.update_idletasks()
		with open(encFileName, mode='wb') as file:
			file.write(encrypted)
			
	def dec_cfb_file(self, encFileName, decFileName, key):
		decrypted = ""
		with open(encFileName, mode='rb') as file:
			iv = file.read(1)
			iv = iv[0]
			file.seek(1)
			fileContent = file.read()
		fileContentSize = len(fileContent)
		mul = 100/fileContentSize
		startTime = time()
		sec2 = 0
		for i, f in enumerate(fileContent):
			sec = int(time() - startTime)
			if i:
				sec = int((fileContentSize - i) * sec / i)
			else:
				sec = 0
			minutes = int(sec/60)
			seconds = sec - (minutes * 60)
			if seconds != sec2:
				sec2 = seconds
				label_rt1.config(text = str(minutes) + " minutes  " + str(seconds) + " seconds")
			if debug:sleep(0.1)
			progress['value'] = int(i*mul)
			app.update_idletasks()
			decrypted += chr(self.enc_byte(iv, key)^f)
			iv = f
		progress['value'] = 100
		app.update_idletasks()
		with open(decFileName, mode='w') as file:
			file.write(decrypted)
			
	def enc_ofb_file(self, fileName, encFileName, key):
		iv = randint(0, 255)
		encrypted = bytes([iv])
		with open(fileName, mode='rb') as file:
			fileContent = file.read()
		fileContentSize = len(fileContent)
		mul = 100/fileContentSize
		startTime = time()
		sec2 = 0
		for i, f in enumerate(fileContent):
			sec = int(time() - startTime)
			if i:
				sec = int((fileContentSize - i) * sec / i)
			else:
				sec = 0
			minutes = int(sec/60)
			seconds = sec - (minutes * 60)
			if seconds != sec2:
				sec2 = seconds
				label_rt1.config(text = str(minutes) + " minutes  " + str(seconds) + " seconds")
			if debug:sleep(0.1)
			progress['value'] = int(i*mul)
			app.update_idletasks()
			encrypted += bytes([self.enc_byte(iv, key)^f])
		progress['value'] = 100
		app.update_idletasks()
		with open(encFileName, mode='wb') as file:
			file.write(encrypted)
			
	def dec_ofb_file(self, encFileName, decFileName, key):
		decrypted = ""
		with open(encFileName, mode='rb') as file:
			iv = file.read(1)
			iv = iv[0]
			file.seek(1)
			fileContent = file.read()
		fileContentSize = len(fileContent)
		mul = 100/fileContentSize
		startTime = time()
		sec2 = 0
		for i, f in enumerate(fileContent):
			sec = int(time() - startTime)
			if i:
				sec = int((fileContentSize - i) * sec / i)
			else:
				sec = 0
			minutes = int(sec/60)
			seconds = sec - (minutes * 60)
			if seconds != sec2:
				sec2 = seconds
				label_rt1.config(text = str(minutes) + " minutes  " + str(seconds) + " seconds")
			if debug:sleep(0.1)
			progress['value'] = int(i*mul)
			app.update_idletasks()
			decrypted += chr(self.enc_byte(iv, key)^f)
		progress['value'] = 100
		app.update_idletasks()
		with open(decFileName, mode='w') as file:
			file.write(decrypted)

def selectFile():
	global FILE_NAME
	select_file_name = askopenfilename()
	FILE_NAME = select_file_name.split("/").pop().split(".")[0]
	entry_sef.delete(0, 'end')
	entry_sef.insert(0, select_file_name)

def saveFile():
	global SAVE_FILE_PATH
	try: FILE_NAME
	except NameError:
		label_log1.config(text = "First select the file you want to encrypt!")
		return
	select_file_name = askdirectory()
	entry_sf.delete(0, 'end')
	if isinstance(select_file_name, str):
		SAVE_FILE_PATH = select_file_name
		entry_sf.insert(0, select_file_name+"/"+FILE_NAME+".enc")
		
def changeFileExtention(event):
	if combo_action.get() == "Encrypt":
		try: FILE_NAME and SAVE_FILE_PATH
		except NameError:
			label_log1.config(text = "First select the file you want to encrypt!")
			return
		entry_sf.delete(0, 'end')
		entry_sf.insert(0, SAVE_FILE_PATH+"/"+FILE_NAME+".enc")
	else:
		try: FILE_NAME and SAVE_FILE_PATH
		except NameError:
			label_log1.config(text = "First select the file you want to encrypt!")
			return
		entry_sf.delete(0, 'end')
		entry_sf.insert(0, SAVE_FILE_PATH+"/"+FILE_NAME+".dec")
		
def checkKeyRequestment(P):
	if str.isdigit(P) or P == "":
		if P == "" or int(P) < 16:
			return True
		else:
			label_log1.config(text = "Key must be 0 to 15!")
			return False
		return True
	else:
		label_log1.config(text = "Key must be a interger, given character!")
		return False
		
def randomKey():
	entry_k0.delete(0, 'end')
	entry_k0.insert(0, randint(0, 15))
	entry_k1.delete(0, 'end')
	entry_k1.insert(0, randint(0, 15))
	
def close():
	app.destroy()
	
def start():
	select_file = entry_sef.get()
	if select_file == '':
		label_log1.config(text = "Please select the file you want to encrypt!")
		return
	if not os.path.exists(select_file):
		label_log1.config(text = "The file you want to encrypt not found!")
		return
	save_file = entry_sf.get()
	if save_file == '':
		label_log1.config(text = "Please select the save file path!")
		return
	if os.path.exists(save_file):
		if not start.override_granted:
			MsgBox = tk.messagebox.askquestion ('Confirmation',
			'The file name you want to save already exist!\n Do you want to override the file?',
				icon = 'warning')
			if MsgBox == 'yes':
				start.override_granted = True
			else:
				label_log1.config(text = "change saving file name!")
				return
	action = combo_action.get()
	Type = combo_type.get()
	key = entry_k0.get(), entry_k1.get()
	if key[0] == '' or key[1] == '':
		label_log1.config(text = "Key is empty!")
		return
		
	label_log1.config(text = "File encrypting ...")
	TCA = ToyCipherApp()
	if action == "Encrypt" and Type == "cbc":
		TCA.enc_cbc_file(select_file, save_file, (int(key[0]), int(key[1])))
		label_log1.config(text = "File successfully encrypted.")
	elif action == "Decrypt" and Type == "cbc":
		TCA.dec_cbc_file(select_file, save_file, (int(key[0]), int(key[1])))
		label_log1.config(text = "File successfully decrypted.")
	elif action == "Encrypt" and Type == "cfb":
		TCA.enc_cfb_file(select_file, save_file, (int(key[0]), int(key[1])))
		label_log1.config(text = "File successfully encrypted.")
	elif action == "Decrypt" and Type == "cfb":
		TCA.dec_cfb_file(select_file, save_file, (int(key[0]), int(key[1])))
		label_log1.config(text = "File successfully decrypted.")
	elif action == "Encrypt" and Type == "ofb":
		TCA.enc_ofb_file(select_file, save_file, (int(key[0]), int(key[1])))
		label_log1.config(text = "File successfully encrypted.")
	elif action == "Decrypt" and Type == "ofb":
		TCA.dec_ofb_file(select_file, save_file, (int(key[0]), int(key[1])))
		label_log1.config(text = "File successfully decrypted.")


# GUI
app = tk.Tk()
app.title("ToyCipher - File encryption, decryption")
app.geometry("400x510")
app.resizable(False, False)


# select file + choose file button + entry bar
label_sef = tk.Label(app, text = "Select file : ")
label_sef.grid(column = 0, row = 0, padx = 15, pady = 20, sticky = tk.W)

button_sef = tk.Button(app, text = "choose file", command = selectFile)
button_sef.grid(column = 0, row = 0, padx = 100, pady = 5, sticky = tk.W)

entry_sef = tk.Entry(app, width = 45)
entry_sef.grid(column = 0, row = 1, padx = 15, pady = 5, sticky = tk.W)


# save file + choose file button + entry bar
label_sf = tk.Label(app, text = "Save file : ")
label_sf.grid(column = 0, row = 2, padx = 15, pady = 20, sticky = tk.W)

button_sf = tk.Button(app, text = "choose path", command = saveFile)
button_sf.grid(column = 0, row = 2, padx = 100, pady = 5, sticky = tk.W)

entry_sf = tk.Entry(app, width = 45)
entry_sf.grid(column = 0, row = 3, padx = 15, pady = 5, sticky = tk.W)


# action (encrypt, decrypt) + type (cbc, cfb, ofb)
label_sf = tk.Label(app, text = "Action : ")
label_sf.grid(column = 0, row = 4, padx = 15, pady = 15, sticky = tk.W)

combo_action = ttk.Combobox(app, values=["Encrypt", "Decrypt"], width = 10, state="readonly")
combo_action.grid(column = 0, row = 4, padx = 100, pady = 10, sticky = tk.W)
combo_action.current(0)
combo_action.bind("<<ComboboxSelected>>", changeFileExtention)

label_type = tk.Label(app, text = "Type : ")
label_type.grid(column = 0, row = 4, padx = 220, pady = 10, sticky = tk.W)

combo_type = ttk.Combobox(app, values=["cbc", "cfb", "ofb"], width = 10, state="readonly")
combo_type.grid(column = 0, row = 4, padx = 282, pady = 10, sticky = tk.W)
combo_type.current(0)


# Key pair (k0, k1) entry + random key button
vcmd = (app.register(checkKeyRequestment))

label_sf = tk.Label(app, text = "Key pair : ")
label_sf.grid(column = 0, row = 5, padx = 15, pady = 10, sticky = tk.W)

entry_k0 = tk.Entry(app, width = 3, validate='all', validatecommand=(vcmd, '%P'))
entry_k0.grid(column = 0, row = 5, padx = 100, pady = 10, sticky = tk.W)

entry_k1 = tk.Entry(app, width = 3, validate='all', validatecommand=(vcmd, '%P'))
entry_k1.grid(column = 0, row = 5, padx = 150, pady = 10, sticky = tk.W)

button_ran = tk.Button(app, width = 10, text = "Random Key", command = randomKey)
button_ran.grid(column = 0, row = 5, padx = 270, pady = 5, sticky = tk.W)


# Remaining time + Progress bar
label_rt = tk.Label(app, text = "Remaining time : ")
label_rt.grid(column = 0, row = 6, padx = 15, pady = 10, sticky = tk.W)

label_rt1 = tk.Label(app, text = "")
label_rt1.grid(column = 0, row = 6, padx = 150, pady = 10, sticky = tk.W)

label_rt = tk.Label(app, text = "Progression : ")
label_rt.grid(column = 0, row = 7, padx = 15, pady = 10, sticky = tk.W)

progress = ttk.Progressbar(app, orient = "horizontal", length = 365, mode = 'determinate') 
progress.grid(column = 0, row = 8, padx = 15, pady = 10, sticky = tk.W)


# start button + close button
start.override_granted = False
button_start = tk.Button(app, width = 10, text = "Start", command = start)
button_start.grid(column = 0, row = 9, padx = 15, pady = 20, sticky = tk.NW)

button_close = tk.Button(app, width = 10, text = "Close", command = close)
button_close.grid(column = 0, row = 9, padx = 272, pady = 20, sticky = tk.NW)


# separator horizontal
s = ttk.Separator(app, orient="horizontal")
s.grid (column = 0, row = 10, pady = 5, sticky = tk.EW )


# log option
label_log = tk.Label(app, text = "Log : ")
label_log.grid(column = 0, row = 11, padx = 15, sticky = tk.W)

label_log1 = tk.Label(app, text = "")
label_log1.grid(column = 0, row = 11, padx = 50, sticky = tk.W)


# app main loop
app.mainloop()

















