# -*- coding: utf-8 -*-
from distutils.command.build import build
from setuptools import setup
import sys


class CFFIBuild(build):

    def finalize_options(self):
        sys.path.insert(0, 'wktopdf')
        from ffi import ffi

        self.distribution.ext_modules.append(ffi.verifier.get_extension())
        return build.finalize_options(self)


setup(
    name='wktopdf',
    packages=['wktopdf'],
    package_data={'wktopdf': ['decl.h']},
    setup_requires=['cffi'],
    install_requires=['cffi', 'six'],
    zip_safe=False,
    ext_modules=[],
    cmdclass={'build': CFFIBuild},
)
