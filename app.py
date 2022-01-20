
from re import A
from flask import Flask
import json
import os
from web3 import Web3

app=Flask(__name__)

NFTaddress="0xBa15C4fbb5e84C28e53381325c0F9082B9e50FBa"
NFTmarket="0xbA8a346B37bbCCE9E316117435472c0A96820099"
# client = ipfshttpclient.connect()

al='https://eth-ropsten.alchemyapi.io/v2/MIRYh8RdGpXd4M6pSdl0VTJe7l8zFSEN'
web3 = Web3(Web3.HTTPProvider(al))

key='0x05ba5a15a4ac68580fe2a9c6980d869aa47c6c983f1b0f21b14713477bbe6970'
# account = web3.eth.account.privateKeyToAccount(key)
# print(account.address)

# path="C:/Users/MSI 1/Desktop/BlockChain/nft/nftBack/brawnie"
# os.chdir(path)

with open(f'{os.getcwd()}/build/contracts/NFT.json') as f:
        NFTdata = json.load(f)

with open(f'{os.getcwd()}/build/contracts/NFTMarket.json') as f:
        Marketdata = json.load(f)
        
NFTabi=NFTdata["abi"]
NFTmarket_abi=Marketdata["abi"]

NFTcontract = web3.eth.contract(
    address=NFTaddress,
    abi=NFTabi,
)

NFTmarket_contract = web3.eth.contract(
    address=NFTmarket,
    abi=NFTmarket_abi,
)



@app.route('/')
def index():
    return {
        "balance": "",
    }

@app.route('/create_wallet')
def createAcccount():
    account= web3.eth.account.create()
    print(account)
    return {
        "account address ": account,
        
    }

@app.route('/import_wallet/<private_key>')
def importAcccount(private_key):
    account = web3.eth.account.privateKeyToAccount(private_key)
    return {
        "account address ": account.address,
    }

@app.route('/fetch')
def fatch():
    data=NFTmarket_contract.functions.fetchMarketItems().call()
    details=NFTcontract.functions.tokenURI(3).call()
    print(details)
    return {
        "data": data,
        "details":details
    }

if __name__=="__main__":
    app.run(debug=True)