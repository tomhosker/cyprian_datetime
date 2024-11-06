"""
This code defines the extension of the standard datetime class.
"""

# Standard imports.
from datetime import datetime
from typing import Self

# Local imports.
from .cyprian_date import CyprianDate
from .frontend_utils import convert_date

##############
# MAIN CLASS #
##############

class CyprianDateTime(datetime):
    """ The class in question. """
    def __new__(cls, *args, **kwargs) -> Self:
        self = super().__new__(cls, *args, **kwargs)
        self._cyprian = convert_date(self)
        return self

    @property
    def cyprian(self) -> CyprianDate:
        """ The Cyprian equivalent to the current date. """
        self._cyprian = convert_date(self)  # Synchronise on each lookup.
        return self._cyprian
