import os
from pathlib import Path
import shutil
import fnmatch
# os.mkdir("Example")
path="./Example/subdirect"
# os.mkdir(path)

#shutil.move("download.png","Example/subdirect")

# shutil.move("python.txt","Example/subdirect")
newpath="./Example"
son=".txt"
#shutil.move("./Example/subdirect/python.txt","./Example")
with Path(path) as file:
    for i in file.iterdir():
        if i.is_file() and i.name.endswith(son):
            print(i.name)
            shutil.move("./Example/subdirect/"+i.name,"./Example")



