# -*- coding: utf-8 -*-
import wktopdf

google_pdf = wktopdf.from_url('http://www.google.com/')

with open('hello_world.pdf', 'wb') as f:
    f.write(google_pdf)
