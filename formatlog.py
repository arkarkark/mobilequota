#!/usr/bin/env python3
"""Quick test file for logging."""
import logging

class StyleAdapter(logging.LoggerAdapter):
    """"Use .format {} style logging rather than %."""
    def __init__(self, logger, extra=None):
        super(StyleAdapter, self).__init__(logger, extra or {})

    def log(self, level, msg, *args, **kwargs):
        if self.isEnabledFor(level):
            msg, kwargs = self.process(msg, kwargs)
            self.logger._log(level, msg.format(*args), (), **kwargs) # pylint: disable=protected-access

logging.basicConfig()

LOG = StyleAdapter(logging.getLogger(__name__))
LOG.logger.setLevel(logging.DEBUG)

LOG.info('this is a debug log')
# LOG.info('using percent %r', 1)
LOG.info('using squiggles {}', 1)
