from .metric import Metric
import requests

class TotalNfts(Metric):
    url = "https://eth-mainnet.g.alchemy.com/v2/A5HAWbrqu_g8L0CL54zO9jhFfSSiDfhF/getNFTs?owner="

    def getText(self, p, b):
        if b > 0:
            return f'{p} has {b} NFTs..'
        else:
            return ' Neither of you have NFTs :('


    def compare(self, web3, p1, p2):
        b1 = self.calculate(p1)
        b2 = self.calculate(p2)

        return {
            'winner1': b1 > b2,
            'winner2': b2 > b1,
            'topic': 'Total number of NFTs',
            'text1': self.getText(p1, b1),
            'text2': self.getText(p2, b2)
        }

    def calculate(self, address):
        result = requests.get(TotalNfts.url + address + "&withMetadata=False").json()
        totalnfts = result['totalCount']
        return totalnfts
