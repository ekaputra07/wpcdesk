#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  wpcdesk - WordPress Comment Desktop
#  Copyright (C) 2012 Eka Putra - ekaputra@balitechy.com
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

setup(
    name = "WpcDesk",
    version = "1.0.0",
    url = 'https://bitbucket.org/ekaputra/wpcdesk',
    description = 'Simple python program to manage comments on remote WordPress blog via XML-RPC access.',
    license = 'GNU/GPL',
    author = 'Eka Putra',
    author_email = 'ekaputra@balitechy.com',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    scripts=['bin/wpcdesk'],
)

