
from web3 import Web3
from eth_account import Account
from eth_account.signers.local import LocalAccount


SharesV1Address = "0xCF205808Ed36593aa40a44F10c7f7C2F67d4A4d4"
RpcURL = "https://developer-access-mainnet.base.org"  # "https://mainnet.base.org"  # "https://base.blockpi.network/v1/rpc/public"
AbiFile = "sharesv1.abi"
ChainID = 8453
MaxFeePerGas = int(130e9)  # 130 gwei
MaxPriorityFeePerGas = int(120e9)  # 120 gwei
GasUnits = int(90000)


def main():
    abi = open(AbiFile, "r").read()

    print()
    print("##############################################################")
    print("##                                                          ##")
    print("##                         Welcome                          ##")
    print("##                                                          ##")
    print("##############################################################")
    print("##                                                          ##")
    print("##   This script will generate a raw signed transaction     ##")
    print("## to onboard to friend.tech. Sharing this signed tx will   ##")
    print("## allow us to onboard you in a priviledged manner, while   ##")
    print("## maintaining the security of your account.                ##")
    print("##                                                          ##")
    print("##   We never see your private key, and can only broadcast  ##")
    print("## your signed transaction.                                 ##")
    print("##                                                          ##")
    print("##############################################################")
    print("##")
    pk = input("## Paste your private key here: ")
    
    web3: Web3 = Web3(Web3.HTTPProvider(RpcURL))
    SharesV1Contract = web3.eth.contract(address=SharesV1Address, abi=abi)
    user: LocalAccount = Account.from_key(pk)

    onboard = SharesV1Contract.functions.buyShares(user.address, 1).build_transaction(
        {
            "value": 0,
            "chainId": ChainID,
            "maxFeePerGas": MaxFeePerGas,
            "gas": GasUnits,
            "maxPriorityFeePerGas": MaxPriorityFeePerGas,
            "nonce": web3.eth.get_transaction_count(user.address),
        }
    )
    signedtx = user.sign_transaction(onboard)
    print("##")
    print("## Your Signed Transaction is Below:")
    print()
    print(signedtx.rawTransaction.hex())
    print()
    print("##                                                          ##")
    print("##############################################################")
    print("##                                                          ##")
    print("##         We look forward to delivering you alpha!         ##")
    print("##                                                          ##")
    print("##############################################################")


if __name__ == "__main__":
    main()