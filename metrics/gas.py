from .metric import Metric
import requests

class Gas(Metric):
    url1 = "https://api.etherscan.io/api?module=account&action=txlist&address="
    url2 = "&startblock=0&endblock=99999999&page=1&offset=0&sort=desc&apikey=3SJEA6GFDBZNAGPYG26SRTR5JF9MW7DNCB"

    def getText(self, p, b):
        if b > 0:
            return f'{p} is a pyromaniac spending {b} WEI..'
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

        if len(result) == 0: 
            return 0

        gas = [d['cumulativeGasUsed'] for d in result]
        # TODO must make sum of all transactions (and do paging) - probably to slow to do
        return int(gas[0])