#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

if __name__ == '__main__':
    package_name = 'tuxedomask'

    description = ('A lightweight, minimalist Identity and Access Management '
                   'microservice.')
    url = 'https://github.com/dnguyen0304/tuxedo-mask.git'
    dependency_links = [
        'git+https://github.com/dnguyen0304/python-common.git@v0.4.2#egg=common-0.4.2']

    with open('./README.md', 'r') as file:
        long_description = file.read()
    with open('./requirements.txt', 'r') as file:
        install_requires = file.read().splitlines()

    setuptools.setup(name=package_name,
                     version='1.3.0',
                     description=description,
                     long_description=long_description,
                     url=url,
                     author='Duy Nguyen',
                     author_email='dnguyen0304@gmail.com',
                     license='MIT',
                     packages=setuptools.find_packages(exclude=['*.tests']),
                     dependency_links=dependency_links,
                     install_requires=install_requires,
                     test_suite='nose.collector',
                     tests_require=['nose'],
                     include_package_data=True)
