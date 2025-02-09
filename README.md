
# Net Armor

[![Python 3.x](https://img.shields.io/badge/python-3.x-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPLv3-red.svg)](https://raw.githubusercontent.com/adhithyashivan/net-armor/refs/heads/main/LICENSE) [![LinkedIn](https://img.shields.io/badge/linkedin-@adhithyasivanesh-blue.svg)](https://www.linkedin.com/in/adhithyashivan/)

Net Armor is a unified web security toolkit that provides various utilities for cybersecurity professionals. Currently, it includes an IP Locator tool that fetches and displays information about a provided IP address. Net Armor is designed to be your go-to tool for comprehensive web security analysis and operations.


## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages: `requests`, `argparse`, `colorama`

You can install the required packages using `pip`:

```bash
pip install requests argparse colorama
```

### Usage

1. **Clone the repository:**

```bash
git clone https://github.com/adhithyashivan/web-security-tools.git
```

2. **Run the `netArmor.py` script:**

```bash
python3 netArmor.py
```

### Tools

#### 1. IP Locator

The IP Locator tool fetches and displays information about a provided IP address using the IP-API service.

### Example

```bash
python3 netArmor.py
```

Output:

```
2025-02-09 12:28:10,422 - INFO - Welcome to NET ARMOR! Please select a tool:
2025-02-09 12:28:10,422 - INFO - 1. IP Locator
Enter the number of your choice: 1
Please enter the IP address: 8.8.8.8
2025-02-09 12:28:13,993 - INFO - IP Details:
Country: United States
Countrycode: US
Region: VA
Regionname: Virginia
City: Ashburn
Zip: 20149
Lat: 39.03
Lon: -77.5
Timezone: America/New_York
Isp: Google LLC
Org: Google Public DNS
As: AS15169 Google LLC
Query: 8.8.8.8
...
```

2. **Run the `netArmor.py` script:**

```bash
python3 netArmor.py
```

#### 2. Sub Domain Extractor

The Sub Domain Extractor tool fetches and displays information about sub domains from the provided domain using crt.sh

### Example

```bash
python3 netArmor.py
```

Output:

```
2025-02-09 14:53:46,287 - INFO - Welcome to NET ARMOR! Please select a tool:
2025-02-09 14:53:46,288 - INFO - 1. IP Locator
2025-02-09 14:53:46,289 - INFO - 2. Sub Domain Extractor
Enter the number of your choice: 2
Please enter the domain name: example.com
2025-02-09 14:53:53,528 - INFO - Sub DOmains:
example.com
*.example.com
...
```

### Extending the Toolbox

To add a new tool:
1. Create a new script file in the `toolbox` directory.
2. Implement the tool’s logic in the new script.
3. Update `netArmor.py` to include the new tool in the prompt and handle user input accordingly.

### License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

- [IP-API](http://ip-api.com) for providing the IP geolocation API.
- [Colorama](https://pypi.org/project/colorama/) for colored terminal text.
- [Argparse](https://docs.python.org/3/library/argparse.html) for argument parsing.