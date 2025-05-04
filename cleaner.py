import os
import shutil
import time

# Cleaning Function
def clean_temp_folder(folder_path):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        except Exception as e:
            pass

# Path Founder
temp_path = os.environ['TEMP']
temp_path_system = r'C:\Windows\Temp'

print("Hello! I'm a program coded by @matteoatw. I'll help you with some garbage on your system. Let's start.")
time.sleep(3)

print(f"The folder was found successfully in {temp_path}")
print(f"The folder was found successfully in {temp_path_system}")
time.sleep(1)

answer=input("Let's clean your computer. Are you sure? (Y/N)")
time.sleep(1)

if answer.lower() == 'y':
    print("Ok, cleaning... don't close the window.")
    clean_temp_folder(temp_path)
    clean_temp_folder(temp_path_system)
else:
    print("Alright. See your later!")

time.sleep(1)
print("Done. Now, everything is cleaned.")
input("Press ENTER your keyboard to close this windows...")

# Coded By github.com/mateuscapo