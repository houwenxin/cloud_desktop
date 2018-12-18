#!/usr/bin/python
# encoding: utf-8
# File Name: makeform.py

import embedded_terminal
from Tkinter import *

host = '127.0.0.1'
port = 12000
#注册窗口
class LogupForm(Frame):
    vars = []
    def __init__(self, parent=None):
	Frame.__init__(self, parent)
	fontsel = ('Courier', 20, 'bold')
	self.pack()
        
        #生成用户名和口令窗口
        e = 'User Name'
        row=Frame(self)
        lab=Label(row, font=fontsel, width=15, text=e)
        self.en1 = Entry(row,width=16,font=fontsel)
        row.pack(side=TOP,fill=X)
        lab.pack(side=LEFT)
        self.en1.pack(side=RIGHT,expand=YES,fill=X,padx=5, pady=5)
        self.vars.append(self.en1)

        e='Password'
        row=Frame(self)
        lab=Label(row, font=fontsel, width=15, text=e)
        self.en2 = Entry(row,width=16,font=fontsel,show='*')
        row.pack(side=TOP,fill=X)
        lab.pack(side=LEFT)
        self.en2.pack(side=RIGHT,expand=YES,fill=X,padx=5, pady=5)
        self.vars.append(self.en2)

	e='Verify Password'
        row=Frame(self)
        lab=Label(row, font=fontsel, width=15, text=e)
        self.en3 = Entry(row,width=16,font=fontsel,show='*')
        row.pack(side=TOP,fill=X)
        lab.pack(side=LEFT)
        self.en3.pack(side=RIGHT,expand=YES,fill=X,padx=5, pady=5)
        self.vars.append(self.en3)

                
        #生成button

        self.login = Button(self)
        self.login["text"] = 'Sign Up'
        self.login["command"] = self.show #点击"注册" button 就可以输出密码和账号了,没有做验证
        self.login.pack({"side": "left"})

    def show(self):
        print "username:",self.en1.get()
        print "passwd:",self.en2.get()
        embedded_terminal.client(host, port, '2', self.en1.get(), self.en2.get())
	self.pack_forget()

#登陆窗口
class LoginForm(Frame):
    vars = []
    window = Tk()
    def __init__(self, parent=None):
	self.window.title('Login')
	Frame.__init__(self, parent)
	fontsel = ('Courier', 20, 'bold')
	self.pack()
        
	#生成用户名和口令窗口
	e = 'User Name'
        row=Frame(self)
        lab=Label(row, font=fontsel, width=15, text=e)
        self.en1 = Entry(row,width=16,font=fontsel)
        row.pack(side=TOP,fill=X)
        lab.pack(side=LEFT)
        self.en1.pack(side=RIGHT,expand=YES,fill=X,padx=5, pady=5)
        self.vars.append(self.en1)

        e='Password'
        row=Frame(self)
        lab=Label(row, font=fontsel, width=15, text=e)
        self.en2 = Entry(row,width=16,font=fontsel,show='*')
        row.pack(side=TOP,fill=X)
        lab.pack(side=LEFT)
        self.en2.pack(side=RIGHT,expand=YES,fill=X,padx=5, pady=5)
        self.vars.append(self.en2)
	
	#生成两个button

        self.login = Button(self)
        self.login["text"] = 'Sign In'
        self.login["command"] = self.show #点击"log in" button 就可以输出密码和账号了,改show
        self.login.pack({"side": "left"})

	self.Make_acconts = Button(self)
        self.Make_acconts["text"] = 'Sign Up'
        self.Make_acconts["command"] = self.make #点击'make' button 就可以注册了
        self.Make_acconts.pack({"side": "left"})

    def show(self):
        print "username:",self.en1.get()
        print "passwd:",self.en2.get()
        print port
        print host
	command = quit
        embedded_terminal.client(host, port, '1', self.en1.get(), self.en2.get())
	
    def make(self):
#	self.window.destroy()
	LogupForm().mainloop()
	

if __name__ == '__main__':
	 LoginForm().mainloop()
