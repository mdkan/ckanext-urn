from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-urn',
	version=version,
	description="URN support for dataset and resources",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Aleksi Suomalainen',
	author_email='aleksi.suomalainen@nomovok.com',
	url='http://not.yet.fi',
	license='GPL',
	packages=find_packages(exclude=['ez_setup', 'examples', 'test']),
	namespace_packages=['ckanext', 'ckanext.urn'],
	include_package_data=True,
	zip_safe=False,
	setup_requires=[
				'nose>=1.0'
				],
	install_requires=[
		# -*- Extra requirements: -*-
	],
	tests_require=[
		'nose',
		'mock',
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here, eg
	urn=ckanext.urn.plugin:URNPlugin
	""",
)
