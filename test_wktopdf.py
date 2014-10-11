# -*- coding: utf-8 -*-
import wktopdf

pdf = wktopdf.from_html('<h1>Douze</h1>')
print pdf.bytes
print pdf.bytes_len

pdf = wktopdf.from_url('http://google.com/')
print pdf.bytes_len
