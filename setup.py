#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

if __name__ == '__main__':
    package_name = 'tuxedo_mask'

    description = ('A lightweight, minimalist Identity and Access Management '
                   'microservice.')
    url = 'https://github.com/dnguyen0304/{package_name}.git'.format(
        package_name=package_name.replace('_', '-'))
    dependency_links = [
        'git+https://github.com/dnguyen0304/python-common.git@v0.4.2#egg=common-0.4.2']

    with open('./README.md', 'r') as file:
        long_description = file.read()
    with open('./requirements.txt', 'r') as file:
        install_requires = file.read().splitlines()

    setuptools.setup(name=package_name,
                     version='1.2.2',
                     description=description,
                     long_description=long_description,
                     url=url,
                     author='Duy Nguyen',
                     author_email='dnguyen0304@gmail.com',
                     license='MIT',
                     packages=[package_name,
                               package_name + '.models',
                               package_name + '.repositories',
                               package_name + '.resources',
                               package_name + '.services',
                               package_name + '.views'],
                     dependency_links=dependency_links,
                     install_requires=install_requires,
                     test_suite='nose.collector',
                     tests_require=['nose'],
                     include_package_data=True)

