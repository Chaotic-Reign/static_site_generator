import os, shutil

def remove_directory_contents(directory_path):
    contents = os.listdir(directory_path)
    for item in contents:
        item_path = os.path.join(directory_path, item)
        if os.path.exists(item_path):
            if os.path.isfile(item_path):
                os.remove(item_path)
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)

def copy_files_from_directory(old_directory, new_directory):
    to_copy = os.listdir(old_directory)
    for item in to_copy:
        src_path = os.path.join(old_directory, item)
        dst_path = os.path.join (new_directory, item)
        if os.path.isdir(src_path):
            if not os.path.exists(dst_path):
                os.mkdir(dst_path)
            copy_files_from_directory(src_path, dst_path)
        if os.path.isfile(src_path):
            if not os.path.exists(dst_path):
                shutil.copy(src_path, new_directory)

def static_to_public(old_directory, new_directory):
    remove_directory_contents(new_directory)
    copy_files_from_directory(old_directory, new_directory)