import requests
import logging
from colorama import Fore, init
from common.constants import ERROR_FETCHING_SUBDOMAIN, FAILED_SUB_DOMAIN_RETRIEVE, UNEXPECTED_ERROR, SUB_DOMAIN_DETAILS_SUCCESS

init(autoreset=True)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SubDomainExtractor:
    """Class to locate and display information about sub domains."""

    def __init__(self, domain):
        """
        Initialize SubDomainExtractor with a domain.
        
        Args:
            domain (str): The Domain to be enumerated.
        """
        self.domain = domain
        self.api_url = f"https://crt.sh/?q=%.{domain}&output=json"

    def fetch_sub_domains(self):
        """
        Fetch sub domains for the provided domain using crt.sh

        Returns:
            list: A sorted list of subdomains.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            if(response.status_code == 200):
                subdomains = set()
                for entry in response.json():
                    subdomains.add(entry['name_value'].split('\n')[0])
                    return sorted(subdomains)
            else:
                return []
        except requests.RequestException as e:
            logging.error(f"{Fore.RED}" + ERROR_FETCHING_SUBDOMAIN.format(error=e))
            return None
        except Exception as e:
            logging.error(f"{Fore.RED}" + UNEXPECTED_ERROR.format(error=e))
            return None

    def display_sub_domains(self):
        """
        Display the fetched Sub domains in a formatted manner with colors.
        """
        try:
            subdomains = self.fetch_sub_domains()
            if subdomains:
                logging.info(f"{Fore.GREEN}" + SUB_DOMAIN_DETAILS_SUCCESS.format(details=self.domain))
                for subdomain in subdomains:
                    print(Fore.CYAN + subdomain)
            else:
                logging.error(f"{Fore.RED}" + FAILED_SUB_DOMAIN_RETRIEVE)
        except Exception as e:
            logging.error(f"{Fore.RED}" + UNEXPECTED_ERROR.format(error=e))

def run_sub_domain_enumerator(domain):
    """
    Run the sub domain enumerator with the provided domain.

    Args:
        domain (str): The domain to be enumerated.
    """
    locator = SubDomainExtractor(domain)
    locator.display_sub_domains()
