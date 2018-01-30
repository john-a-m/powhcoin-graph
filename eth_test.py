import json

from web3 import IPCProvider, Web3
from web3.contract import ConciseContract

ENDPOINT = '/home/john/.ethereum/geth.ipc'
ADDRESS = '0xA7CA36F7273D4d38fc2aEC5A454C497F86728a7A'

with open('abi.json') as f:
    abi = json.load(f)

w3 = Web3(IPCProvider(ENDPOINT))

contract = w3.eth.contract(ADDRESS, abi=abi, ContractFactoryClass=ConciseContract)

contract.buyPrice()

