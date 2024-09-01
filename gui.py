import tkinter as tk
import threading
import core, config

w,h = core.space_length

def changeL(label,text):
    label.config(text=text)

class Label1(tk.Frame):
    def __init__(self,w,h,tconfig,*args,**kargs):
        super().__init__(*args,**kargs)
        self.elements = []
        self.w = w
        self.h = h
        for i in range(h):
            f = tk.Frame(self)
            self.elements.append([])
            for i_ in range(w):
                l = tk.Label(f, **tconfig)
                l.pack(side="left")
                self.elements[-1].append(l)
            f.pack(side="top")
    def config(self,text=""):
        text = text.replace("\n","")
        if len(text)!=self.h*self.w:
            print()
            raise AssertionError(len(text),"len(text)!=self.h*self.w")
        for i in range(self.h):
            for i_ in range(self.w):
                text_ = text[self.w*i+i_]
                background="#fff"
                if text_ in config.t2n: 
                    text_=config.t2n[text_]
                    background = "#999"
                self.elements[i][i_].config(text=text_,background=background)

root = tk.Tk()
root.geometry("450x450")
root.tk.call('tk', 'scaling', 2)
frame = tk.Frame(root)
frame1 = tk.Frame(root)

label = tk.Label(frame, text="1", padx=10, pady=10,font=('Helvetica', 15))
label1 = Label1(w,h,{"padx":-100, "pady":0,"font":('Helvetica', 13),"width":0}, frame, background=None)
label2 = tk.Label(frame1, text="3", padx=10, pady=10,font=('Helvetica', 15))
label3 = tk.Label(frame1, text="3", padx=10, pady=10,font=('Helvetica', 15))
label4 = tk.Label(frame1, text="3", padx=10, pady=10,font=('Helvetica', 15))

label.pack(side="top")
label1.pack(side="top")
label2.pack(side="top")
label3.pack(side="top")
label4.pack(side="top")

frame.place(relx=0,y=0,relwidth=0.5)
frame1.place(relx=0.5,y=0,relwidth=0.5)

core.main(root,label,label1,label2,label3,label4)#https://stackoverflow.com/questions/75205191/python-thread-calling-wont-finish-when-closing-tkinter-application
root.protocol("WM_DELETE_WINDOW")
root.mainloop()
config.stop = 1