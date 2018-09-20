#!/usr/bin/env python3
"""Quick test file for logging.

also: https://stackoverflow.com/questions/22993667/logging-module-not-pep8
"""
import logging

DEBUG = logging.DEBUG
INFO = logging.INFO

class StyleAdapter(logging.LoggerAdapter):
    """"Use .format {} style logging rather than %."""
    def __init__(self, logger, extra=None):
        super(StyleAdapter, self).__init__(logger, extra or {})

    def log(self, level, msg, *args, **kwargs):
        if self.isEnabledFor(level):
            msg, kwargs = self.process(msg, kwargs)
            self.logger._log(level, msg.format(*args), (), **kwargs) # pylint: disable=protected-access

def basicConfig(): # pylint: disable=invalid-name
    """Do the basic config thing"""
    logging.basicConfig()

def getLogger(name): # pylint: disable=invalid-name
    """get a logger that uses .format {} formatting."""
    return StyleAdapter(logging.getLogger(name))
