# -*- coding: utf-8 -*-
import wktopdf

pdf_bytes = wktopdf.from_html(u'''
    <h1>Hello world!</h1>
    <h1>你好世界</h1>
    <h1>Здравствулте мир</h1>
''')
with open('hello_world.pdf', 'wb') as f:

    f.write(pdf_bytes)
