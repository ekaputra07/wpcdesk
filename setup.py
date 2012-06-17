#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "Wordpress Comment Desk",
    version = "1.0.0",
    url = 'https://bitbucket.org/ekaputra/wpcdesk',
    license = 'BSD',
    description = "Simple python program to manage comments on remote WordPress blog via XML-RPC access.",
    author = 'Eka Putra',
    author_email = 'ekaputra@balitechy.com',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
)

