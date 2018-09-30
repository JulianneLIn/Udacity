import os
def rename_files():
    #1 get files
    file_list = os.listdir(r"/Users/bestlin/Desktop/python2/2018.9.9/prank")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is" + saved_path)
    os.chdir(r"/Users/bestlin/Desktop/python2/2018.9.9/prank")
    #2 rename files
    for file_name in file_list:
        os.renames(file_name,file_name.strip("1234567890"))
    os.chdir(saved_path)

rename_files()
