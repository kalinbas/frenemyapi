from .metric import Metric
from web3 import Web3

class Balance(Metric):

    def getText(self, p, b):
        if b > 0:
            return f'{p} has {b / 10**18} ETH balance.'
        else:
            return f'{p} has ZERO ETH balance :('


    def compare(self, web3, p1, p2):
        b1 = self.calculate(web3, p1)
        b2 = self.calculate(web3, p2)

        return {
            'winner1': b1 > b2,
            'winner2': b2 > b1,
            'topic': 'ETH Balance',
            'text1': self.getText(p1, b1),
            'text2': self.getText(p2, b2)
        }

    def calculate(self, web3, address):
        caddress = Web3.toChecksumAddress(address)
        balance = web3.eth.get_balance(caddress)
        return balance
