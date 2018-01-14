# -*- coding: utf-8 -*-

import os
from tkinter import *
import tkinter.filedialog


def chooseProcessDir():
    filename = tkinter.filedialog.askdirectory()
    if filename != '':
        #lb.config(text="The directory is ：" + filename);
        lb_procDir.set(filename)
        lb2.config(text=lb_procDir.get())
    else:
        lb2.config(text="You haven't choose any preocess directory");
def chooseReferenceDir():
    filename = tkinter.filedialog.askdirectory()
    if filename != '':
        # lb.config(text="The directory is ：" + filename);
        lb_refDir.set(filename)
        lb3.config(text=lb_refDir.get())
    else:
        lb3.config(text="You haven't choose any preocess directory");

def process():
    return


root = Tk()
lb1 = Label(root, text='photoProcess')
lb2= Label(root, text='')
lb3 = Label(root, text='')
lb_procDir=StringVar()
lb_refDir=StringVar()
chooseRefBtn = Button(root, text="选择参照文件夹", command=chooseProcessDir)
chooseProcBtn = Button(root, text="选择需要处理的文件夹", command=chooseReferenceDir)
confirmBtn = Button(root, text="确定", command=process)
lb1.pack()
lb2.pack()
chooseRefBtn.pack()
lb3.pack()
chooseProcBtn.pack()
confirmBtn.pack()
root.mainloop()



def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        print(files)  # 当前路径下所有非目录子文件

