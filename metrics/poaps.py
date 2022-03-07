from .metric import Metric
import requests

class Poaps(Metric):
    url = "https://api.poap.xyz/actions/scan/"

    def getText(self, p, b):
        if b > 0:
            return f'{p} is the bigger party animal, crashing {b} events..'
        else:
            return ' Both of you are antisocial introverts :('


    def compare(self, web3, p1, p2):
        b1 = self.calculate(p1)
        b2 = self.calculate(p2)
        
        return {
            'winner1': b1 > b2,
            'winner2': b2 > b1,
            'topic': 'Total number of POAPS',
            'text1': self.getText(p1, b1),
            'text2': self.getText(p2, b2)
        }

    def calculate(self, address):
        result = requests.get(Poaps.url + address).json()
        totalpoaps = len(result)
        return totalpoaps
