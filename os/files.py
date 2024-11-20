from datetime import datetime
import zipfile
from pathlib import Path
import csv
import time

path = r'C:\pyproj\knowledge\knowledge\os\files\a.zip'
respath = r"C:\pyproj\knowledge\knowledge\os"
mass = []

def extract_and_explore_archives(archive_path, depth=0):
    indent = '  ' * depth
    global mass

    try:
        with zipfile.ZipFile(archive_path) as zf:
            for info in zf.infolist():
                filename = info.filename
                if not filename.endswith(".zip"):
                    date = info.date_time
                    print(f"{indent}{filename} {date}")
                    infolist = [filename,date]
                    mass.append(infolist)
                else:
                    print(f"{indent}{filename}")
                if not info.is_dir():
                    if filename.endswith('.zip'):
                        extracted_file = zf.extract(filename)
                        extract_and_explore_archives(Path(extracted_file), depth + 1)
                        Path(extracted_file).unlink()
    except zipfile.BadZipFile:
        print(f"{indent}Ошибка: Не удалось открыть архив {archive_path}. Возможно, он повреждён.")

def write_csv(directory,dict):
    with open('result.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, quoting=1)
        for i,j in mass:
            j = datetime(*j[:6])
            spamwriter.writerow([i]+[j])
    print("Данные успешно выведены")
    return 0


extract_and_explore_archives(path)
write_csv(respath,mass)