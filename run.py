import csv

from web3 import Web3
from mnemonic import Mnemonic
from eth_account import Account

Account.enable_unaudited_hdwallet_features()
wallets_to_save = []
amount = int(input('How many wallets you want to create?'))
for i in range(amount):
    mnemo = Mnemonic("english")
    seed_phrase = mnemo.generate(128)
    account: Account = Account.from_mnemonic(seed_phrase)
    wallet = {
        'public_key': account.address,
        'private_key': account.key.hex(),
        'seed_phrase': seed_phrase,
    }
    wallets_to_save.append(wallet)

keys = wallets_to_save[0].keys()
with open('wallets.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(wallets_to_save)

print('Copy CSV file to other directory because next script run will overwrite file')