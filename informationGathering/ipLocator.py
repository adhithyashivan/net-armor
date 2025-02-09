import requests
import logging
from colorama import Fore, init
from common.constants import ERROR_FETCHING_IP, FAILED_IP_RETRIEVE, UNEXPECTED_IP_ERROR, IP_DETAILS_SUCCESS

init(autoreset=True)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class IPLocator:
    """Class to locate and display information about an IP address."""

    def __init__(self, ip_address):
        """
        Initialize IPLocator with an IP address.
        
        Args:
            ip_address (str): The IP address to locate.
        """
        self.ip_address = ip_address
        self.api_url = f"http://ip-api.com/json/{ip_address}"

    def fetch_ip_details(self):
        """
        Fetch details for the provided IP address from IP-API.

        Returns:
            dict: A dictionary containing IP details if successful, None otherwise.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"{Fore.RED}" + ERROR_FETCHING_IP.format(error=e))
            return None
        except Exception as e:
            logging.error(f"{Fore.RED}" + UNEXPECTED_IP_ERROR.format(error=e))
            return None

    def display_ip_info(self):
        """
        Display the fetched IP details in a formatted manner with colors.
        """
        try:
            details = self.fetch_ip_details()
            if details and details.get('status') == 'success':
                ip_info = "\n".join(
                    f"{Fore.YELLOW}{key.capitalize()}: {Fore.CYAN}{value}"
                    for key, value in details.items() if key != 'status'
                )
                logging.info(f"{Fore.GREEN}" + IP_DETAILS_SUCCESS.format(details=ip_info))
            else:
                logging.error(f"{Fore.RED}" + FAILED_IP_RETRIEVE)
        except Exception as e:
            logging.error(f"{Fore.RED}" + UNEXPECTED_IP_ERROR.format(error=e))

def run_ip_locator(ip_address):
    """
    Run the IP locator with the provided IP address.

    Args:
        ip_address (str): The IP address to locate.
    """
    locator = IPLocator(ip_address)
    locator.display_ip_info()
