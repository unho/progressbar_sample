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

"""Classes for drawing animated progress bars."""

import sys


PROGRESS_BAR_INNER_LENGTH = 73  # By default consoles are 80 characters wide.


class BaseProgressBar(object):
    """Class providing common code and behavior for progress bars."""

    def __init__(self, total):
        """Initialize the progress bar.

        :param int total: Number of total items to be processed.
        """
        self.total = float(total)

    @property
    def style(self):
        """Style used to indicate the progress."""
        raise NotImplementedError

    @property
    def output(self):
        """File to write the progress to."""
        return sys.stdout

    def write(self, string):
        """Write a string to the output file and flush.

        :param str string: The string to be written in the output file.
        """
        self.output.write(string)
        self.output.flush()

    def get_inner_bar(self, percentage):
        """Returns the string that represents the progress bar's inner part.

        The string takes in account the length of the style used.

        :param float percentage: Percentage of the progress so far.
        :return: Returns the progress bar's central section representation.
        :rtype: str
        """
        i = int(percentage * PROGRESS_BAR_INNER_LENGTH / len(self.style))
        return self.style * i

    def update(self, count):
        """Update the progress bar based on the specified progress.

        :param int count: Number of items processed so far.
        """
        percentage = count / self.total
        int_percent = int(percentage * 100)
        string = '[%s ] %d%%' % (self.get_inner_bar(percentage), int_percent)
        self.write('\r' + string)  # Printing \r first resets current line.

    def finish(self):
        """Force cursor to show up in a new line after progress is complete."""
        self.write('\n')


class EqualsProgressBar(BaseProgressBar):
    """Class rendering a progress bar using equals characters."""

    @property
    def style(self):
        """Style used to indicate the progress."""
        return '='


class SawtoothProgressBar(BaseProgressBar):
    """Class rendering a progress bar in a sawtooth-like fashion."""

    @property
    def style(self):
        """Style used to indicate the progress."""
        return '/\\'


class SquaresProgressBar(BaseProgressBar):
    """Class rendering a progress bar using square characters."""

    @property
    def style(self):
        """Style used to indicate the progress."""
        return '■'


PROGRESS_BARS = {
    'equals': EqualsProgressBar,
    'sawtooth': SawtoothProgressBar,
    'squares': SquaresProgressBar,
}
