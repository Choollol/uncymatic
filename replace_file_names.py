from pathlib import Path

def replace_file_name(path: Path, old_string: str, new_string: str) -> bool:
    """Tries to replace all occurrences of old_string with new_string in path"""
    if old_string in str(path):
        try:
            path.rename(str(path).replace(old_string, new_string))
            return True
        except IOError as e:
            print(e)
    return False

def replace_file_names(abs_path: Path, old_string: str, new_string: str) -> tuple[int, int]:
    files_replaced = 0
    dirs_replaced = 0
    next_dirs = [abs_path]
    while next_dirs:
        path = next_dirs[-1]
        next_dirs.pop()
        files = []
        did_replace = replace_file_name(path, old_string, new_string)
        if did_replace:
            if path.is_dir():
                dirs_replaced += 1
            else:
                files_replaced += 1
        if path.is_dir():
            for sub_dir in path.iterdir():
                if sub_dir.is_dir():
                    next_dirs.append(sub_dir)
                else:
                    files.append(sub_dir)
        next_dirs.extend(files)
    return (dirs_replaced, files_replaced)