import os 

def make_dir(file_path):
    if os.path.exists(file_path):
        pass
    else : 
        os.makedirs(file_path)
    #
#