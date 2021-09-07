from web3 import Web3
from eth_abi import encode_abi
import sha3
bsc = "https://bsc-dataseed1.defibit.io"
web3 = Web3(Web3.HTTPProvider(bsc))
UniABI = '''[
                {
                    "inputs":[
                        
                    ],
                    "name":"RANDOM_NUMBER_X82",
                    "outputs":[
                        {
                            "internalType":"uint256",
                            "name":"",
                            "type":"uint256"
                        }
                    ],
                    "stateMutability":"view",
                    "type":"function"
                }
            ]
        '''
presaleAddress = "0x538F3BD1B4d8DEa550C62C4E68427D093676961A"
presaleA = web3.eth.contract(address=presaleAddress, abi=UniABI)
radomNumber = (presaleA.functions.RANDOM_NUMBER_X82().call())
result = encode_abi(['address', 'uint'], ['0x55069CB4edEE3A646ca8A257067ce370E85e04d4', radomNumber])
k = sha3.keccak_256()
k.update(result)
print('0x0d052dfd0000000000000000000000000000000000000000000000000000000000000000'+k.hexdigest())
