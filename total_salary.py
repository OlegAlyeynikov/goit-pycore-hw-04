from typing import Tuple

def total_salary(path: str) -> Tuple[int, float]:
    """
    Calculates the total and average salary of developers from a file.

    Each line in the file must contain a developer's name and their salary
    separated by a comma (e.g., "John Doe,3000").

    Args:
        path (str): Path to the text file containing salary data.

    Returns:
        Tuple[int, float]: A tuple where the first value is the total salary,
                           and the second is the average salary.
                           Returns (0, 0.0) if the file is missing or empty.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            total = 0
            count = 0

            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    _, salary_str = line.split(",")
                    total += int(salary_str)
                    count += 1
                except ValueError:
                    print(f"Invalid line format skipped: {line}")
                    continue

            if count == 0:
                return 0, 0.0

            average = total / count
            return total, average

    except FileNotFoundError:
        print(f"File not found: {path}")
        return 0, 0.0
    except Exception as e:
        print(f"Error while processing the file: {e}")
        return 0, 0.0


if __name__ == "__main__":
    total, average = total_salary("salary_file.txt")
    print(f"Total salary: {total}, Average salary: {average:.2f}")
