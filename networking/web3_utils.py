from web3 import Web3

# Connect to the Goerli network
def connect_to_web3():
    infura_url = 'https://goerli.infura.io/v3/22348f916b8944be930ac83951a7a245'
    return Web3(Web3.HTTPProvider(infura_url))

# Instantiate the web3 object
web3 = connect_to_web3()