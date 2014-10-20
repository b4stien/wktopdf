# -*- coding: utf-8 -*-
import six

from wktopdf.core import UnprocessedWebkitPdf


def from_html(html_content, encoding='utf-8'):
    if not isinstance(html_content, six.text_type):
        raise TypeError('`wktopdf.api.from_html()` is expecting unicode data.')
    unprocessed_pdf = UnprocessedWebkitPdf()
    unprocessed_pdf.set('web.defaultEncoding', 'utf-8')
    return unprocessed_pdf.process_html_content(html_content.encode(encoding))


def from_url(url):
    unprocessed_pdf = UnprocessedWebkitPdf()
    return unprocessed_pdf.process_url(url)
