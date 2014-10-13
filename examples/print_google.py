# -*- coding: utf-8 -*-
import wktopdf

google_pdf = wktopdf.from_url('http://www.google.com/')
google_pdf.save_to_file('google.pdf')
