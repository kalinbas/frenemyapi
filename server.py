from flask import Flask, request, json, abort
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
@app.route('/api', methods=['GET'])
def root():
    return 'Frenemy API Server'

@app.route('/api/battle', methods=['GET'])
def battle():
    p1 = request.args.get('p1')
    p2 = request.args.get('p2')
    steps = request.args.get('steps', default = 3, type = int)
    seed = request.args.get('seed', default = int(time.time()), type = int)

    if p1 != None and p2 != None:
        return calculate(p1, p2, steps, seed);
    else: 
        abort(400);

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

    