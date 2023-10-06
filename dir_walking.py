import os

for root, dirs, files in os.walk(".."):
    abs_root = os.path.abspath(root)
    #print(abs_root)

    if dirs:
        print("Directories")
        for dir_ in dirs:
            print(dir_)

    if files:
        print("Files:")
        for filename in files:
            print(filename)

for root, dirs, files in os.walk("../pythonProject"):
    for file in files:
        if file == 'api_get.py':
            file_path = os.path.join(root, file)
            print(file_path)