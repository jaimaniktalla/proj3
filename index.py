import tkinter as tk
import os
import shutil

def organize_files():
    folder_path = entry_folder.get()
    if os.path.isdir(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                file_extension = filename.split('.')[-1]
                folder_name = os.path.join(folder_path, file_extension)
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                shutil.move(file_path, os.path.join(folder_name, filename))
        label_result.config(text="Files organized successfully!")
    else:
        label_result.config(text="Invalid directory path.")

# GUI setup
root = tk.Tk()
root.title("File Organizer")

label_folder = tk.Label(root, text="Enter Folder Path:")
label_folder.pack()

entry_folder = tk.Entry(root)
entry_folder.pack()

button_organize = tk.Button(root, text="Organize Files", command=organize_files)
button_organize.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()