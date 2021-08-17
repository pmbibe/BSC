
# Import Module
from tkinter import *
import json
import sys
from web3 import Web3

ABI = """[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"claimRefund","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"claimTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"minTokensBeforeSwap","type":"uint256"}],"name":"MinTokensBeforeSwapUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"tokensSwapped","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"ethReceived","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"tokensIntoLiqudity","type":"uint256"}],"name":"SwapAndLiquify","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"enabled","type":"bool"}],"name":"SwapAndLiquifyEnabledUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"_liquidityFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_maxTxAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_taxFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tAmount","type":"uint256"}],"name":"deliver","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"excludeFromFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"excludeFromReward","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"geUnlockTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"includeInFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"includeInReward","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"isExcludedFromFee","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"isExcludedFromReward","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"time","type":"uint256"}],"name":"lock","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tAmount","type":"uint256"},{"internalType":"bool","name":"deductTransferFee","type":"bool"}],"name":"reflectionFromToken","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"liquidityFee","type":"uint256"}],"name":"setLiquidityFeePercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"maxTxPercent","type":"uint256"}],"name":"setMaxTxPercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_enabled","type":"bool"}],"name":"setSwapAndLiquifyEnabled","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"taxFee","type":"uint256"}],"name":"setTaxFeePercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"swapAndLiquifyEnabled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rAmount","type":"uint256"}],"name":"tokenFromReflection","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalFees","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"uniswapV2Pair","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"uniswapV2Router","outputs":[{"internalType":"contract IUniswapV2Router02","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"unlock","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]"""

def readFile(fileName):
    openFile = open(fileName,'r')
    return openFile.read()

def checksumAddress(tokenAddress):
    return web3.toChecksumAddress(tokenAddress)
def getTokenName():
    return tokenContract.functions.name().call()
def getSymbol():
    return tokenContract.functions.symbol().call()
    
def getConfig(fileName):
    config = readFile(fileName) 
    return json.loads(config)

def getDecimals():
    return tokenContract.functions.decimals().call()
def getBalance(Address):
    return tokenContract.functions.balanceOf(Address).call()

def getTokenAddress():
    global tokenContract,tokenAddress
    tokenAddress = checksumAddress(inputToken.get())
    tokenABI = json.loads(ABI)
    tokenContract = web3.eth.contract(address=tokenAddress, abi=tokenABI)
    decimals = getDecimals() 
    tokenName = getTokenName()
    symbol = getSymbol()
    x = 0
    for wallet in config["Wallet"]:
        if getBalance(wallet['Address']) > 0:
            lbTokenName = Label(root, text = tokenName)
            lbTokenName.grid(column =0, row =x+3)  
            lbTokenName = Label(root, text = wallet['Address'])
            lbTokenName.grid(column =1, row =x+3)
            lbTokenName = Label(root, text = getBalance(wallet['Address'])/10**decimals)
            lbTokenName.grid(column =2, row =x+3)
            lbTokenName = Label(root, text = web3.eth.get_balance(wallet['Address'])/10**18)
            lbTokenName.grid(column =3, row =x+3)
            x = x+1 
def transfer():
    recipientAddress = checksumAddress(txt.get())
    global tokenContract,tokenAddress
    tokenAddress = checksumAddress(inputToken.get())
    tokenABI = json.loads(ABI)
    tokenContract = web3.eth.contract(address=tokenAddress, abi=tokenABI)
    decimals = getDecimals() 
    tokenName = getTokenName()
    symbol = getSymbol()
    x = 0
    for wallet in config["Wallet"]:
        if getBalance(wallet['Address']) > 0:
            try:
                tokenTransfer(wallet['Address'], wallet['Key'], getBalance(wallet['Address']), recipientAddress)
            except Exception:
                pass
def tokenTransfer(Address, Key, amount, recipient):
    nonce = web3.eth.getTransactionCount(Address)
    transfer = tokenContract.functions.transfer(recipient, amount).buildTransaction({
        'chainId':56, 
        'gas': 800000,
        'gasPrice': web3.toWei('5','gwei'), 
        'nonce':nonce
    })
    sign_txn = web3.eth.account.signTransaction(transfer, private_key=Key)
    print(sign_txn)
    web3.eth.sendRawTransaction(sign_txn.rawTransaction) 
def main():
    global root,txt, web3, config, inputToken
    root = Tk()
    root.title("pmbibe")
    root.geometry('1200x500')
    inputToken = Entry(root, width=40)
    inputToken.grid(column =1, row =0)
    txt = Entry(root, width=40)
    txt.grid(column =1, row =1)
    btn = Button(root, text = "Run" , fg = "red", command=getTokenAddress)
    btn.grid(column=2, row=0)
    btn = Button(root, text = "Transfer" , fg = "red", command=transfer)
    btn.grid(column=2, row=1)
    lbl = Label(root, text = "Token Address")
    lbl.grid(column =0, row =0)
    lbl = Label(root, text = "Recipient Address")
    lbl.grid(column =0, row =1)
    lbl1 = Label(root, text = "Token Name")
    lbl1.grid(column =0, row =2)
    lbl2 = Label(root, text = "Wallet Address")
    lbl2.grid(column =1, row =2)
    lbl3 = Label(root, text = "Balance")
    lbl3.grid(column =2, row =2)
    lbl3 = Label(root, text = "Balance BNB")
    lbl3.grid(column =3, row =2)
    bsc = "https://bsc-dataseed.binance.org/"
    web3 = Web3(Web3.HTTPProvider(bsc))
    
    config = getConfig("config.json")
    


    root.mainloop()
main()