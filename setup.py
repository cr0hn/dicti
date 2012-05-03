#!/usr/bin/env python2

# This file is part of dicti.

# dicti is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# dicti is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero Public License for more details.

# You should have received a copy of the GNU Affero Public License
# along with dicti.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup
import dicti

setup(name='dicti',
      author='Thomas Levine',
      author_email='occurrence@thomaslevine.com',
      #author_email='thomas@scraperwiki.com',
      description='Dictionary with case-insensitive keys',
      url='https://github.com/tlevine/dicti',
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
          'Programming Language :: Python :: 2.7',
      ],
      packages=['dicti'],

      # From requests
      version=dicti.__version__,
      license='AGPL',
     )
