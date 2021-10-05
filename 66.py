# Import Module
from tkinter import *
import sys
import json
from web3 import Web3
import csv


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
    with open('config.csv') as csv_file:
        config = csv.reader(csv_file, delimiter=',')
        for wallet in config:
            if getBalance(checksumAddress(wallet[0])) > 0:
                lbTokenName = Label(root, text = tokenName)
                lbTokenName.grid(column =0, row =x+3)  
                lbTokenName = Label(root, text = checksumAddress(wallet[0]))
                lbTokenName.grid(column =1, row =x+3)
                lbTokenName = Label(root, text = getBalance(checksumAddress(wallet[0]))/10**decimals)
                lbTokenName.grid(column =2, row =x+3)
                lbTokenName = Label(root, text = web3.eth.get_balance(checksumAddress(wallet[0]))/10**18)
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
    with open('config.csv') as csv_file:
        config = csv.reader(csv_file, delimiter=',')
        for wallet in config:
            if getBalance(checksumAddress(wallet[0])) > 0:
                try:
                    tokenTransfer(checksumAddress(wallet[0]), wallet[1], getBalance(checksumAddress(wallet[0])), recipientAddress)
                except Exception as e:
                    lblErr0 = Label(root, text = str(e))
                    lblErr0.grid(column =5, row =1)
                    pass
def tokenTransfer(Address, Key, amount, recipient):
    try:
        nonce = web3.eth.getTransactionCount(Address)
        transfer = tokenContract.functions.transfer(recipient, amount).buildTransaction({
            'chainId':56, 
            'gas': 3000000,
            'gasPrice': web3.toWei('5','gwei'), 
            'nonce':nonce
        })
        sign_txn = web3.eth.account.signTransaction(transfer, private_key=Key)
        web3.eth.sendRawTransaction(sign_txn.rawTransaction) 
    except Exception as e:
        lblErr = Label(root, text = str(e))
        lblErr.grid(column =5, row =0)
        pass
def waitForTransactionReceipt(transaction_hash):
    responseCode = 1
    while responseCode > 0:
        try:
            web3.eth.get_transaction_receipt(transaction_hash)
            responseCode = 0
        except Exception as e:
            pass
def TransferBNB():
    Address = checksumAddress(inputAddressFrom.get())
    Key = inputKey.get()
    value = int(float(inputAmountBNB.get()) * 10**18)
    recipient = checksumAddress(inputAddressTo.get())
    try:
        nonce = web3.eth.getTransactionCount(Address)
        txTransferBNB = {
            'to': recipient,
            'value': value,
            'chainId':56,
            'gas': 3000000,
            'gasPrice': web3.toWei('5','gwei'), 
            'nonce':nonce
        }
        sign_txn = web3.eth.account.signTransaction(txTransferBNB, private_key=Key)
        waitForTransactionReceipt(web3.eth.sendRawTransaction(sign_txn.rawTransaction))
        lblNotice = Label(root, text = "Done")
        lblNotice.grid(column =2, row =3)        
    except Exception as e:
        lblErr = Label(root, text = str(e))
        lblErr.grid(column =5, row =0)
        pass      
def main():
    global root,txt, web3, config, inputToken, inputAddressFrom, inputAddressTo, inputKey, inputAmountBNB
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
    lbl = Label(root, text = "Transfer BNB From")
    lbl.grid(column =0, row =2)
    inputAddressFrom = Entry(root, width=40)
    inputAddressFrom.grid(column =1, row =2)
    lbl = Label(root, text = "Private Key")
    lbl.grid(column =0, row =3)
    inputKey = Entry(root, width=40)
    inputKey.grid(column =1, row =3)
    lbl = Label(root, text = "Transfer BNB To")
    lbl.grid(column =0, row =4)
    inputAddressTo = Entry(root, width=40)
    inputAddressTo.grid(column =1, row =4)
    lbl = Label(root, text = "Amount BNB")
    lbl.grid(column =0, row =5)
    inputAmountBNB = Entry(root, width=40)
    inputAmountBNB.grid(column =1, row =5)
    btn = Button(root, text = "Transfer BNB" , fg = "red", command=TransferBNB)
    btn.grid(column=2, row=2)
    lbl1 = Label(root, text = "Token Name")
    lbl1.grid(column =0, row =6)
    lbl2 = Label(root, text = "Wallet Address")
    lbl2.grid(column =1, row =6)
    lbl3 = Label(root, text = "Balance")
    lbl3.grid(column =2, row =6)
    lbl3 = Label(root, text = "Balance BNB")
    lbl3.grid(column =3, row =6)
    bsc = "https://bsc-dataseed.binance.org/"
    web3 = Web3(Web3.HTTPProvider(bsc))
    root.mainloop()
main()  
