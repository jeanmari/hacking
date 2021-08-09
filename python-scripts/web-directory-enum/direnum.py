#! /usr/bin/env python3
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-w', '-wordlist', help='path to wordlist')
parser.add_argument('-u', '-url', help='target website url')

args = parser.parse_args()

subList = open(args.w).read()
wordlist = subList.splitlines()

for word in wordlist:
    url = f'{args.u}/{word}'
    r = requests.get(url)
    if r.status_code == 404:
        pass
    else:
        print('Valid directory: ', url)
