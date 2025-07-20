from pathlib import Path

def get_files_in_directory(directory_path):
    #convert the relative path to an absolute path
    directory_path = Path(directory_path).resolve()
    #convert to Path object
    directory = Path(directory_path)
    # validate that it is a directory
    if not directory.is_dir():
        raise ValueError(f"{directory_path} is not a valid directory.")
    return [file for file in directory.iterdir() if file.is_file()
            and not file.name.startswith('.')]
    

    