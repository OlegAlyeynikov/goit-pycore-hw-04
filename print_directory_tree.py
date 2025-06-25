import sys
from pathlib import Path
from colorama import init, Fore, Style


def print_directory_tree(path: Path, prefix: str = "") -> None:
    """
    Recursively prints the structure of the given directory with colored output.

    Args:
        path (Path): The directory path to display.
        prefix (str): Prefix used for indentation.
    """
    try:
        for item in sorted(path.iterdir()):
            if item.is_dir():
                print(f"{prefix}{Fore.BLUE}{item.name}{Style.RESET_ALL}")
                print_directory_tree(item, prefix + " ┃ ")
            else:
                print(f"{prefix}{Fore.GREEN}{item.name}{Style.RESET_ALL}")
    except PermissionError:
        print(f"{prefix}{Fore.RED}Permission denied: {item}{Style.RESET_ALL}")


def main() -> None:
    """
    Main function that reads the directory path from command-line arguments
    and prints its structure using colorama.
    """
    init(autoreset=True)

    if len(sys.argv) != 2:
        print(f"{Fore.RED}Usage: python hw03.py <directory_path>{Style.RESET_ALL}")
        sys.exit(1)

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(f"{Fore.RED}Error: The path does not exist.{Style.RESET_ALL}")
        sys.exit(1)

    if not directory_path.is_dir():
        print(f"{Fore.RED}Error: The path is not a directory.{Style.RESET_ALL}")
        sys.exit(1)

    print(f"{Fore.YELLOW}Directory structure of: {directory_path}{Style.RESET_ALL}\n")
    print_directory_tree(directory_path)


if __name__ == "__main__":
    main()
