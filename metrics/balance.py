from .metric import Metric
from web3 import Web3

class Balance(Metric):

    def __init__(self) :
        self.w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161'))

    def getText(self, p, b):
        if b > 0:
            return f'{p} has {b / 10**18} ETH balance.'
        else:
            return f'{p} has ZERO ETH balance :('


    def compare(self, p1, p2):
        b1 = self.calculate(p1)
        b2 = self.calculate(p2)

        return {
            'winner1': b1 > b2,
            'winner2': b2 > b1,
            'topic': 'ETH Balance',
            'text1': self.getText(p1, b1),
            'text2': self.getText(p2, b2)
        }

    def calculate(self, address):
        caddress = Web3.toChecksumAddress(address)
        balance = self.w3.eth.get_balance(caddress)
        return balance
