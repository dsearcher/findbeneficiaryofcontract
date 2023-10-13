# Ethereum Address Beneficiary Lookup

This Python script allows you to determine the beneficiary of Ethereum contracts and update a CSV file with the beneficiary addresses. It works with both contracts and Externally Owned Accounts (EOAs).

## Prerequisites

#### Before running the script, ensure you have the following prerequisites installed:

- Python
- Web3.py (Python library for Ethereum interaction)
- An Ethereum node or access to a Web3 provider (in this example, I'm using Infura)
- A CSV file named `addresses.csv` with Ethereum addresses in the "A" column.

## Setup

1. Install the required Python libraries using pip:

   ```bash
   pip install web3

2. Create an Infura project and obtain your API key. Replace 'https://arbitrum-mainnet.infura.io/v3/insert_your_Web3_API_Key_here' with your Infura project URL in the script. You can create it here: https://app.infura.io/dashboard

3. Prepare the contract_abi.json file, which should contain the ABI (Application Binary Interface) of the contract you want to interact with. You can obtain this ABI from the contract developer or from an Etherscan-like platform. I've added code of the "L2GraphTokenLockWallet" ABI contract to the file contract_abi.json

#### Ensure you have a CSV file named addresses.csv with Ethereum addresses in the "A" column.

## Usage
1. Run the script:

python script.py

1. The script will process each address in the addresses.csv file. For contract addresses, it will fetch the beneficiary using the provided ABI and write it to the "B" column in the CSV file. For EOAs, it will simply copy the same address to the "B" column.

2. The updated data will be saved in the same addresses.csv file.

## License
This script is provided under the MIT License.

#### Note: Be sure to take a backup of your addresses.csv file before running the script as it will be updated.
#### I didn't add any checkers, so If you try to run this script multiple times with the same .csv fine it will keep adding addresses with each iteration into this file.
