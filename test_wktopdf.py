# -*- coding: utf-8 -*-
import wktopdf

pdf = wktopdf.from_html(u'<h1>Douze</h1>')
print len(pdf)


unprocessed_pdf = wktopdf.UnprocessedWebkitPdf()
unprocessed_pdf.set('dpi', '600')
unprocessed_pdf.set('imageDPI', '600')
unprocessed_pdf.set_dict(wktopdf.settings.NO_MARGIN)

with open('test.pdf', 'wb') as f:
    f.write(unprocessed_pdf.process_url('http://google.com'))
