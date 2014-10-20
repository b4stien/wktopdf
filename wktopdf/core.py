# -*- coding: utf-8 -*-
import six

from wktopdf import logger
from wktopdf.ffi import ffi, C

default_object_settings = {
    'web.defaultEncoding': 'utf-8',
}


class UnprocessedWebkitPdf(object):

    _html_content = None
    _webpage_url = None

    def __init__(self):
        self._gs = C.wkhtmltopdf_create_global_settings()
        self._os = C.wkhtmltopdf_create_object_settings()
        self._converter = C.wkhtmltopdf_create_converter(self._gs)

        C.wkhtmltopdf_set_object_setting(self._os, 'web.defaultEncoding', 'utf-8')

    def process_url(self, url):
        C.wkhtmltopdf_set_object_setting(self._os, 'page', self._webpage_url)
        C.wkhtmltopdf_add_object(self._converter, self._os, ffi.NULL)
        return self._process()

    def process_html_content(self, html_content):
        if not isinstance(html_content, six.binary_type):
            raise TypeError('`wktopdf.core.UnprocessedWebkitPdf.set_html()` is'
                            ' expecting binary data.')
        C.wkhtmltopdf_add_object(self._converter, self._os, html_content)
        return self._process()

    def _process(self):
        C.wkhtmltopdf_convert(self._converter)

        cstr = ffi.new('unsigned char **')
        bytes_len = C.wkhtmltopdf_get_output(self._converter, cstr)
        bytes = ffi.buffer(cstr[0], bytes_len)

        C.wkhtmltopdf_destroy_converter(self._converter)

        return WebkitPdf(bytes)


class WebkitPdf(object):

    bytes = None

    def __init__(self, bytes):
        self.bytes = bytes

    def save_to_file(self, filename):
        with open(filename, 'wb') as f:
            f.write(self.bytes)
