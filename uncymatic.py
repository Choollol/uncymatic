from pathlib import Path
import sys

import replace_file_names

CYMATICS_PREFIX = "Cymatics - "


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} 'absolute directory'")
        return
    abs_path = Path(u"\\\\?\\" + sys.argv[1])
    if not abs_path.is_dir():
        print("Please enter a valid path.")
        return
    if not abs_path.is_absolute():
        print("Please enter an absolute path.")
        return
    
    dirs_replaced, files_replaced = replace_file_names.replace_file_names(abs_path, CYMATICS_PREFIX, "")
    
    print(f"Directory names replaced: {dirs_replaced}")
    print(f"File names replaced: {files_replaced}")


if __name__ == "__main__":
    main()
