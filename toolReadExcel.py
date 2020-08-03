from tkinter import *
import pandas as pd
from tkinter import filedialog
import os
import xlrd
import lxml

# root =Tk()

# label= Label(root,text="WorkOn Team")
# label.pack()

# df = pd.read_excel (r'WorkON+Platform.xls', sheet_name='general_report')



# root.mainloop()

root= Tk()

canvas1 = Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')
canvas1.pack()

def getExcel ():
    global df
    
    import_file_path = filedialog.askopenfile()
    df = pd.read_html(import_file_path)
    print (df)
    
browseButton_Excel = Button(text='Import Excel File', command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_Excel)

root.mainloop()