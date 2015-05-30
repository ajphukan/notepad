#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Notepad 13

#  Copyright 2015 Paul Sutton <psutton@zleap.net>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#http://effbot.org/zone/vroom.htm  
#http://knowpapa.com/text-editor/
#printing to the printer
#
import Tkinter # note use of caps
from Tkinter import *
import tkFileDialog
from tkFileDialog import askopenfilename
import tkMessageBox
import sys
import time
import os

        
#window = Tkinter.Tk(className=" Just another Text Editor")



#set up

window = Tk()
window.title('Notepad 13.0')
window.geometry("800x400") #set window size  W x h
window.resizable(0,0) #wxh

#define text entry box
notetext = Text(window, height=800, width=580)  #set text box size
#display text entry box
#notetext.pack()
#notetext.grid(row = 1, column = 3,)

#code for scroll bars

txt = Text(notetext, height=100, width=110)
scr = Scrollbar(notetext)	
scr.config(command=txt.yview)
txt.config(yscrollcommand=scr.set)
txt.pack(side=LEFT)

#code for status bar

test1 = "Notepad by Paul Sutton"


status = Label(window, text=test1, bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
#status.grid(row = 4, column = 3,)

#set up text formatting
notetext.tag_configure("Token.Comment", foreground="#b21111")

#place scroll bar in application

scr.pack(side="right", fill="y", expand=False)
notetext.pack(side="left", fill="both", expand=True)

#define menu option calls

def newfile():
	txt.delete(1.0, END)
	
# legacy open file 	
def openfile():
	text = open("document.txt").read()
	txt.delete(1.0, END)
	txt.insert(END, text)
	txt.mark_set(INSERT, 1.0)
	
def open_command():
        file = tkFileDialog.askopenfile(parent=window,mode='rb',title='Select a file')
        if file != None:
            text = file.read()
            txt.insert(END, text)
            print file
            file.close()	

#def save_command(self):
def save_command():
    file = tkFileDialog.asksaveasfile(mode='w')
    if file != None:
    # slice off the last character from get, as an extra return is added
        data = txt.get('1.0', END+'-1c')
        file.write(data)
        #filepath = tkFileDialog.asksaveasfilename()
        #filepath = os.path.normpath(filepath)
        print "this is the file name ",file
        file.close()
		
#legacy save file
def savefile():
	f = open("document.txt", "w")
	text = txt.get(1.0, END)
	try:
		# normalize trailing whitespace
		f.write(text.rstrip())
		f.write("\n")
	finally:
		f.close()
	
def syntax_highlight():
		for token, content in lex(txt, PythonLexer()):
			txt.insert("end", content, str(token))		
	
def about_cmd():
    label = tkMessageBox.showinfo("About", "Notepad by Paul Sutton")		

def exit_cmd():
	if(char_count() == 0):
		sys.exit()
	elif tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
		sys.exit()
	
		
def insert_date_time():
	dati = time.ctime() # set variable to grab the current date and time
	txt.insert(END, dati) #insert date and time into the document

def char_count():
	#msg = "Number of Characters : "
	data = txt.get('1.0', END+'-1c')
	chrcount = len(data) # get length of string 
	#txt.insert(END, chrcount)
	txt.insert(END, '\n' + str(chrcount))
	#return chrcount;
	
# create a menu
def dummy():
    print ("I am a Dummy Command, I will be removed in the next step")
    
def send2printer():
	os.system("lpr -P printer_name file_name.txt")
	print ("printer feature not enabled")    
	
def displayasASCII():
	txt.insert(END, '\n' ) # insert newline
	box = txt.get('1.0', END+'-1c')
	x = len(box)
	str(box)
	s = box
	for c in s:
		txt.insert(END, ord(c)) # insert ascII codes for each character in box
		txt.insert(END, ' ' ) # insert spsaces

def displayashex():
	txt.insert(END, '\n' ) # insert newline
	box = txt.get('1.0', END+'-1c')
	x = len(box)
	str(box)
	s = box
	for c in s:
		txt.insert(END, hex(ord(c))) # insert ascII codes for each character in box
		txt.insert(END, ' ' ) # insert spaces
    
menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=newfile)
filemenu.add_command(label="Open...", command=open_command)
filemenu.add_command(label="Save_As", command=save_command)
filemenu.add_command(label="Print", command=send2printer)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_cmd)

insertmenu = Menu(menu)
menu.add_cascade( label="Insert", menu=insertmenu)
insertmenu.add_command(label="Date/time", command=insert_date_time)		
insertmenu.add_command(label="Character count", command=char_count)	
insertmenu.add_command(label="Syntax Highlighting", command=syntax_highlight)

insertmenu.add_command(label="Display as ASCII", command=displayasASCII)		
insertmenu.add_command(label="Display as Hex", command=displayashex)	



helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about_cmd)

#toolbar

def callback():
    print "called the callback!"


#toolbar end


#display window
#window.config(menu=menubar)
window.config(menu=menu)

window.mainloop()

#define text entry box
notetext = Text(window, height=290, width=150)
#display text entry box
notetext.grid(row = 1, column = 4,)



