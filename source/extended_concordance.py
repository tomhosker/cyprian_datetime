"""
This code defines a class which produces a concordance for a given number of
years.
"""

# Standard imports.
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path

# Local imports.
from .cyprian_date import CyprianDate
from .frontend_utils import convert_greg_to_cyprian
from .liturgical_summary import LiturgicalSummary

# Local constants.
PATH_TO_TEMP = "_temp"
PATH_OBJ_TO_TEX = Path(__file__).parent/"tex"
PATH_TO_CONCORDANCE_BASE = str(PATH_OBJ_TO_TEX/"concordance_base.tex")

##############
# MAIN CLASS #
##############

@dataclass
class ExtendedConcordance:
    """ A class to hold an concordance extended in scope. """
    year: int
    liturgical_summary: LiturgicalSummary|None = field(init=False, default=None)
    equivalents: list[dict]|None = field(init=False, default=None)

    def __post_init__(self):
        self.liturgical_summary = LiturgicalSummary(self.year)
        self.fill_equivalents()

    def fill_equivalents(self):
        """ Ronseal. """
        self.equivalents = []
        today = datetime(self.year, 1, 1)
        while today.year == self.year:
            cyprian = convert_greg_to_cyprian(today)
            liturgical = \
                find_liturgical_equivalent(today, self.liturgical_summary)
            equivalent = Equivalent(today, cyprian, liturgical)
            self.equivalents.append(equivalent)
            today += timedelta(days=1)

    def export_dict(self) -> dict:
        """ Ronseal. """
        result = [equivalent.to_json() for equivalent in self.equivalents]
        return result

    def make_latex_rows(self) -> str:
        """ Ronseal. """
        lines = []
        for equ in self.equivalents:
            if equ.greg.day == 1 or equ.cyprian.day == 1 or equ.liturgical:
                greg = equ.greg_latex
                cyprian = equ.cyprian_latex
                liturgical = equ.liturgical_latex
                row = f"        {greg} & {cyprian} & {liturgical} \\\\"
                lines.append(row)
        result = "\n".join(lines)
        return result

    def export_latex_file(self) -> str:
        """ Put a summmary of the concordance into a LaTeX file. """
        with open(PATH_TO_CONCORDANCE_BASE, "r") as base_file:
            code = base_file.read()
        rows = self.make_latex_rows()
        code = code.replace("#YEAR", str(self.year))
        code = code.replace("#ROWS", rows)
        path_obj_to_temp = Path(PATH_TO_TEMP)
        path_obj_to_temp.mkdir(exist_ok=True)
        path_to_output = str(path_obj_to_temp/f"concordance{self.year}.tex")
        with open(path_to_output, "w") as output_file:
            output_file.write(code)
        return path_to_output

################################
# HELPER CLASSES AND FUNCTIONS #
################################

@dataclass(frozen=True)
class Equivalent:
    """ A class to hold several equivalent dates. """
    greg: datetime
    cyprian: CyprianDate
    liturgical: str|None

    @property
    def greg_json(self) -> str:
        """ Get the field in a JSON-friendly form. """
        return str(self.greg)

    @property
    def cyprian_json(self) -> dict:
        """ Get the field in a JSON-friendly form. """
        return self.cyprian.to_dict()

    @property
    def liturgical_json(self) -> dict:
        """ Get the field in a JSON-friendly form. """
        return self.liturgical

    @property
    def greg_latex(self) -> str:
        """ Get the field in a LaTeX-friendly form. """
        return self.greg.strftime("%d %b %Y")

    @property
    def cyprian_latex(self) -> dict:
        """ Get the field in a LaTeX-friendly form. """
        return self.cyprian.to_latex()

    @property
    def liturgical_latex(self) -> dict:
        """ Get the field in a LaTeX-friendly form. """
        if self.liturgical:
            return self.liturgical
        return "---"

    def to_json(self) -> dict:
        """ Ronseal. """
        result = {
            "greg": self.greg_json,
            "cyprian": self.cyprian_json,
            "liturgical": self.liturgical_json
        }
        return result

def find_liturgical_equivalent(
    greg: datetime,
    liturgical_summary: LiturgicalSummary
) -> str|None:
    """ Find the liturgical equivalent to a given date, if it exists. """
    key = greg.isoformat()
    lookup = liturgical_summary.to_lookup()
    result = lookup.get(key)
    return result
