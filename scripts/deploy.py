import json
import os
from web3 import Web3



ropson='https://ropsten.infura.io/v3/340c05dbf801409b983bbf521c42e3b3'
al='https://eth-ropsten.alchemyapi.io/v2/MIRYh8RdGpXd4M6pSdl0VTJe7l8zFSEN'
web3 = Web3(Web3.HTTPProvider(al))
print(web3.isConnected())

key=''
account = web3.eth.account.privateKeyToAccount(key)
print(account.address)


path="C:/Users/MSI 1/Desktop/BlockChain/nft/nftBack/brawnie"
os.chdir(path)

with open(f'{os.getcwd()}/build/contracts/NFTMarket.json') as f:
        data = json.load(f)
        
abi=data["abi"]
bytecode=data["bytecode"]


# # # Instantiate and deploy contract
Bank = web3.eth.contract(abi=abi, bytecode='0x'+bytecode)
tax_body={
    'nonce':web3.eth.get_transaction_count(account.address),
    # 'value':web3.toWei(1,'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei'),
}

deplyment=Bank.constructor().buildTransaction(tax_body)
signed_tax=web3.eth.account.sign_transaction(deplyment,key)
result= web3.eth.send_raw_transaction(signed_tax.rawTransaction)

tx_receipt = web3.eth.waitForTransactionReceipt(web3.toHex(result))

print("NFT market  ",tx_receipt.contractAddress)

with open(f'{os.getcwd()}/build/contracts/NFT.json') as f:
        data = json.load(f)
        
abi=data["abi"]
bytecode=data["bytecode"]

Bank = web3.eth.contract(abi=abi, bytecode=bytecode)

tax_body={
    'nonce':web3.eth.get_transaction_count(account.address),
    # 'value':web3.toWei(1,'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei'),
}

deplyment=Bank.constructor(tx_receipt.contractAddress).buildTransaction(tax_body)

signed_tax=web3.eth.account.sign_transaction(deplyment,key)

result= web3.eth.send_raw_transaction(signed_tax.rawTransaction)


tx_receipt = web3.eth.waitForTransactionReceipt(web3.toHex(result))

  
print("NFT  ",tx_receipt.contractAddress)
