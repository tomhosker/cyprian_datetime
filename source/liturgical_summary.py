"""
This code defines a class which calculates and contains the important
liturgical dates within a given year.
"""

# Standard imports.
from dataclasses import dataclass, field
from datetime import datetime, timedelta

# Non-standard imports
from dateutil.easter import easter

# Local constants.
WEEKS_IN_ADVENT = 4
# Fixed dates: (month, day) format.
CHRISTMAS = (12, 25)
EPIPHANY = (1, 6)
FEAST_OF_ST_GEORGE = (4, 23)
TRANSITUS_OF_ST_FRANCIS = (10, 3)
FEAST_OF_ST_FRANCIS = (10, 4)
EVE_OF_ST_CRISPIN = (10, 24)
FEAST_OF_ST_CRISPIN = (10, 25)
ALL_SAINTS_DAY = (11, 1)

################################
# HELPER CLASSES AND FUNCTIONS #
################################

@dataclass
class AdventDDates:
    """ A class to give the Advent-dependent dates in a given year. """
    year: int
    advent_sunday: datetime = field(init=False, default=None)
    second_sunday_of_advent: datetime = field(init=False, default=None)
    gaudete_sunday: datetime = field(init=False, default=None)
    fourth_sunday_of_advent: datetime = field(init=False, default=None)

    def __post_init__(self):
        self.advent_sunday = advent_sunday(self.year)
        self.second_sunday_of_advent = self.advent_sunday+timedelta(weeks=1)
        self.gaudete_sunday = self.advent_sunday+timedelta(weeks=2)
        self.fourth_sunday_of_advent = self.advent_sunday+timedelta(weeks=3)

    def to_lookup(self) -> dict[str, str]:
        """ Get the fields of this class indexed by date string. """
        result = {
            self.advent_sunday.isoformat(): "Advent Sunday",
            #self.second_sunday_of_advent.isoformat(): \
            #    "Second Sunday of Advent",
            self.gaudete_sunday.isoformat(): "Gaudete Sunday",
            #self.fourth_sunday_of_advent.isoformat(): "Fourth Sunday of Advent"
        }
        return result

@dataclass
class EasterDDates:
    """ A class to give the Easter-dependent dates in a given year. """
    year: int
    ash_wednesday: datetime = field(init=False, default=None)
    first_sunday_of_lent: datetime = field(init=False, default=None)
    second_sunday_of_lent: datetime = field(init=False, default=None)
    third_sunday_of_lent: datetime = field(init=False, default=None)
    mothering_sunday: datetime = field(init=False, default=None)
    fifth_sunday_of_lent: datetime = field(init=False, default=None)
    palm_sunday: datetime = field(init=False, default=None)
    maundy_thursday: datetime = field(init=False, default=None)
    good_friday: datetime = field(init=False, default=None)
    holy_saturday: datetime = field(init=False, default=None)
    easter_sunday: datetime = field(init=False, default=None)
    second_sunday_of_easter: datetime = field(init=False, default=None)
    third_sunday_of_easter: datetime = field(init=False, default=None)
    fourth_sunday_of_easter: datetime = field(init=False, default=None)
    fifth_sunday_of_easter: datetime = field(init=False, default=None)
    sixth_sunday_of_easter: datetime = field(init=False, default=None)
    ascension: datetime = field(init=False, default=None)
    seventh_sunday_of_easter: datetime = field(init=False, default=None)
    pentecost: datetime = field(init=False, default=None)
    trinity_sunday: datetime = field(init=False, default=None)

    def __post_init__(self):
        easter_date = easter(self.year)
        self.easter_sunday = datetime.combine(easter_date, datetime.min.time())
        self.holy_saturday = self.easter_sunday-timedelta(days=1)
        self.good_friday = self.holy_saturday-timedelta(days=1)
        self.maundy_thursday = self.good_friday-timedelta(days=1)
        self.palm_sunday = self.easter_sunday-timedelta(weeks=1)
        self.fifth_sunday_of_lent = self.easter_sunday-timedelta(weeks=2)
        self.mothering_sunday = self.easter_sunday-timedelta(weeks=3)
        self.fourth_sunday_of_lent = self.mothering_sunday-timedelta(weeks=1)
        self.third_sunday_of_lent = self.mothering_sunday-timedelta(weeks=2)
        self.second_sunday_of_lent = self.mothering_sunday-timedelta(weeks=3)
        self.first_sunday_of_lent = self.mothering_sunday-timedelta(weeks=4)
        self.ash_wednesday = self.first_sunday_of_lent-timedelta(days=4)
        self.second_sunday_of_easter = self.easter_sunday+timedelta(weeks=1)
        self.third_sunday_of_easter = self.easter_sunday+timedelta(weeks=2)
        self.fourth_sunday_of_easter = self.easter_sunday+timedelta(weeks=3)
        self.fifth_sunday_of_easter = self.easter_sunday+timedelta(weeks=4)
        self.sixth_sunday_of_easter = self.easter_sunday+timedelta(weeks=5)
        self.ascension = self.sixth_sunday_of_easter+timedelta(days=4)
        self.seventh_sunday_of_easter = self.easter_sunday+timedelta(weeks=6)
        self.pentecost = self.easter_sunday+timedelta(weeks=7)
        self.trinity_sunday = self.pentecost+timedelta(weeks=1)

    def to_lookup(self) -> dict[str, str]:
        """ Get the fields of this class indexed by date string. """
        result = {
            self.ash_wednesday.isoformat(): "Ash Wednesday",
            #self.first_sunday_of_lent.isoformat(): "First Sunday of Lent",
            #self.second_sunday_of_lent.isoformat(): "Second Sunday of Lent",
            #self.third_sunday_of_lent.isoformat(): "Third Sunday of Lent",
            self.mothering_sunday.isoformat(): "Mothering Sunday",
            #self.fifth_sunday_of_lent.isoformat(): "Fifth Sunday of Lent",
            self.palm_sunday.isoformat(): "Palm Sunday",
            self.maundy_thursday.isoformat(): "Maundy Thursday",
            self.good_friday.isoformat(): "Good Friday",
            #self.holy_saturday.isoformat(): "Holy Saturday",
            self.easter_sunday.isoformat(): "Easter Sunday",
            #self.second_sunday_of_easter.isoformat(): \
            #    "Second Sunday of Easter",
            #self.third_sunday_of_easter.isoformat(): "Third Sunday of Easter",
            #self.fourth_sunday_of_easter.isoformat(): \
            #    "Fourth Sunday of Easter",
            #self.fifth_sunday_of_easter.isoformat(): "Fifth Sunday of Easter",
            #self.sixth_sunday_of_easter.isoformat(): "Sixth Sunday of Easter",
            self.ascension.isoformat(): "Ascension",
            #self.seventh_sunday_of_easter.isoformat(): \
            #    "Seventh Sunday of Easter",
            self.pentecost.isoformat(): "Pentecost",
            #self.trinity_sunday.isoformat(): "Trinity Sunday"
        }
        return result

@dataclass
class FixedDates:
    """ Ronseal. """
    year: int
    christmas: datetime = field(init=False, default=None)
    epiphany: datetime = field(init=False, default=None)
    feast_of_st_george: datetime = field(init=False, default=None)
    transitus_of_st_francis: datetime = field(init=False, default=None)
    feast_of_st_francis: datetime = field(init=False, default=None)
    eve_of_st_crispin: datetime = field(init=False, default=None)
    feast_of_st_crispin: datetime = field(init=False, default=None)
    all_saints_day: datetime = field(init=False, default=None)

    def __post_init__(self):
        self.christmas = datetime(self.year, *CHRISTMAS)
        self.epiphany = datetime(self.year, *EPIPHANY)
        self.feast_of_st_george = datetime(self.year, *FEAST_OF_ST_GEORGE)
        self.transitus_of_st_francis = \
            datetime(self.year, *TRANSITUS_OF_ST_FRANCIS)
        self.feast_of_st_francis = datetime(self.year, *FEAST_OF_ST_FRANCIS)
        self.eve_of_st_crispin = datetime(self.year, *EVE_OF_ST_CRISPIN)
        self.feast_of_st_crispin = datetime(self.year, *FEAST_OF_ST_CRISPIN)
        self.all_saints_day = datetime(self.year, *ALL_SAINTS_DAY)

    def to_lookup(self) -> dict[str, str]:
        """ Get the fields of this class indexed by date string. """
        result = {
            self.christmas.isoformat(): "Christmas",
            self.epiphany.isoformat(): "Epiphany",
            self.feast_of_st_george.isoformat(): "Feast of St George",
            self.transitus_of_st_francis.isoformat(): "Transitus of St Francis",
            self.feast_of_st_francis.isoformat(): "Feast of St Francis",
            self.eve_of_st_crispin.isoformat(): "Eve of St Crispin",
            self.feast_of_st_crispin.isoformat(): "Feast of St Crispin",
            self.all_saints_day.isoformat(): "All Saints' Day"
        }
        return result

def advent_sunday(year: int) -> datetime:
    """ Get the date on which Advent Sunday falls in a given year. """
    christmas = datetime(year, *CHRISTMAS)
    christmas_wday = christmas.weekday()
    if christmas_wday == 0:
        sunday_before_christmas = christmas-timedelta(weeks=1)
    else:
        sunday_before_christmas = christmas-timedelta(days=christmas_wday)
    result = sunday_before_christmas-timedelta(weeks=WEEKS_IN_ADVENT-1)
    return result

##############
# MAIN CLASS #
##############

@dataclass
class LiturgicalSummary:
    """ The class in question. """
    year: int
    advent_dependent_dates: AdventDDates|None = field(init=False, default=None)
    easter_dependent_dates: EasterDDates|None = field(init=False, default=None)
    fixed_dates: FixedDates|None = field(init=False, default=None)

    def __post_init__(self):
        self.advent_dependent_dates = AdventDDates(self.year)
        self.easter_dependent_dates = EasterDDates(self.year)
        self.fixed_dates = FixedDates(self.year)

    def to_lookup(self) -> dict[str, str]:
        """ Get all the liturgical milestones, indexed by date string. """
        result = {}
        result.update(self.advent_dependent_dates.to_lookup())
        result.update(self.easter_dependent_dates.to_lookup())
        result.update(self.fixed_dates.to_lookup())
        return result
