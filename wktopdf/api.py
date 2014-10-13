# -*- coding: utf-8 -*-
import six

from wktopdf.core import UnprocessedWebkitPdf


def from_html(html_content):
    if not isinstance(html_content, six.text_type):
        raise TypeError('`wktopdf.api.from_html()` is expecting unicode data.')
    pdf = UnprocessedWebkitPdf()
    pdf.set_html(html_content.encode('utf-8'))
    return pdf.process()


def from_url(url):
    pdf = UnprocessedWebkitPdf()
    pdf.set_url(url)
    return pdf.process()
