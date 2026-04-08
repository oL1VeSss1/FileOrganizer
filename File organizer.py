import  os
import shutil
from pathlib import Path


def your_path():
    while True:
        folder = input('\nWrite the path to the folder(example:C:/users/user/Desktop): ')
        if not os.path.exists(folder):
            print('\nThis path does not exist. Do you want to create this path?: \nYes \nNo\n')
            answer = input('\nWrite your answer: ')
            if answer == 'Yes':
                try:
                    os.makedirs(folder)
                except Exception as a:
                    print('\nError', a) 
                print('\nDo you want to create another folder?: \nYes \nNo\n')
                while True:
                    x = input('\nWrite your answer: ')
                    if x == 'Yes':
                      try:
                        os.makedirs(input('\nEnter the path you want to create: '))  
                      except Exception as f:
                        print('\nError', f)
                      else:
                        print('\nDo you want to create another folder?: \nYes \nNo')
                        g = input('\nWrite your answer: ')
                        if g == 'Yes':
                            pass
                        elif g == 'No':
                            break  
                        else:
                            print('\nIt looks like you entered the wrong answer or wrote the answer incorrectly, please try again.') 
                    elif x == 'No':
                        break  
                    else:
                        print('\nIt looks like you entered the wrong answer or wrote the answer incorrectly, please try again.')               
            elif answer == 'No':
                pass
            else:
                print('\nIt looks like you entered the wrong answer or wrote the answer incorrectly, please try again.')
        else:
            print(os.listdir(folder))
            break

def working_with_files():
    print('\nSelect options: ''\n1. Move a file from one folder to another', '\n2. Sort folder')
    n = input('\nWrite your answer: ')
    while True:
        if n == '1':
            source = input('\nWrite the source path: ')
            destination = input('\ndestination: ')
            try:
                shutil.move(source, destination)
                print('The file has been moved')
            except Exception as j:
                print("Error:", j)
                pass
            else:
                break
        if n == '2':
            print('\nHow do you want to sort files?: ', '\n1. By size', '\n2. By file extensions', '\n3. Alphabetically')
            q = input('\nWrite your answer: ')
            if q == '1':
                    path = input('\nWrite your path: ')
                    try:
                        files = os.listdir(path)
                        files.sort(key=lambda x: os.path.getsize(os.path.join(path, x)))
                        print('\n'.join(files))
                        break
                    except Exception as l:
                        print('\nError', l)
                        pass
            elif q == '2':
                path = input('\nWrite your path: ')
                try:
                    files = os.listdir(path)
                    file_types = {
                        "Images": [".jpg", ".png", ".jpeg", ".ico", ".gif", ".webp", ".bmp"],
                        "Documents": [".pdf", ".docx", ".txt", ".csv"],
                        "Music": [".mp3", ".wav"],
                        "Videos": [".mp4", ".avi"],
                        "Archives": [".zip", ".rar"],
                        "Executable files": [".exe", ".dll", ".com", ".bat"],
                        "Programming languages": [".py", ".js", ".ts", ".java", ".cpp", ".cs", ".rs", ".go"]
                    }
                    def get_category(filename):
                        ext = os.path.splitext(filename)[1].lower().strip()
                        for category, extensions in file_types.items():
                            if ext in extensions:
                                return category
                        return "Other"
                    grouped = {}
                    for file in files:
                        full_path = os.path.join(path, file)
                        if os.path.isdir(full_path):
                            continue
                        ext = os.path.splitext(file)[1]
                        print(file, "->", ext) 
                        category = get_category(file)
                        if category not in grouped:
                            grouped[category] = []
                        grouped[category].append(file)
                    for category in grouped:
                        print(f"\n{category}:")
                        for f in grouped[category]:
                            print(f"  {f}")

                    break
                except Exception as c:
                    print('\nError', c)
            elif q == '3':
                    path = input('\nWrite your path: ')
                    print('\nHow do you want to sort the files?: ', '\n1. A-Z', '\n2. Z-A')
                    choice = input('\nWrite your answer: ')
                    if choice == '1':
                        try:
                            files = os.listdir(path)
                            files.sort()
                            print(files)
                        except Exception as d:
                            print('\nError', d)
                            pass
                        else:
                            break                      
                    elif choice == '2':
                        try:
                            files = os.listdir(path)
                            files.sort(reverse=True)
                            print(files)
                        except Exception as w:
                            print('\nError', w)
                    else:
                        print('\nThere is no such choice')
                        pass
        else:
            print('\nThere is no such choice')
            pass
def your_choice():
    print('Hello, this is a program for working with files.')
    print('\nChoose what you want: ', '\n1. Working with folders (searching for all files in a folder, creating, etc.)', '\n2. Transferring and sorting files ')
    select_function = input('\nWrite your answer: ')
    if select_function == '1':
        your_path()
    elif select_function == '2':
        working_with_files()
    else:
        print('\nThere is no such choice')
your_choice()

            




        

      


