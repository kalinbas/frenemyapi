from .metric import Metric
import requests

class Commonpoaps(Metric):
    url = "https://api.poap.xyz/actions/scan/"

    def getText(self, p, b):
        if b > 0:
            return f'Party animals unite!!! You both crashed {p} and {b-1} more events.'
        else:
            return ' You make sure to never attend the same event. Coincidence?! :('


    def compare(self, web3, p1, p2):
        b1 = self.calculate(p1)
        b2 = self.calculate(p2)
        listcommon = list(set(b1) & set(b2))
        totalcommon = len(listcommon)
        return {
            'fren': totalcommon > 0,
            'frenemies':  totalcommon < 1,
            'topic': 'Number of Poaps in common',
            #'text1': self.getText(p1, totalcommon),
            'text2': self.getText(listcommon[0], totalcommon)
        }

    def calculate(self, address):
        result = requests.get(Commonpoaps.url + address).json()
        result = [d['event'] for d in result]
        result = [d['fancy_id'] for d in result]
        return result