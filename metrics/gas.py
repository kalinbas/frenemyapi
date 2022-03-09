from ast import operator
from functools import reduce
from .metric import Metric
import operator
import requests

class Gas(Metric):
    url1 = "https://api.etherscan.io/api?module=account&action=txlist&address="
    url2 = "&startblock=0&endblock=99999999&page=1&offset=0&sort=desc&apikey=3SJEA6GFDBZNAGPYG26SRTR5JF9MW7DNCB"

    def getText(self, p, b):
        if b > 0:
            return f'{p} is a pyromaniac spending {b} ETH on gas.'
        else:
            return f'{p} is not using Ethereum. SHAME! >:('


    def compare(self, web3, p1, p2):
        b1 = self.calculate(p1)
        b2 = self.calculate(p2)

        return {
            'winner1': b1 > b2,
            'winner2': b2 > b1,
            'topic': 'Total GAS',
            'text1': self.getText(p1, b1),
            'text2': self.getText(p2, b2)
        }

    def calculate(self, address):
        result = requests.get(Gas.url1 + address + Gas.url2).json()
        result = result['result']
        gas = reduce(operator.add, map(lambda r: int(r['gasUsed']) * int(r['gasPrice']), result))
        return gas / 10 ** 18