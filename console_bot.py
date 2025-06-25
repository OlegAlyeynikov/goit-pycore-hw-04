from typing import Tuple, List, Dict


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """
    Parses the user's input into a command and its arguments.

    Args:
        user_input (str): Raw input from the user.

    Returns:
        Tuple[str, List[str]]: A tuple containing the command and list of arguments.
    """
    parts = user_input.strip().split()
    if not parts:
        return "", []
    command = parts[0].lower()
    args = parts[1:]
    return command, args


def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """
    Adds a new contact to the phonebook.

    Args:
        args (List[str]): [name, phone]
        contacts (Dict[str, str]): The contact storage.

    Returns:
        str: Result message.
    """
    if len(args) != 2:
        return "Usage: add <name> <phone>"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """
    Updates an existing contact's phone number.

    Args:
        args (List[str]): [name, new_phone]
        contacts (Dict[str, str]): The contact storage.

    Returns:
        str: Result message.
    """
    if len(args) != 2:
        return "Usage: change <name> <new_phone>"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Contact not found."


def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    """
    Shows the phone number for the given contact name.

    Args:
        args (List[str]): [name]
        contacts (Dict[str, str]): The contact storage.

    Returns:
        str: Result message.
    """
    if len(args) != 1:
        return "Usage: phone <name>"
    name = args[0]
    if name in contacts:
        return contacts[name]
    return "Contact not found."


def show_all(contacts: Dict[str, str]) -> str:
    """
    Shows all contacts in the phonebook.

    Args:
        contacts (Dict[str, str]): The contact storage.

    Returns:
        str: Formatted list of all contacts.
    """
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main() -> None:
    """
    Main interactive loop for the assistant bot.
    """
    contacts: Dict[str, str] = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["exit", "close"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
