====================
pydap.responses.xlsx
====================

This package implements a Pydap responder which returns a Excel 2010 XLSX formatted file for a certain subset of DAP requests.

--------------
How to Install
--------------

One can install pydap.responses.xlsx using the standard methods of any other Python package.

1. clone our repository and run the setup script

    $ git clone https://github.com/pacificclimate/pydap.responses.xlsx
    $ cd pydap.responses.xlsx
    $ python setup.py install

2. or just point `pip` to our `GitHub repo <https://github.com/pacificclimate/pydap.responses.xlsx>`_:

    $ pip install git+https://github.com/pacificclimate/pydap.responses.xlsx

------------
Requirements
------------

* XlsxWriter
* `pydap_pdp <https://github.com/pacificclimate/pydap-pdp>`_ - This is the `Pacific Climate Impacts Consortium's <http://www.pacificclimate.org>`_ fork of Pydap version 3.1. When Pydap 3.2 is released, we hope to merge our fork and require Pydap's main line.

-----------
Limitations
-----------

The XLSX format itself is `limited to a worksheet size of 1,048,576 rows by 16,384 columns <http://office.microsoft.com/en-ca/excel-help/excel-specifications-and-limits-HP010342495.aspx?CTT=5&origin=HP005199291>`_. At present this response supports only tabular data (i.e. a single dimensional DAP GridType or a DAP SequenceType).

-------
Credits
-------

This package is based heavily on Roberto De Almeida's `pydap.responses.xls <https://pypi.python.org/pypi/pydap.responses.xls/>`_ and depends on the `XlsxWriter <https://pypi.python.org/pypi/XlsxWriter>`_ package to do all of the format-specific work. Many thanks to the authors of both for all of their hard work.
