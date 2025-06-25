from typing import List, Dict


def get_cats_info(path: str) -> List[Dict[str, str]]:
    """
    Reads a file containing cat information and returns a list of dictionaries.

    Each line in the file must contain a cat's unique ID, name, and age,
    separated by commas. Example:
        60b90c1c13067a15887e1ae1,Tayson,3

    Args:
        path (str): Path to the text file containing cat data.

    Returns:
        List[Dict[str, str]]: A list of dictionaries where each dictionary has keys
                              "id", "name", and "age" representing a single cat.
    """
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) != 3:
                    print(f"Invalid line format skipped: {line}")
                    continue

                cat_id, name, age = parts
                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }
                cats.append(cat_info)

        return cats

    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []


if __name__ == "__main__":
    cats_info = get_cats_info("cats_file.txt")
    print(cats_info)
