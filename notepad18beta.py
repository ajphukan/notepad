#!/usr/bin/env python2
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
#printing to the printer#!/usr/bin/env python
#add rot13 encoding http://code.activestate.com/recipes/578322-use-rot13-to-endecrypt-clear-text/ added v16
#add highlighting version 16 http://pygments.org/docs/
#fix issue with pressing x to close window and getting error http://stackoverflow.com/questions/3295270/overriding-tkinter-x-button-control-the-button-that-close-the-window

#
import Tkinter # note use of caps
from Tkinter import *
import tkFileDialog
from tkFileDialog import askopenfilename
import tkMessageBox
import sys
import time
import os
from pygments import lex
from pygments.lexers import PythonLexer

#define functions for menu calls
#define menu option calls

LOWER_LETTERS = [chr(x) for x in range(97, 123)];
UPPER_LETTERS = [chr(x) for x in range(65, 91)];



def doSomething():
    # check if saving
    # if not:
   sys.exit()

def newfile():
	txt.delete(1.0, END)
	
def open_command():
	txt.delete(1.0, END)
	filename = tkFileDialog.askopenfile(parent=window,mode='rb',title='Select a file')
	if filename != None:
		txt.delete(1.0, END)
		text = filename.read()
		txt.insert(END, text)
		name = askopenfilename()
		print(name)
		filename.close()	
            
def savefile():
	print ("save file")
	data = txt.get('1.0', END+'-1c')
        filename.write(data)
        filename.close()
        
def saveas_command():
    filename = tkFileDialog.asksaveasfile(mode='w')
    if filename != None:
    # slice off the last character from get, as an extra return is added
        data = txt.get('1.0', END+'-1c')
        filename.write(data)
        #filepath = tkFileDialog.asksaveasfilename()
        #filepath = os.path.normpath(filepath)
        #print "this is the file name ",fname
        filename.close()
		

def syntax_highlight():
		for token, content in lex(txt, PythonLexer()):
			txt.insert("end", content, str(token))		
	
def about_cmd():
    label = tkMessageBox.showinfo("About", "Notepad v17 by Paul Sutton")		

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

#convert to / from rot13, as in this can go BOTH ways
def rot13():
	#print ("rot 13 encoding")
	sourceString = txt.get('1.0', END+'-1c')
	#print sourceString
	resultString = "";
	for char in sourceString:
		if char.isupper():
			resultString += encrypt(char, UPPER_LETTERS);
		elif char.islower():
			resultString += encrypt(char, LOWER_LETTERS);
		else:
			resultString += char;
	#print("The rot13 string is:%s" % (resultString));	
	txt.delete(1.0, END)
	txt.insert(END, resultString)
	
def encrypt(char, letterList):
    resultchar = '';
    originalIndex = letterList.index(char)
    newIndex = originalIndex + 13
    resultchar += letterList[newIndex % len(letterList)]
    return resultchar	


def insertfname():
	print ("insert filename")
	print filename
	
#syntax highlighting not working    
#def syntax_highlight():
#	for token, content in lex(txt, PythonLexer()):
#		txt.insert("end", content, str(token))
	
	
	
#set up

window = Tk()
window.title('Notepad 16.0')
window.geometry("800x400") #set window size  W x h
window.resizable(0,0) #wxh
window.protocol('WM_DELETE_WINDOW', doSomething)  # root is your root window


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

#code for tool bar

# create a toolbar
	
toolbar = Frame(window)	
#new file
b = Button(toolbar, text="New", width=6, command=newfile)
b.pack(side=LEFT, padx=2, pady=2)
#open file
b = Button(toolbar, text="Open", width=6, command=open_command)
b.pack(side=LEFT, padx=2, pady=2)

#saveas file
b = Button(toolbar, text="Save", width=6, command=savefile)
b.pack(side=LEFT, padx=2, pady=2)

#saveas file
b = Button(toolbar, text="Save_As", width=6, command=saveas_command)
b.pack(side=LEFT, padx=2, pady=2)


toolbar.pack(side=TOP, fill=X)	

#code for status bar

test1 = "Notepad by Paul Sutton"

status = Label(window, text=test1, bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


#status.grid(row = 4, column = 3,)

#code for status bar end

#set up text formatting
notetext.tag_configure("Token.Comment", foreground="#b21111")

#place scroll bar in application

scr.pack(side="right", fill="y", expand=False)
notetext.pack(side="left", fill="both", expand=True)


	
	
#menu	
    
menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=newfile)
filemenu.add_command(label="Open...", command=open_command)
filemenu.add_command(label="Save", command=savefile)
filemenu.add_command(label="Save_As", command=saveas_command)
#filemenu.add_command(label="Print", command=send2printer)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_cmd)

insertmenu = Menu(menu)
menu.add_cascade( label="Insert", menu=insertmenu)
insertmenu.add_command(label="Date/time", command=insert_date_time)		
insertmenu.add_command(label="Character count", command=char_count)	
#insertmenu.add_command(label="Syntax Highlighting", command=syntax_highlight)
insertmenu.add_command(label="Insert Filenamet", command=insertfname)

insertmenu.add_command(label="Display as ASCII", command=displayasASCII)		
insertmenu.add_command(label="Display as Hex", command=displayashex)	
insertmenu.add_command(label="ROT13 Encode / Decode", command=rot13)
#insertmenu.add_command(label="ROT13 Decode", command=rot13_decode)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about_cmd)

#display window
#window.config(menu=menubar)
window.config(menu=menu)


window.mainloop()

#define text entry box
notetext = Text(window, height=290, width=150)
#display text entry box
notetext.grid(row = 1, column = 4,)



