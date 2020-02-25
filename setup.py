"""
Acidfile setup script.

"""
from setuptools import setup, find_packages
import os
from io import open

HERE = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(HERE, 'README.rst'), encoding='utf-8').read()
NEWS = open(os.path.join(HERE, 'NEWS.txt'), encoding='utf-8').read()

VERSION = '1.2.1'

setup(name='acidfile',
      version=VERSION,
      description="ACID transaction with common files",
      long_description=README + '\n\n' + NEWS,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Software Development :: Embedded Systems',
          'Topic :: System :: Archiving',
      ],
      keywords='ACID transactional file',
      author='Roberto Abdelkader Mart\xc3\xadnez P\xc3\xa9rez',
      author_email='robertomartinezp@gmail.com',
      url='https://github.com/nilp0inter/acidfile',
      license='LGPLv3',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,)
