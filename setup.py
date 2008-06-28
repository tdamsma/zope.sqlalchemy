from setuptools import setup, find_packages
import sys, os

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

def desc(*texts):
    return '\n'.join(texts)

SVN_VERSION = "`SVN version <svn://svn.zope.org/repos/main/zope.sqlalchemy/trunk#egg=zope.sqlalchemy-dev>`_\n"

long_description = desc(
    read('README.txt'),
    read('src', 'zope', 'sqlalchemy', 'README.txt'),
    SVN_VERSION,
    read('CHANGES.txt'),
    'Download\n********\n',
    )

setup(name='zope.sqlalchemy',
      version='0.2', # Remember to update __version__ in __init__.py
      description="Minimal Zope/SQLAlchemy transaction integration",
      long_description=long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Zope3",
        "Programming Language :: Python",
        "License :: OSI Approved :: Zope Public License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Laurence Rowe',
      author_email='laurence@lrowe.co.uk',
      url='http://pypi.python.org/pypi/zope.sqlalchemy',
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir = {'':'src'},
      namespace_packages=['zope'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'setuptools',
          'SQLAlchemy>=0.4.6',
          'transaction',
          'zope.interface',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      extras_require = dict(
              test = ['zope.testing'],
              ),
      )