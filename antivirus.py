import os
import hashlib
import psutil
import time

# Function to compare MD5 hash values
global counter
def compare_hash(file_path, virus_hashes):
    with open(file_path, 'rb') as file:
        content = file.read()
        file_hash = hashlib.md5(content).hexdigest()
        print(file_hash)
        # file_hash = file_hash.decode()
        if file_hash in virus_hashes:
            print("Virus found in file:", file_path)
            return True
    return False

# Function to delete a file
def delete_file(file_path):
    try:
        os.remove(file_path)
        print("File deleted:", file_path)
    except Exception as e:
        print("Error deleting file:", e)

# Function to scan and compare the system or folder
def scan_and_delete(virus_hashes, path):
    counter=0
    start_time = time.time()
    virus_found = False
    num_files_scanned = 0

    for root, dirs, files in os.walk(path):
        for file_name in files:
            num_files_scanned += 1
            file_path = os.path.join(root, file_name)
            if compare_hash(file_path, virus_hashes):
                virus_found = True
                counter +=1

    end_time = time.time()

    if virus_found:
        print("Virus found in the path:", path)
        choice = input("Do you want to delete the infected files? (y/n): ")
        if choice.lower() == 'y':
            for root, dirs, files in os.walk(path):
                for file_name in files:
                    file_path = os.path.join(root, file_name)
                    if compare_hash(file_path, virus_hashes):
                        delete_file(file_path)

    report = f"\nScan Report\n" \
             f"Number of files scanned: {num_files_scanned}\n" \
             f"Viruses found:{counter} {'Yes' if virus_found else 'No'}\n"\
             f"Time taken: {end_time - start_time:.2f} seconds\n"
    print(report)

# Function to free RAM storage and boost RAM
def free_ram_boost():
    memory = psutil.virtual_memory()
    print("Current memory usage:")
    print(f"Total: {memory.total / (1024**2):.2f} MB")
    print(f"Available: {memory.available / (1024**2):.2f} MB")
    print(f"Used: {memory.used / (1024**2):.2f} MB")

    print("Freeing RAM storage...")
    psutil.Process().memory_info().rss

    print("Boosting RAM...")
    psutil.Process().nice(psutil.REALTIME_PRIORITY_CLASS)

    memory = psutil.virtual_memory()
    print("New memory usage:")
    print(f"Total: {memory.total / (1024**2):.2f} MB")
    print(f"Available: {memory.available / (1024**2):.2f} MB")
    print(f"Used: {memory.used / (1024**2):.2f} MB")

# Function to remove junk files in a folder with confirmation
def remove_junk_files(folder_path):
    junk_extensions = ['.tmp', '.bak', '.swp', '.~']

    junk_files = []
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            _, ext = os.path.splitext(file_name)
            if ext.lower() in junk_extensions:
                junk_files.append(os.path.join(root, file_name))

    if not junk_files:
        print("No junk files found in the folder.")
        return

    print("Junk files found in the folder:")
    for file_path in junk_files:
        print(file_path)

    choice = input("Do you want to remove the junk files? (y/n): ")
    if choice.lower() == 'y':
        for file_path in junk_files:
            try:
                os.remove(file_path)
                print("Junk file removed:", file_path)
            except Exception as e:
                print("Error removing junk file:", e)
    else:
        print("Junk files removal canceled.")

# Function to display the main menu
def display_menu():
    print("---------- Bit Protect Menu ----------")
    print("1. Scan and compare full system")
    print("2. Scan and delete files in a folder")
    print("3. Scan and delete a file")
    print("4. Free RAM storage and boost RAM")
    print("5. Remove junk files in a folder")
    print("6. Exit")
    print("--------------------------------------")

# Function to display the Bit Protect heading
def display_heading():
    print(r"""
 oooooooooo.   o8o      .                                     .                           .   
`888'   `Y8b  `"'    .o8                                   .o8                         .o8   
 888     888 oooo  .o888oo oo.ooooo.  oooo d8b  .ooooo.  .o888oo  .ooooo.   .ooooo.  .o888oo 
 888oooo888' `888    888    888' `88b `888""8P d88' `88b   888   d88' `88b d88' `"Y8   888   
 888    `88b  888    888    888   888  888     888   888   888   888ooo888 888         888   
 888    .88P  888    888 .  888   888  888     888   888   888 . 888    .o 888   .o8   888 . 
o888bood8P'  o888o   "888"  888bod8P' d888b    `Y8bod8P'   "888" `Y8bod8P' `Y8bod8P'   "888" 
                            888                                                              
                           o888o                                                             
                                                                                              
                                         
    """)

# Load virus hash values from the file hash.txt
with open('hash.txt', 'r') as hash_file:
    virus_hashes = hash_file.read().splitlines()

# Main programloop
while True:
    display_heading()
    display_menu()
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        scan_and_delete(virus_hashes, '/')
    elif choice == '2':
        folder_path = input("Enter the folder path: ")
        scan_and_delete(virus_hashes, folder_path)
    elif choice == '3':
        file_path = input("Enter the file path: ")
       # scan_and_delete_file(file_path, virus_hashes)
    elif choice == '4':
        free_ram_boost()
    elif choice == '5':
        folder_path = input("Enter the folder path: ")
        remove_junk_files(folder_path)
    elif choice == '6':
        print("Exiting Bit Protect...")
        break
    else:
        print("Invalid choice. Please try again.")