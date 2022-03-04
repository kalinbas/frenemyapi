import random
import time

from flask import Flask, request, json, abort, jsonify
from flask_cors import CORS

from metrics import hexspeak, balance

#list of all used metrics
metrics = [hexspeak.HexSpeak(), balance.Balance(), hexspeak.HexSpeak()]

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
@app.route('/api', methods=['GET'])
def root():
    return 'Frenemy API Server'

@app.route('/api/test', methods=['GET'])
def test():
    p1 = request.args.get('p1')
    p2 = request.args.get('p2')
    hs = Balance()
    return hs.compare(p1, p2)

@app.route('/api/battle', methods=['GET'])
def battle():

    p1 = request.args.get('p1')
    p2 = request.args.get('p2')
    steps = request.args.get('steps', default = 3, type = int)
    seed = request.args.get('seed', default = int(time.time()), type = int)

    random.seed(seed)
    usedMetrics = random.sample(metrics, steps)
    results = list(map(lambda m: m.compare(p1, p2), usedMetrics))

    return jsonify(results)

    if p1 != None and p2 != None:
        return calculate(p1, p2, steps, seed);
    else: 
        return {'success': False,
                'error': "Missing p1 or p2 parameter"}

def calculate(p1, p2, steps, seed):

    #TODO implement this logic ;)

    return {'success': True,
            'p1': p1,
            'p2': p2,
            'winner1': True,
            'steps': [{
                'winner1': True,
                'topic': 'NFT Gains',
                'summary': 'P1 hurts P2 with fireball',
                'text1': 'P1 made 1.56 ETH on Opensea',
                'text2': 'P2 lost 4.5 ETH flipping JPEGs',
                }, {
                'winner1': False,
                'topic': 'Rugpull Participation',
                'summary': 'P2 hurts P1 with mega-punch',
                'text1': 'P1 lost 100 ETH to 3 rugpulls',
                'text2': 'P2 never lost to anything we know about',
                }, {
                'winner1': True,
                'topic': 'NFT Count',
                'summary': 'P1 hurts P2 with super-flash',
                'text1': 'P1 is a pro with 100 NFTs',
                'text2': 'P2 is a noob with 2 NFTs',
                }],
            }

    