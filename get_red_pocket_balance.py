#!/usr/bin/env python3

"""Proof of concept to get redpocket mobile usage.
based on code from https://gist.github.com/gene1wood/236f1dcc082950afb4851a382951820c
"""

import requests
import yaml
import json
import os.path
import datetime
import re
import logging


LOG = logging.getLogger("get_red_pocket_balance")
LOG.setLevel(logging.DEBUG)

def main():
    """Login and get usage data."""
    logging.basicConfig()

    with open(os.path.expanduser('~/.config/mobileusage.yaml')) as conf_file:
        config = yaml.load(conf_file)

    jar = requests.cookies.RequestsCookieJar()
    req = requests.get('https://www.redpocket.com/login', cookies=jar)
    csrf = re.search('name="csrf"[^=]+value="([^"]+)"', req.text, re.MULTILINE).group(1)

    LOG.debug('csrf is %s', csrf)

    data = {
        'mdn': config['username'],
        'password': config['password'],
        'remember_me': 1,
        'redirect_url': '',
        'csrf': csrf
    }
    req = requests.post(
        'https://www.redpocket.com/login',
        data=data,
        cookies=jar)

    LOG.debug('Logged in!')

    data = {'refill_mdn': config['mdn']}

    req = requests.post(
        'https://www.redpocket.com/refill/get-account-info',
        data=data,
        cookies=jar
    )

    result = req.json()

    LOG.info('got back: %r', result)

    output = {
        'datetime': "%s" % datetime.datetime.now(),
        'plan_name': result['plan'],
        'expiration_date': result['aed'],
        'voice_balance': result['voice_balance'],
        'messaging_balance': result['messaging_balance'],
        'data_balance': result['data_balance']
    }

    LOG.info('which is :\n%r', json.dumps(output))

main()
