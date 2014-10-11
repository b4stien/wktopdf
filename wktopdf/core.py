# -*- coding: utf-8 -*-
from wktopdf.ffi import ffi, C


class WebkitPdf(object):

    def __init__(self, url=None, html=None):
        wkhtml_gs = C.wkhtmltopdf_create_global_settings()
        wkhtml_os = C.wkhtmltopdf_create_object_settings()
        wkhtml_converter = C.wkhtmltopdf_create_converter(wkhtml_gs)

        if url:
            C.wkhtmltopdf_set_object_setting(wkhtml_os, 'page', url)
            C.wkhtmltopdf_add_object(wkhtml_converter, wkhtml_os, ffi.NULL)
        elif html:
            C.wkhtmltopdf_add_object(wkhtml_converter, wkhtml_os, html)
        else:
            raise AttributeError('No content has been given.')

        C.wkhtmltopdf_convert(wkhtml_converter)

        cstr = ffi.new('unsigned char **')
        self.bytes_len = C.wkhtmltopdf_get_output(wkhtml_converter, cstr)
        self.bytes = ffi.buffer(cstr[0], self.bytes_len)

        C.wkhtmltopdf_destroy_converter(wkhtml_converter)
