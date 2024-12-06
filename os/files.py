from datetime import datetime
import zipfile
from pathlib import Path
import csv
from optparse import OptionParser

zippath = r'C:\pyproj\knowledge\knowledge\os\files\a\a.zip'
respath = r"C:\pyproj\knowledge\knowledge\os"
mass = []

def archives_e(path = zipfile.ZipFile, depth=0):
    indent = '  ' * depth
    global mass

    try:
        with zipfile.ZipFile(path) as zf:
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
                        archives_e(Path(extracted_file), depth + 1)
                        Path(extracted_file).unlink()
    except zipfile.BadZipFile:
        print(f"{indent}Ошибка: Не удалось открыть архив {path}. Возможно, он повреждён.")

def write_csv(respath):
    with open(respath+'/result.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, quoting=1)
        for i,j in mass:
            j = datetime(*j[:6])
            spamwriter.writerow([i]+[j])
    print("Данные успешно выведены")
    return 0