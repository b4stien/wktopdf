# -*- coding: utf-8 -*-
from wktopdf.core import WebkitPdf


def from_html(html_content):
    return WebkitPdf(html=html_content)


def from_url(url):
    return WebkitPdf(url=url)
