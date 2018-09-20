#!/usr/bin/env python3
"""RedPocket Mobile stuff."""

import json

import formatlogging

formatlogging.basicConfig()
LOG = formatlogging.getLogger(__name__)
LOG.logger.setLevel(formatlogging.DEBUG)

class RedPocket(object):
    """."""

    def __init__(self, json_string):
        """."""
        self.obj = json.loads(json_string)
        LOG.debug('Loading {}', self.obj)

    def get_minutes(self):
        """Get the number of minutes remaining."""
        return {
            'minutes': self.obj['voice_balance']
        }

    def get_messages(self):
        """Get the number of messages remaining."""
        return {
            'minutes': self.obj['message_balance']
        }

def main():
    """."""
    LOG.info("all ' done")
    with open('test/get-account-info.json') as test_file:
        red_pocket = RedPocket(test_file.read())
        LOG.debug('GOT {}', red_pocket)

if __name__ == '__main__':
    main()
