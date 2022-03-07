import requests
import random
import time
import re
from web3 import Web3

from flask import Flask, request, json, abort, jsonify
from flask_cors import CORS

from metrics import hexspeak, balance, paperhands, totalbluechips, totalnfts, gas, common

web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161'))

#list of all used metrics
metrics = [hexspeak.HexSpeak(), balance.Balance(), paperhands.Paperhands(), totalbluechips.TotalBluechips(), totalnfts.TotalNfts(), gas.Gas(), common.Common()]

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
@app.route('/api', methods=['GET'])
def root():
    return 'Frenemy API Server'

@app.route('/api/test', methods=['GET'])
def test():
    m = request.args.get('m', type = int)
    p1 = request.args.get('p1')
    p2 = request.args.get('p2')
    metric = metrics[m]
    return metric.compare(p1, p2)

@app.route('/api/battle', methods=['GET'])
def battle():
    try:
        p1 = request.args.get('p1')
        p2 = request.args.get('p2')

        steps = request.args.get('steps', default = 3, type = int)
        seed = request.args.get('seed', default = int(time.time()), type = int)

        if p1 == None or p2 == None:
            return {'success': False, 'error': "Missing p1 or p2 parameter"}

        p1Address = resolveAddress(p1)
        p2Address = resolveAddress(p2)

        if p1Address == None:
            return {'success': False, 'error': "Invalid address p1"}
        if p2Address == None:
            return {'success': False, 'error': "Invalid address p2"}


        if steps < 1 or steps > 5:
            return {'success': False, 'error': "Invalid steps parameter must be between 1 and 5"}

        random.seed(seed)
        usedMetrics = random.sample(metrics, steps)
        results = list(map(lambda m: m.compare(web3, p1Address, p2Address), usedMetrics))

        return {'success': True,
                'p1': p1,
                'p2': p2,
                'steps': results}
    except Exception as e:
        return {'success': False, 'error': str(e)}


def resolveAddress(ad):
    if Web3.isAddress(ad):
        return ad
    return web3.ens.resolve(ad)

    