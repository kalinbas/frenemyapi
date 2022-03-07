from .metric import Metric
import requests

class Commonnfts(Metric):
    url = "https://eth-mainnet.g.alchemy.com/v2/A5HAWbrqu_g8L0CL54zO9jhFfSSiDfhF/getNFTs?owner="

    def getText(self, p, b):
        if b > 0:
            return f'You both love the same NFTS!!! like {p} and {b-1} more..'
        else:
            return ' You dont like the same NFTs :('


    def compare(self, web3, p1, p2):
        b1 = self.calculate(p1)
        b2 = self.calculate(p2)
        listcommon = list(set(b1) & set(b2))
        totalcommon = len(listcommon)
        #here query the name of listcommon[0]

        return {
            'fren': totalcommon > 0,
            'frenemies':  totalcommon < 1,
            'topic': 'Number of Nfts in common',
            #'text1': self.getText(p1, totalcommon),
            'text2': self.getText(listcommon[0], totalcommon)
        }

    def calculate(self, address):
        result = requests.get(Commonnfts.url + address ).json()
        result = result['ownedNfts']
        result = [d['contract'] for d in result]
        result = [d['address'] for d in result]
        return result