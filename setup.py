#! /usr/bin/env python
#
# Copyright (C) 2013 Linaro Limited
#
# Author: Neil Williams <neil.williams@linaro.org>
#
# This file is part of LAVA Coordinator.
#
# LAVA Coordinator is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# LAVA Coordinator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses>.

from setuptools import setup, find_packages

setup(
    name='lava-coordinator',
    version="0.1.3",
    author="Neil Williams",
    author_email="neil.williams@linaro.org",
    license="GPL2+",
    description="LAVA Coordinator daemon for MultiNode",
    packages=find_packages(),
    install_requires=[
        "daemon",
        "lockfile",
    ],
    data_files=[
        ("/etc/init.d/", ["etc/lava-coordinator.init"]),
        ("/etc/lava-coordinator/", ["etc/lava-coordinator.conf"])
    ],
    scripts=[
        'lava-coordinator'
    ],
    zip_safe=False,
    include_package_data=True)
