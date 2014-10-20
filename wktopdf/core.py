# -*- coding: utf-8 -*-
import six

from wktopdf import WktopdfError, settings
from wktopdf.ffi import ffi, C


class UnprocessedWebkitPdf(object):

    def __init__(self):
        self._gs = C.wkhtmltopdf_create_global_settings()
        self._os = C.wkhtmltopdf_create_object_settings()
        self._converter = C.wkhtmltopdf_create_converter(self._gs)

    def set(self, setting, value):
        if setting in settings.GLOBAL_SETTINGS:
            set_result = self._global_set(setting, value)

        elif setting in settings.OBJECT_SETTINGS:
            set_result = self._object_set(setting, value)

        else:
            raise WktopdfError('`{}` is not a recognized setting.'.format(setting))

        if set_result != 1:
            raise WktopdfError('An error happened while trying to set `{}` to '
                               '"{}".'.format(setting, value))

    def set_dict(self, settings_dict):
        for setting, value in settings_dict.items():
            self.set(setting, value)

    def _object_set(self, setting, value):
        return C.wkhtmltopdf_set_object_setting(self._os, setting, value)

    def _global_set(self, setting, value):
        return C.wkhtmltopdf_set_global_setting(self._gs, setting, value)

    def process_url(self, url):
        C.wkhtmltopdf_set_object_setting(self._os, 'page', url)
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
        pdf_bytes_len = C.wkhtmltopdf_get_output(self._converter, cstr)
        pdf_bytes = ffi.buffer(cstr[0], pdf_bytes_len)

        C.wkhtmltopdf_destroy_converter(self._converter)

        return pdf_bytes
