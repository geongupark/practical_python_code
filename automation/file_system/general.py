import os
import shutil

# mkdir


def create_folder(directory: str):
    """
    Create folder (mkdir)

    Args:
        directory (str): Path of directory want to make.
    """
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Creating directory. " + directory)


# Checking exetension


def is_allowed_file(file_name: str, allowed_extensions: list):
    """
    Method For checking exetension

    Args:
        file_name (str): file name
        allowed_extensions (list): Allowed exetension list

    Returns:
        bool : Is allowed file
    """
    allowed_extensions = set(allowed_extensions)
    return "." in file_name and file_name.rsplit(".", 1)[1] in allowed_extensions


def is_python_file(file_name: str):
    """
    To check if it is python file.

    Args:
        file_name (str): file name

    Returns:
        bool : Is python file
    """
    return is_allowed_file(file_name, ["py"])


def is_image_file(file_name: str):
    """
    To check if it is image file.

    Args:
        file_name (str): file name

    Returns:
        bool : Is image files
    """
    return is_allowed_file(file_name, ["jpg", "png", "jpeg", "gif"])


# ls


def ls_only_file(target_path: str):
    """
    Get only file list in current path

    Args:
        target_path (str): target directory

    Returns:
        list : file list
    """
    return [
        file
        for file in os.listdir(target_path)
        if os.path.isfile(os.path.join(target_path, file))
    ]


def ls_only_dir(target_path: str):
    """
    Get only dir list in current path

    Args:
        target_path (str): target directory

    Returns:
        list : dir list
    """
    return [
        dir
        for dir in os.listdir(target_path)
        if os.path.isdir(os.path.join(target_path, dir))
    ]


def traversing_dir_for_file(target_path: str, target_condition: function):
    """
    Get file list that are target exetension below the target path. (recursive)

    Args:
        target_path (str): target path
        target_condition (function): exetension function

    Returns:
        list : target list
    """
    matched_files = []
    for root, dirs, files in os.walk(target_path):
        for file in files:
            file_full_path = os.path.join(root, file)
            if target_condition(file_full_path):
                matched_files.append(file_full_path)
    return matched_files


# cp


def copy_file(src_file: str, dst_path: str):
    """
    Copy the file to target path

    Args:
        src_file (str): source file
        dst_path (str): dest path
    """
    shutil.copy(src_file, dst_path)


# remove


def remove_file(target_file: str):
    """
    Remove the target file

    Args:
        target_file (str): target file
    """
    if os.path.exists(target_file):
        os.remove(target_file)


def remove_folder(target_path: str):
    """
    Remove the target folder

    Args:
        target_path (str): target folder
    """
    # "/" is danger
    if target_path.startswith("/"):
        print(target_path)
        return
    if os.path.exists(target_path):
        shutil.rmtree(target_path)


if __name__ == "__main__":
    remove_folder("./new_folder")

    # search img files
    img_files = traversing_dir_for_file("../", is_image_file)

    # create new dir
    create_folder("new_folder/images")

    # copy img files to new dir
    for img_file in img_files:
        try:
            copy_file(img_file, "new_folder/images")
        except shutil.SameFileError:
            continue
