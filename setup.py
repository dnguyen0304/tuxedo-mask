#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

import setuptools

if __name__ == '__main__':
    package_name = 'tuxedomask'

    description = ('A lightweight, minimalist Identity and Access Management '
                   'microservice.')

    with open('./README.md', 'r') as file:
        long_description = file.read()

    dependency_links = list()
    install_requires = ['bcrypt==3.1.3',
                        'common==0.4.3',
                        'Flask-HTTPAuth==3.2.2',
                        'Flask-RESTful==0.3.5',
                        'marshmallow==2.13.4',
                        'psycopg2==2.7.1',
                        'SQLAlchemy==1.1.6']

    for dependency in install_requires:
        match = re.match(pattern='common==(?P<version>\d\.\d\.\d)',
                         string=dependency)
        if match:
            repository_url = 'git+https://github.com/dnguyen0304/python-common.git@v{0}#egg=common-{0}'
            dependency_links.append(repository_url.format(
                match.group('version')))
            break

    setuptools.setup(name=package_name,
                     version='1.3.0',
                     description=description,
                     long_description=long_description,
                     url='https://github.com/dnguyen0304/tuxedo-mask.git',
                     author='Duy Nguyen',
                     author_email='dnguyen0304@gmail.com',
                     license='MIT',
                     packages=setuptools.find_packages(exclude=['*.tests']),
                     dependency_links=dependency_links,
                     install_requires=install_requires,
                     test_suite='nose.collector',
                     tests_require=['nose'],
                     include_package_data=True)
