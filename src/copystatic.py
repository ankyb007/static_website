import os,os.path
import shutil
src = "static"
dest = "docs"



def copy_static(src, dest):
    
    src_contents = os.listdir(src)
    
    for item in src_contents:
        s = os.path.join(src, item)
        d = os.path.join(dest, item)
        if os.path.isfile(s):
            print(f"copying file {s} --> {d}")
            shutil.copy(s, d)
        elif os.path.isdir(s):
            print(f"Entering directory {s}--> {d}")
            os.makedirs(d,exist_ok= True)
            copy_static(s, d)


if os.path.exists(dest):
    shutil.rmtree(dest)
os.makedirs(dest)
copy_static(src, dest)

            




    




