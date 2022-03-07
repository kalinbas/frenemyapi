from .metric import Metric
import requests

class TotalBluechips(Metric):
    url = "https://eth-mainnet.g.alchemy.com/v2/A5HAWbrqu_g8L0CL54zO9jhFfSSiDfhF/getNFTs?owner="
    #Bluechip NFT list
    Cryptopunks     = "&contractAddresses[]=" + "0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB"
    BAYC            = "&contractAddresses[]=" + "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"
    CyberKongz      = "&contractAddresses[]=" + "0x57a204AA1042f6E66DD7730813f4024114d74f37"
    Coolcats        = "&contractAddresses[]=" + "0x1A92f7381B9F03921564a437210bB9396471050C"
    Doodles         = "&contractAddresses[]=" + "0x8a90CAb2b38dba80c64b7734e58Ee1dB38B8992e"
    WorldofWomen    = "&contractAddresses[]=" + "0xe785E82358879F061BC3dcAC6f0444462D4b5330"
    Veefriends      = "&contractAddresses[]=" + "0xa3AEe8BcE55BEeA1951EF834b99f3Ac60d1ABeeB"
    MAYC            = "&contractAddresses[]=" + "0x60E4d786628Fea6478F785A6d7e704777c86a7c6"

    filterlist =   Cryptopunks + BAYC + CyberKongz + Coolcats + Doodles + WorldofWomen + Veefriends + MAYC
    
    def getText(self, p, b):
        if b > 0:
            return f'{p} has {b} bluechip NFTs.'
        else:
            return f'{p} is a poor peasant without bluechip NFTs :('


    def compare(self, web3, p1, p2):
        b1 = self.calculate(p1)
        b2 = self.calculate(p2)

        return {
            'winner1': b1 > b2,
            'winner2': b2 > b1,
            'topic': 'Total number of BLUECHIP NFTs',
            'text1': self.getText(p1, b1),
            'text2': self.getText(p2, b2)
        }

    def calculate(self, address):
        result = requests.get(TotalBluechips.url + address + "&withMetadata=False" + TotalBluechips.filterlist).json()
        totalbluechips = result['totalCount']
        return totalbluechips