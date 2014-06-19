from setuptools import setup, find_packages
import sys, os

version = '0.1'

install_requires = [
    'XlsxWriter',
    'pydap_pdp >=3.2.1'
]

setup(name='pydap.responses.xlsx',
    version=version,
    description="Pydap response that returns the dataset as a XLSX file",
    keywords='xlsx pydap opendap dods',
    author='James Hiebert',
    author_email='hiebert@uvic.ca',
    license='MIT',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    namespace_packages = ['pydap', 'pydap.responses'],
    zip_safe=True,
    install_requires=install_requires,
    entry_points="""
        [pydap.response]
        xlsx = pydap.responses.xlsx:XLSXResponse
    """,
    classifiers = """Development Status :: 3 - Alpha
Intended Audience :: Developers
Intended Audience :: Science/Research
Operating System :: OS Independent
Programming Language :: Python :: 2.7
Topic :: Internet :: WWW/HTTP :: WSGI :: Server
License :: OSI Approved :: MIT License
Topic :: Scientific/Engineering :: GIS""".splitlines(),

)
