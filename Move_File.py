import os
import shutil
from_dir="C:/Users/dell/Downloads"
to_dir="C:/Users/dell/Desktop/Document_Files"
list_of_files=os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
   # print("name of path:",name)
    #print("extension of path:",extension)

    if extension == '':
        continue 
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1=from_dir+'/'+file_name
        path2=to_dir + '/'+"Document_Files"
        path3=to_dir + '/'+"Document_Files"+file_name
        print("path1:",path1)
        print("path3:",path3)
        if os.path.exists(path2):
            print("moving "+file_name+"....")
            shutil.move(path1,path3)
        else :
            os.mkdir(path2)
            print("moving "+file_name+"....")
            shutil.move(path1,path3)
