# -*- coding: utf-8 -*-
#
# Copyright © 2017 Leandro Regueiro Iglesias.
#
# This code is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This code is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this code.  If not, see <http://www.gnu.org/licenses/>.

"""Sample script to test animated progress bars."""

import argparse
import time

from bars import PROGRESS_BARS


SLEEP_TIME = 0.05  # Time to wait between steps. In seconds.
TOTAL = 105  # Random total. The bigger it is, the more steps are calculated.


def main():
    """Sample script to test the different progress bars."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--style',
        choices=PROGRESS_BARS.keys(),
        default='equals',
        help='style used to display the progress')

    args = parser.parse_args()
    progress_bar = PROGRESS_BARS[args.style](TOTAL)

    for i in range(1, TOTAL + 1):
        progress_bar.update(i)
        time.sleep(SLEEP_TIME)

    progress_bar.finish()


if __name__ == '__main__':
    main()
