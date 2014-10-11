# -*- coding: utf-8 -*-
import atexit
import codecs
import inspect
from os import path

import cffi


wkhtmltopdf_path = '/usr/local'

include_dirs = [path.join(wkhtmltopdf_path, 'include/wkhtmltox')]
library_dirs = [path.join(wkhtmltopdf_path, 'lib')]

ffi = cffi.FFI()

dir_path = path.dirname(path.abspath(inspect.getfile(inspect.currentframe())))

decl_path = path.join(dir_path, 'decl.h')
with codecs.open(decl_path, 'r', 'utf-8') as header:
    ffi.cdef(header.read())

C = ffi.verify(
    '#include <pdf.h>',
    libraries=['wkhtmltox'],
    include_dirs=include_dirs,
    library_dirs=library_dirs,
)

C.wkhtmltopdf_init(0)


def deinit_wkhtmltopdf(C):
    C.wkhtmltopdf_deinit()
atexit.register(deinit_wkhtmltopdf, C)
