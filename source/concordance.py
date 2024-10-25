"""
This code defines a class which gives the equivalent Cyprian date for each day
in a given Gregorian year.
"""

# Standard imports.
import sqlite3
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path
from sqlite3 import Connection

# Non-standard imports.
import ephem

# Local imports.
from . import constants
from .cyprian_date import (
    CyprianDate,
    get_cyprian_year,
    get_vernal_equinox,
    get_cyprian_new_year
)

##############
# MAIN CLASS #
##############

@dataclass
class Concordance:
    """ The class in question. """
    greg_year: int|None = None
    path_to_cache_db: str = constants.DEFAULT_PATH_TO_CACHE_DB
    cyprian_year: int|None = None
    last_vernal_equinox: datetime|None = field(init=False, default=None)
    this_vernal_equinox: datetime|None = field(init=False, default=None)
    last_cyprian_new_year: datetime|None = field(init=False, default=None)
    this_cyprian_new_year: datetime|None = field(init=False, default=None)
    db_connection: Connection|None = field(init=False, default=None)

    def __post_init__(self):
        if self.greg_year is None:
            self.greg_year = datetime.now().year
        self.cyprian_year = get_cyprian_year(self.greg_year)

    def write(self):
        """ Create a concordance, and write it to the database. """
        self.establish_connection()
        self.create_database()
        self.set_equinoctes()
        self.set_cyprian_new_years()
        self.walk_through()
        self.commit_and_close()

    def establish_connection(self):
        """ Create the Connection object. """
        self.db_connection = sqlite3.connect(self.path_to_cache_db)

    def commit_and_close(self):
        """ Commit all transactions and close the connection. """
        self.db_connection.commit()
        self.db_connection.close()

    def create_database(self):
        """ Run the create-drop script. """
        path_to_script = str(Path(__file__).parent/"sql"/"create_drop.sql")
        with open(path_to_script, "r") as script_file:
            script = script_file.read()
        cursor = self.db_connection.cursor()
        cursor.executescript(script)

    def set_equinoctes(self):
        """ Ronseal. """
        self.last_vernal_equinox = get_vernal_equinox(self.greg_year-1)
        self.this_vernal_equinox = get_vernal_equinox(self.greg_year)

    def set_cyprian_new_years(self):
        """ Ronseal. """
        self.last_cyprian_new_year = get_cyprian_new_year(self.greg_year-1)
        self.this_cyprian_new_year = get_cyprian_new_year(self.greg_year)

    def walk_through(self):
        """
        Go through each day of the Gregorian year, assigning an equivalent
        Cyprian date to each.
        """
        greg_date = self.last_cyprian_new_year
        cyprian_date = CyprianDate(self.cyprian_year, 1, 1)
        print(greg_date)
        while greg_date.year <= self.greg_year:
            if greg_date.year == self.greg_year:
                self.write_dates(greg_date, cyprian_date)
            cyprian_date.advance_one_day(greg_date)
            greg_date += timedelta(days=1)

    def write_dates(self, greg_date: datetime, cyprian_date: CyprianDate):
        """ Write the corresponding dates to the database. """
        cursor = self.db_connection.cursor()
        query = (
            "INSERT INTO Equivalence "+
            "(greg_year, greg_month, greg_day, "+
            "cyprian_year, cyprian_month, cyprian_day) "+
            "VALUES (?, ?, ?, ?, ?, ?);"
        )
        cursor.execute(
            query,
            (
                greg_date.year, greg_date.month, greg_date.day,
                cyprian_date.year, cyprian_date.month, cyprian_date.day,
            )
        )
