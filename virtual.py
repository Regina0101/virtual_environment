import sys
from pathlib import Path
from colorama import Fore, Style

def list_directory(path, indent=""):
    directory = Path(path)

    if not directory.is_dir():
        print(f"{indent}📜{directory.name}")
        return

    print(f"{indent}📦{directory.name}")
    for item in directory.iterdir():
        if item.is_dir() and item.name != ".venv":  # Исключаем папку .venv из вывода
            print(f"{indent} ┣ 📂{item.name}")
            list_directory(item, indent + " ┃ ┣ ")
        elif item.is_file():
            print(f"{indent} ┗ 📜{item.name}")

def main():
    if len(sys.argv) != 2:
        print("Пожалуйста, укажите путь к директории как аргумент командной строки.")
        return

    path = sys.argv[1]
    list_directory(path)

if __name__ == "__main__":
    main()
