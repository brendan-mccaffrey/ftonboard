# Friend Tech Onboarding Utility

This is a script that generates a signed transaction that, when broadcasted, will onboard the respective user onto [friend.tech](https://www.friend.tech/).

This allows creators to be onboarded, by my team, onto the platform in a priviledged manner (guarantee ownership of the creator's first `N` shares, for example).

## Usage

First, clone this repository, and install dependencies.

1. [Download python](https://www.python.org/downloads/) if you don't have it already. This should take ~1 minute.

2. Open your command line, and install two web3 packages.

```bash
pip install web3

pip install eth_account
```

## Usage

Make sure you are in the project directory. Then, run the following command:

```bash
python main.py
```

### Example User Flow

```bash
$ python main.py

##############################################################
##                                                          ##
##                         Welcome                          ##
##                                                          ##
##############################################################
##                                                          ##
##   This script will generate a raw signed transaction     ##
## to onboard to friend.tech. Sharing this signed tx will   ##
## allow us to onboard you in a priviledged manner, while   ##
## maintaining the security of your account.                ##
##                                                          ##
##   We never see your private key, and can only broadcast  ##
## your signed transaction.                                 ##
##                                                          ##
##############################################################
##
## Paste your private key here:
```

_user pastes their private key, and presses enter_

```bash
##
## Your Signed Transaction is Below:

0x02f8b482210580851bf08eb000851e449a940083015REDACTED08ed36593aa40a44f10c7f7c2f67d4a4d480b8446945b12300000000000000000000000021ee967REDACTED28f3c94d0ef0103f51dd71f5a0000000000000000000000000000000000000000000000000000000000000001c080a059d375d50ddc2d13c31d5f8306eb7ae072de985d88fREDACTED43e7f2aaaef07a0173b68fad1d9465fe9104d200bb444c07a3aab8bf653b7b352141bc0e5b010f3

##                                                          ##
##############################################################
##                                                          ##
##         We look forward to delivering you alpha!         ##
##                                                          ##
##############################################################
```

## Contact

If you have any questions, or are interested in onboarding with us, please reach out to

tech [at] undefined [dot] xyz
