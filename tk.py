import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import shutil, os
from shutil import copy2
from natsort import natsorted, os_sorted
import datetime
from pathlib import Path

def upload_files():
   global file_paths
   file_paths = filedialog.askopenfilenames()
   files_label.configure(text='Selected Files: \n'+ '\n' .join(file_paths))      

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

#dictionary
target_locations = {
    'INF_MMF_': r'C:\Users\mmu9654\OneDrive - MassMutual\Desktop\redrop-copy\BBH',
    'STAR_': r'C:\Users\mmu9654\OneDrive - MassMutual\Desktop\redrop-copy\Babson',
}


def upload():
    for f in file_paths:
        file_name = os.path.basename(f)
        #files_label.configure(text='Redropped Files: \n'+ '\n' .join(file_paths))
        for key in target_locations.keys():
            
            base_name, ext = os.path.splitext(file_name)
            new_name = f"{base_name}_{timestamp}{ext}"
        # print(new_name)
        
            if key in new_name:
                #print(new_name)
                target_location = os.path.join(target_locations[key], new_name)
                
                shutil.move(f, target_location)
                
                result_label.configure(text='File(s) redropped successfully. Thank you!!')
                break  
                

root = tk.Tk()
root.geometry("750x750")
root.title("File Upload App")

upload_button = tk.Button(root, text='Select Files', command=upload_files)
upload_button.grid(row=0, column=0, padx=(20, 20), pady=(20, 0))

save_button = tk.Button(root, text='Upload Files', command=upload)
save_button.grid(row=2, column=0, padx=(20, 20), pady=(20, 0))

files_label = tk.Label(root, text='No files selected.')
files_label.grid(row=1, column=0, padx=(20, 20), pady=(20,0))

result_label = tk.Label(root, text='')
result_label.grid(row=3, column=0, padx=(20, 20), pady=(20, 0))

root.mainloop()