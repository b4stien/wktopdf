# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger('wktopdf')

if logger.level == logging.NOTSET:
    logger.setLevel(logging.WARN)

try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logger.addHandler(NullHandler())

class WktopdfError(StandardError):
    """An error happened"""


from wktopdf.core import UnprocessedWebkitPdf
from wktopdf.api import from_html, from_url
