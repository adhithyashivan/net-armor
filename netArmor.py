import logging
from utils.promptUtils import parse_tool_choice, prompt_for_ip
from informationGathering.ipLocator import run_ip_locator
from colorama import Fore, init
from common.constants import WELCOME_MESSAGE, TOOL_OPTIONS, INVALID_SELECTION, UNEXPECTED_ERROR

init(autoreset=True)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        logging.info(f"{Fore.GREEN}" + WELCOME_MESSAGE)
        for option in TOOL_OPTIONS:
            logging.info(f"{Fore.YELLOW}" + option)

        tool_choice = parse_tool_choice()

        if tool_choice == 1:
            ip_address = prompt_for_ip()
            run_ip_locator(ip_address)
        else:
            logging.error(f"{Fore.RED}" + INVALID_SELECTION)
    except Exception as e:
        logging.error(f"{Fore.RED}" + UNEXPECTED_ERROR.format(error=e))

if __name__ == "__main__":
    main()
