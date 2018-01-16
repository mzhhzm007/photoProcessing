# -*- coding: utf-8 -*-

import os
from tkinter import *
import tkinter.filedialog
from shutil import move

def chooseReferenceFile():
    filename = tkinter.filedialog.askopenfilename()
    if filename != '':
        # lb.config(text="The directory is ：" + filename);
        lb_refDir.set(filename)
        lb2.config(text=lb_refDir.get())
    else:
        lb2.config(text="You haven't choose any reference file");


def chooseProcessDir():
    filename = tkinter.filedialog.askdirectory()
    if filename != '':
        # lb.config(text="The directory is ：" + filename);
        lb_procDir.set(filename)
        lb3.config(text=lb_procDir.get())
    else:
        lb3.config(text="You haven't choose any process directory");

def process():

    picReserve = open(lb_refDir.get())
    num = 0
    picReserveNames = []
    for line in picReserve:
        rs = line.rstrip('\n')
        picReserveNames.append(rs)
        num += 1
    print("There are %d pic names in %s" % (num, picReserve.name))
    print(picReserveNames)
    for pRoot, pDirs, pFiles in os.walk(lb_procDir.get()):
        print("this folder has %d files" % len(pFiles))
        if os.path.isdir(r'd:\ReadyToDelete'):
            pass
        else:
            os.mkdir(r'd:\ReadyToDelete')
        for f in pFiles:
            (shotname, extension) = os.path.splitext(f)
            if shotname not in picReserveNames:
                fullPath = os.path.join(pRoot, f)
                print(fullPath)
                move(fullPath,r'd:\ReadyToDelete\\'+f)
    print("after process,this folder has %d files" % len(os.listdir(lb_procDir.get())))

picReserve = []
picTest = []
procFiles = []
refFiles = []
root = Tk()
lb1 = Label(root, text='photoProcess')
lb2 = Label(root, text='')
lb3 = Label(root, text='')
lb_procDir = StringVar()
lb_refDir = StringVar()
chooseRefBtn = Button(root, text="选择参照文件", command=chooseReferenceFile)
chooseProcBtn = Button(root, text="选择需要处理的文件夹", command=chooseProcessDir)
confirmBtn = Button(root, text="确定", command=process)
lb1.pack()
lb2.pack()
chooseRefBtn.pack()
lb3.pack()
chooseProcBtn.pack()
confirmBtn.pack()
root.mainloop()
