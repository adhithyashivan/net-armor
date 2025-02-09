import argparse
import logging

def parse_tool_choice():
    """
    Prompt the user to choose a tool.

    Returns:
        int: The tool choice made by the user.
    """
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            return choice
        except ValueError:
            logging.error("Invalid input. Please enter a number.")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

def prompt_for_ip():
    """
    Prompt the user to enter an IP address.

    Returns:
        str: The IP address entered by the user.
    """
    try:
        ip_address = input("Please enter the IP address: ")
        return ip_address
    except Exception as e:
        logging.error(f"An unexpected error occurred while entering IP address: {e}")

def parse_arguments():
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    try:
        parser = argparse.ArgumentParser(description="Toolbox for various utilities.")
        parser.add_argument("tool", help="Tool to use", choices=["1"], type=int)
        parser.add_argument("ip", help="IP address to locate", nargs='?', default=None)
        return parser.parse_args()
    except Exception as e:
        logging.error(f"An unexpected error occurred while parsing arguments: {e}")
