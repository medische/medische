import os
import subprocess
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox, ttk
from tkinter.ttk import *

from icrawler.builtin import GoogleImageCrawler


def clicked():
    if not os.path.exists('G_Download'):
        os.mkdir('G_Download')
        
    filters = dict(
        type='photo', #тип контента photo, face, clipart, animation
        # color='',# отвечает за цвет изображения, напривет blackandwhite
        size='={combo1}x{combo2}' #отвечает за размер large, icon, =1024x768
        # license='',#noncommercial, commercial 
        # date=((2022,5,1), (2022,7,1)) #отвечает за то когда было опубликовано изображение: pastweek, ((2020,01,01), (2022,01,01))
    )
        
    crawler = GoogleImageCrawler(storage={'root_dir': './G_Download'})
    crawler.crawl(
        keyword=txt.get(), 
        max_num=int(combo.get()),
        overwrite=True,
        min_size=(120,120),
        filters=filters,
        file_idx_offset='auto'
        )
    

    
    progress_bar = ttk.Progressbar(
        window, 
        orient="horizontal", 
        mode="determinate", 
        maximum=int(combo.get()), 
        value=0
        ) 
    
    label_1 = tk.Label(window, text="Загрузка завершена")
    label_1.grid(row=9, column=1) 
    progress_bar.grid(
        row=9, 
        column=2, 
        ) 
    
    window.update() 
    progress_bar['value'] = 0 
    window.update() 
    while progress_bar['value'] < int(combo.get()): 
        progress_bar['value'] += 1 
        window.update() 


window = Tk()
window.title("Добро пожаловать!")
window.geometry('600x150')

lbl = Label(window, text="Ключевые слова: ")
lbl.grid(column=0, row=0)
txt = Entry(window,width=50)
txt.grid(column=1, row=0)
txt.focus()
btn = Button(window, text="Поиск!", width=20, command=clicked)
btn.grid(column=2, row=0)
lbl = Label(window, text="Кол-во шт. : ")
lbl.grid(column=0, row=2)
lbl = Label(window, text="Разрешение : ")
lbl.grid(column=0, row=3)
combo = Combobox(window)
combo['values']= (10, 20, 50, 100, 200, 500)
combo.current(0)
combo.grid(column=1, row=2)

combo1 = Combobox(window)
combo1['values']= ('1280', '1920', '2560', '3840')
combo1.current(1)
combo1.grid(column=1, row=3)
combo2 = Combobox(window)
combo2['values']= ('720', '1080', '1440', '2160')
combo2.current(1)
combo2.grid(column=2, row=3)

def open_dir():
    subprocess.Popen(r'explorer /select,"C:\"')

btn = Button(
    window, 
    text="Открыть", 
    width=20, 
    command=open_dir
    )
btn.grid(column=1, row=5)


window.mainloop()
