import tkinter as tk
from tkinter import filedialog as fd
from files import archives_e, write_csv 

def archivedialog():
    archivepath_entry.insert(0,fd.askopenfilename(filetypes=(("Archive files", "*.zip"), ("All files", "*.*"))))

def resdialog():
    resultpath_entry.insert(0,fd.askdirectory())

def parse():
    zip_path = archivepath_entry.get()
    result_path = resultpath_entry.get()
    archives_e(zip_path)
    write_csv(result_path)

    print(f"Архив: {zip_path}, Результат: {result_path}")

root = tk.Tk()
root.title("Archive Crawler")
root.geometry("400x200") 

archiveframe = tk.Frame(master=root, borderwidth=1, padx=5, pady=5)
archivetitle = tk.Label(master=archiveframe, text="Путь к архиву:")
archivetitle.grid(row=0, column=0, sticky='w')
archivepath_entry = tk.Entry(master=archiveframe, width="30")
archivepath_entry.grid(row=0, column=1)
archivepath_btn = tk.Button(master=archiveframe, text="...", command=archivedialog)
archivepath_btn.grid(row=0, column=2)
archiveframe.pack(padx=10, pady=10)

resframe = tk.Frame(master=root, borderwidth=1, padx=5, pady=5)
restitle = tk.Label(master=resframe, text="Путь для сохранения:")
restitle.grid(row=0, column=0, sticky='w')
resultpath_entry = tk.Entry(master=resframe, width="30")
resultpath_entry.grid(row=0, column=1)
resultpath_btn = tk.Button(master=resframe, text="...", command=resdialog)
resultpath_btn.grid(row=0, column=2)
resframe.pack(padx=10, pady=10)

parsebtn = tk.Button(master=root, text="Выполнить парс", command=parse)
parsebtn.pack(pady=10)

root.mainloop()