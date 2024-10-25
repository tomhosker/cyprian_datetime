"""
This code defines a class which holds a Cyprian date.
"""

# Standard imports.
from datetime import datetime, timedelta

# Non-standard imports.
import ephem

# Local imports.
from . import constants

##############
# MAIN CLASS #
##############

class CyprianDate:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day

    def advance_one_day(self, current_greg: datetime):
        """ Find the next day in the calendar. """
        if new_moon_tomorrow(current_greg):
            self.advance_one_month(current_greg)
        else:
            self.day += 1

    def advance_one_month(self, current_greg: datetime):
        """ Ronseal. """
        if self.month == constants.LEAP_MONTH:
            self.advance_one_year()
        elif (
            self.month == constants.LAST_MONTH and
            tomorrow_is_on_or_after_vernal_equinox(current_greg)
        ):
            self.advance_one_year()
        else:
            assert self.month <= constants.LAST_MONTH
            self.month += 1
            self.day = 1

    def advance_one_year(self):
        """ Ronseal. """
        self.year += 1
        self.month = 1
        self.day = 1

####################
# HELPER FUNCTIONS #
####################

def new_moon_tomorrow(greg: datetime) -> bool:
    """ Determine whether the new moon occurs tomorrow. """
    next_new_moon = get_next_new_moon(greg)
    tomorrow = greg+timedelta(days=1)
    return fall_on_same_day(next_new_moon, tomorrow)

def get_next_new_moon(greg: datetime) -> datetime:
    """ Get the Gregorian datetime for the next new moon. """
    ephem_date = ephem.next_new_moon(greg)
    result = ephem_date.datetime()
    return result

def fall_on_same_day(left: datetime, right: datetime) -> bool:
    """ Determine whether two events occur on the same calendar day. """
    if round_down_to_nearest_day(left) == round_down_to_nearest_day(right):
        return True
    return False

def round_down_to_nearest_day(greg: datetime) -> datetime:
    """ Ronseal. """
    result = datetime(greg.year, greg.month, greg.day)
    return result

def get_vernal_equinox(year: int) -> datetime:
    """ Ronseal. """
    ephem_date = ephem.next_vernal_equinox(str(year))
    result = ephem_date.datetime()
    return result

def tomorrow_is_on_or_after_vernal_equinox(greg: datetime) -> bool:
    """ Ronseal. """
    tomorrow = greg+timedelta(days=1)
    rounded_equinox = round_down_to_nearest_day(get_vernal_equinox(greg.year))
    if tomorrow >= rounded_equinox:
        return True
    return False

def get_cyprian_new_year(year: int) -> datetime:
    """
    Given the Gregorian year, calculate the Gregorian equivalent of the Cyprian
    New Year falling within that calendar year.
    """
    ephem_date = ephem.next_new_moon(get_vernal_equinox(year))
    result = round_down_to_nearest_day(ephem_date.datetime())
    return result

def get_cyprian_year(greg_year: int) -> int:
    """ Ronseal. """
    result = greg_year-constants.CYPRIAN_GREGORIAN_YEAR_DIFF
    return result
