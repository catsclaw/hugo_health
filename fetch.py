import argparse

import requests


def req_coinmarketcap(cur):
    cur = cur.lower()
    url = f'https://api.coinmarketcap.com/v1/ticker/{cur}/'

    r = requests.get(url)
    if r.status_code == 404:
        print(f'Unknown currency: "{cur}"')
        return

    r.raise_for_status()
    json = r.json()[0]
    print('Price (USD): {json[price_usd]}'.format(json=json))
    print('Market Cap (USD): {json[market_cap_usd]}'.format(json=json))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch cybercurrency data')
    parser.add_argument('currency', type=str, nargs=1, help='the currency')
    args = parser.parse_args()
    req_coinmarketcap(args.currency[0])
