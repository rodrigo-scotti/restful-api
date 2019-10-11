# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

__version__ = '0.1.0'
__description__ = 'Template Python'
__long_description__ = 'Project configuration template Python using microframework Flask'

__author__ = 'Rodrigo Rodrigues'
__author_email__ = 'rrscotti@hotmail.com'

setup(
	name = 'template',
	version = __version__,
	author = __author__,
	author_email = __author_email__,
	packages = find_packages(),
	license = 'MIT',
	description = __description__,
	long_description = __long_description__,
	url = 'https://github.com/RodriguesRodrigo/init-python',
	keywords = 'Template, Configuration, Python, Flask',
	include_package_data = True,
	zip_safe = False,
	classifiers = [
		'Intended Audience :: Developers',
		'Operating System :: OS Independent',
		'Topic :: Software Development',
		'Environment :: Web Environment',
		'Programming Language :: Python :: 3.7',
		'License :: OSI Approved :: MIT License',
	],
)
