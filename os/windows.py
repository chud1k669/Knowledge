import tkinter as tk
from tkinter import ttk
from files import archives_e, write_csv


root = tk.Tk()
root.title("Archive Crawler")
root.geometry("300x250")

archiveframe = tk.Frame(borderwidth=1, padx=0, pady=0)
archivepath_entry = tk.Entry(archiveframe,width="40").grid(column=0, row =0)
archivepath_btn = tk.Button(archiveframe, text="...", height=1,width=2).grid(column=2,row = 0)
archiveframe.pack()
resframe = tk.Frame(borderwidth=1, padx=0, pady=0)
ttk.Separator(root,orient='horizontal').pack()
resultpath_entry = tk.Entry(resframe,width="40").grid(column=0, row =2)
resultpath_btn = tk.Button(resframe, text="...", height=1,width=2).grid(column=2,row = 2)
resframe.pack()



root.mainloop()