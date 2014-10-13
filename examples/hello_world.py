# -*- coding: utf-8 -*-
import wktopdf

pdf = wktopdf.from_html(u'''
    <h1>Hello world!</h1>
    <h1>你好世界</h1>
    <h1>Здравствулте мир</h1>
''')
pdf.save_to_file('hello_world.pdf')
