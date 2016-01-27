#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

setup(
    name = 'taiga-contrib-mailchimp-subscription',
    version = ':versiontools:taiga_contrib_mailchimp_subscription:',
    description = 'Plugin to subscribe and unsubscribe users to the newsletter in MailChimp.',
    long_description = 'Plugin to subscribe and unsubscribe users to the newsletter in MailChimp.',
    keywords = 'taiga, mailchimp, integration',
    author = 'Taiga Agile LLC',
    author_email = 'taiga@taiga.io',
    url = 'https://github.com/taigaio/taiga-contrib-mailchimp-subscription',
    license = 'AGPL',
    include_package_data = True,
    packages = find_packages(),
    install_requires=[],
    setup_requires = [
        'versiontools >= 1.8',
    ],
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
