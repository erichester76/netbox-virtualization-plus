#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='netbox-virtualization-plus',
    version='1.0.0',
    description='Virtualization+ plugin for NetBox',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/clemson-netbox/netbox-virtualization-plus',
    author='Eric Hester',
    author_email='hester1@clemson.edu',
    license='Apache-2.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Pin a NetBox version range if needed, e.g. "netbox>=3.4,<3.6",
        # Or other Python dependencies needed by your plugin
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    zip_safe=False,
)
