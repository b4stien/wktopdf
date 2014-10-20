wktopdf - Python bindings for wkhtmltopdf
=========================================

wktopdf is a set of Python bindings to the `whtmltopdf
<http://wkhtmltopdf.org/>`_ C library. wktopdf works with Python 2&3 as well as
Pypy, and is released under the MIT license.

It aims at providing a (more) convenient way to generate PDF files from HTML
resources. A mandatory code sample:

.. code-block:: pycon

    >>> pdf = wktopdf.from_html('<h1>Hello world!</h1>')
    >>> pdf.bytes_len
    5876
    >>> pdf.bytes
    ...

Library status
--------------

Even though wktopdf is already working for some simple cases, it should still
be considered highly experimental.

How to install
--------------

TODO

Inspiration
-----------

`Pygit2 <https://github.com/libgit2/pygit2>`_ has to be credited for the way
these bindings are written as most of the setup code and the C interface is
extracted from there.
