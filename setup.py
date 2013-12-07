from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()

version = '1.1.0'

install_requires = [
]

setup(name='acidfile',
    version=version,
    description="ACID transaction with common files",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3.3',
      'Topic :: Software Development :: Embedded Systems',
      'Topic :: System',
    ],
    keywords='ACID transactional file',
    author='Roberto Abdelkader Mart\xc3\xadnez P\xc3\xa9rez',
    author_email='robertomartinezp@gmail.com',
    url='https://github.com/nilp0inter/acidfile',
    license='GPLv3',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
    }
)
