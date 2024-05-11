import sys
from pathlib import Path
from colorama import init, Fore # type: ignore

init(autoreset=True)


def display_directory_structure(directory_path, indent=0):
    path = Path(directory_path)

    if not path.exists() or not path.is_dir():
        print(Fore.RED + f"Path '{directory_path}' does not exist or is not a directory.")
        return

    print(" " * indent + Fore.BLUE + f"{path.name}/")

    for item in path.iterdir():
        if item.is_dir():
            print(" " * (indent + 2) + Fore.CYAN + f"{item.name}/")
            display_directory_structure(item, indent + 4)
        elif item.is_file():
            print(" " * (indent + 2) + Fore.GREEN + f"{item.name}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "You need to specify the path to the directory.")
        sys.exit(1)

    directory_path = sys.argv[1]

    display_directory_structure(directory_path)