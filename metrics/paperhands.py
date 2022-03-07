from .metric import Metric
import requests

class Paperhands(Metric):
    url = "https://api.paperhands.gg/wallet-stats?walletAddress="

    def getText(self, p, b):
        if b > 0:
            return f'{p} has bigger paperhands, losing {b} (so far...).'
        else:
            return ' Neither of you have paperhands :)'


    def compare(self, web3, p1, p2):
        b1 = self.calculate(p1)
        b2 = self.calculate(p2)

        return {
            'loser1': b1 > b2,
            'loser2': b2 > b1,
            'topic': 'ETH lost by paperhanding',
            'text1': self.getText(p1, b1),
            'text2': self.getText(p2, b2)
        }

    def calculate(self, address):
        result = requests.get(Paperhands.url + address).json()
        paperhands = result['paperhandsReportSummary']['totalLossInEth']
        return paperhands
