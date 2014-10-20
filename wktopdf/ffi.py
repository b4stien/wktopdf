# -*- coding: utf-8 -*-
import atexit
import codecs
import inspect
from os import getenv, path

import cffi


local_path = '/usr/local'

include_dir = getenv('WKTOPDF_INCLUDE')
if include_dir is None:
	include_dir = path.join(local_path, 'include/wkhtmltox')
library_dir = getenv('WKTOPDF_LIB')
if library_dir is None:
	library_dir = path.join(local_path, 'lib')

ffi = cffi.FFI()

dir_path = path.dirname(path.abspath(inspect.getfile(inspect.currentframe())))

decl_path = path.join(dir_path, 'decl.h')
with codecs.open(decl_path, 'r', 'utf-8') as header:
    ffi.cdef(header.read())

C = ffi.verify(
    '#include <pdf.h>',
    libraries=['wkhtmltox'],
    include_dirs=[include_dir],
    library_dirs=[library_dir],
)

C.wkhtmltopdf_init(0)


def deinit_wkhtmltopdf(C):
    C.wkhtmltopdf_deinit()
atexit.register(deinit_wkhtmltopdf, C)
