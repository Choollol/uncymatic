from pathlib import Path
import sys

CYMATICS_PREFIX = "Cymatics - "


def uncymatic(path: Path) -> None:
    if CYMATICS_PREFIX in str(path):
        try:
            path.rename(str(path).replace(CYMATICS_PREFIX, ""))
        except IOError as e:
            print(e)

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
    
    next_dirs = [abs_path]
    while next_dirs:
        path = next_dirs[-1]
        next_dirs.pop()
        dirs = []
        uncymatic(path)
        if path.is_dir():
            for sub_dir in path.iterdir():
                if sub_dir.is_file():
                    next_dirs.append(sub_dir)
                else:
                    dirs.append(sub_dir)
        next_dirs.extend(dirs)


if __name__ == "__main__":
    main()
