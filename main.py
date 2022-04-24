import os
from tkinter import *
from tkinter import filedialog




def open_file():
    global in_path 
    in_path = filedialog.askopenfile(filetypes=[("Sequence files", ".seq")])


def convert_file():
    if in_path:
        out_path = filedialog.askdirectory()
        file_name = os.path.basename(in_path.name)[:-4]
        print(file_name)
        command = f'ffmpeg -i {in_path.name} {os.path.join(out_path, file_name)}.mp4'
        os.system(command)

bg = '#F7976D'
global in_path
in_path = None
root = Tk()
root.title('Seq to MP4')
root.geometry('400x200')
root.iconbitmap('utils/logo.ico')
root.configure(bg=bg)

title_frame = Frame(root, bg=bg)
title_frame.pack(pady=(5,0))

title = Label(title_frame, text='Seq to Mp4', font='arial 20 bold', bg=bg)
title.grid(row=0, column=0)

subtitle = Label(title_frame, text='(Windows only)', bg=bg)
subtitle.grid(row=0, column=1)

buttons_frame = Frame(root, bg=bg)
buttons_frame.pack(pady=(10,0))

open_button = Button(buttons_frame, text='Open', width=15, font='none 15', command=open_file)
open_button.grid(row=0, column=0, pady=(10))

convert_button = Button(buttons_frame, text='Convert', width=15, font='none 15', command=convert_file)
convert_button.grid(row=1, column=0)


root.mainloop()
