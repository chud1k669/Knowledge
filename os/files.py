import os
from datetime import datetime

path = r'C:\pyproj\knowledge\knowledge\os\files'
pathlist = os.listdir(path)
i=0

for f in os.listdir(path):
    pathname = os.path.join(path, f)
    last_modified_time = os.path.getmtime(pathname)
    formatted_time = datetime.fromtimestamp(last_modified_time).strftime('%Y-%m-%d %H:%M:%S')
    print(formatted_time)