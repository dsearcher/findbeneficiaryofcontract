import csv
import json

from web3 import Web3

# Connect to an Arbitrum node. Change "insert_your_Web3_API_Key_here" to your API key that you can get for free from https://app.infura.io/dashboard. 
# In this example I'm using Arbitrum, but for Ethereum it will be similar(https://mainnet.infura.io/v3/insert_your_Web3_API_Key_here)
web3 = Web3(Web3.HTTPProvider('https://arbitrum-mainnet.infura.io/v3/insert_your_Web3_API_Key_here'))

def is_contract(address):
# Check if the address has bytecode
  checksum_address = web3.to_checksum_address(address)  # Convert to checksum address
  bytecode = web3.eth.get_code(checksum_address)
  return len(bytecode) > 2

def find_beneficiary(contract_address):
  # Load the contract ABI
  with open('contract_abi.json', 'r') as file:
    contract_abi = json.load(file)

# Create a contract instance
    contract = web3.eth.contract(address=web3.to_checksum_address(contract_address), abi=contract_abi)

 # Call the contract function to get the beneficiary address
    beneficiary = contract.functions.beneficiary().call()

    return beneficiary

      # Read addresses from column "A" inside addresses.csv
data = []
with open('addresses.csv', 'r') as file:
  reader = csv.reader(file)
  for row in reader:
      address = row[0]
      is_contract_address = is_contract(address)
      if is_contract_address:
          beneficiary = find_beneficiary(address)
          row.append(beneficiary)  # Append beneficiary address to the row
      else:
        row.append(address)  # If it's an EOA, append the same address to the row
      data.append(row)

    # Write the updated data back to the addresses.csv file
with open('addresses.csv', 'w', newline='') as file:
      writer = csv.writer(file)
      writer.writerows(data)

# I didn't add any checkers, so If you try to run this script multiple times with the same .csv fine it will keep adding addresses with each iteration into this file.
