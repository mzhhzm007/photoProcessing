# -*- coding: utf-8 -*-
import os
from tkinter import *
import tkinter.filedialog

def choosePicDir():
    dirname = tkinter.filedialog.askdirectory()
    if dirname != '':
        lb_picDir.config(text="The directory is ：" + dirname);
        lb_picDir.setvar('dir',dirname)
    else:
        lb_picDir.config(text="You haven't choose any preocess directory");

def outpuName():
    print()
    for rRoot, rDirs, rFiles in os.walk(lb_picDir.getvar('dir')):
        print("this folder has %d files" % len(rFiles))
        try:
            if os.path.isdir(r'd:\ReadyToDelete'):
                pass
            else:
                os.mkdir(r'd:\ReadyToDelete')
            a = open(r'd:\ReadyToDelete\picReserve.txt', 'a')
            for f in rFiles:
                # 把文件名分解为 文件名.扩展名
                (shotname, extension) = os.path.splitext(f)
                a.write(shotname + '\n')
            a.close()
        except IOError as e:
            print(e)
    picReserve = open(r'd:\ReadyToDelete\picReserve.txt')
    num = 0
    #picReserveNames = []
    for line in picReserve:
        #rs = line.rstrip('\n')
        #picReserveNames.append(rs)
        num += 1
    print("There are %d pic names in %s" % (num, picReserve.name))
picReserve = []
root = Tk()
lb_title = Label(root, text='outputPicName')
lb_picDir = Label(root, text='')
chooseDirBtn = Button(root, text="选择照片文件夹路径", command=choosePicDir)
confirmBtn = Button(root, text="确定", command=outpuName)
lb_title.pack()
lb_picDir.pack()
chooseDirBtn.pack()
confirmBtn.pack()
root.mainloop()
