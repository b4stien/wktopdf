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

    def __init__(self, global_settings=None, object_settings=None):
        self._gs = C.wkhtmltopdf_create_global_settings()
        self._os = C.wkhtmltopdf_create_object_settings()
        self._converter = C.wkhtmltopdf_create_converter(self._gs)

        C.wkhtmltopdf_set_object_setting(self._os, 'web.defaultEncoding', 'utf-8')

    def set_url(self, webpage_url):
        self._webpage_url = webpage_url
        C.wkhtmltopdf_set_object_setting(self._os, 'page', self._webpage_url)

    def set_html(self, html_content):
        if not isinstance(html_content, six.binary_type):
            raise TypeError('`wktopdf.core.UnprocessedWebkitPdf.set_html()` is'
                            ' expecting binary data.')
        self._html_content = html_content

    def process(self):
        if self._webpage_url is None and self._html_content is None:
            logger.warning('`wktopdf.core.UnprocessedWebkitPdf.process()` has '
                           'been called on a content-less instance. See '
                           '`wktopdf.core.UnprocessedWebkitPdf.set_url()` and '
                           '`wktopdf.core.UnprocessedWebkitPdf.set_html()` for'
                           ' ways to set content.')

        if self._webpage_url is not None and self._html_content is not None:
            logger.warning('Both html resource content and resource url has '
                           'been set on this '
                           '`wktopdf.core.UnprocessedWebkitPdf` instance. This'
                           ' is probably not what you wanted to do.')

        if self._html_content is not None:
            data = self._html_content
        else:
            data = ffi.NULL

        C.wkhtmltopdf_add_object(self._converter, self._os, data)
        C.wkhtmltopdf_convert(self._converter)

        cstr = ffi.new('unsigned char **')
        bytes_len = C.wkhtmltopdf_get_output(self._converter, cstr)
        bytes = ffi.buffer(cstr[0], bytes_len)

        C.wkhtmltopdf_destroy_converter(self._converter)

        return WebkitPdf(bytes, bytes_len)


class WebkitPdf(object):

    bytes_len = None
    bytes = None

    def __init__(self, bytes, bytes_len):
        self.bytes = bytes
        self.bytes_len = bytes_len

    def save_to_file(self, filename):
        with open(filename, 'wb') as f:
            f.write(self.bytes)
