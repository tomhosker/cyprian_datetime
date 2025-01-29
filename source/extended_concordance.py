"""
This code defines a class which produces a concordance for a given number of
years.
"""

# Standard imports.
from dataclasses import dataclass
from datetime import datetime, timedelta

# Local imports.
from .frontend_utils import convert_greg_to_cyprian

##############
# MAIN CLASS #
##############

@dataclass
class ExtendedConcordance:
    start_year: int
    end_year: int
    equivalents: list[dict]|None = None

    def fill_equivalents(self):
        """ Ronseal. """
        self.equivalents = []
        today = datetime(self.start_year, 1, 1)
        while today.year <= self.end_year:
            equivalent = {
                "greg": today,
                "cyprian": convert_greg_to_cyprian(today)
            }
            self.equivalents.append(equivalent)
            today += timedelta(days=1)

    def export_dict(self):
        """ Ronseal. """
        result = []
        for equivalent in self.equivalents:
            equivalent_json = {
                "greg": str(equivalent["greg"]),
                "cyprian": equivalent["cyprian"].to_dict()
            }
            result.append(equivalent_json)
        return result

    def export_latex_table(self):
        """ Ronseal. """
        lines = [
            "\\begin{table}",
            "    \\begin{tabular}{|l|l|}",
            "        \\hline",
            "        \\textbf{Gregorian} & \\textbf{Cyprian} \\\\",
            "        \\hline"
        ]
        for equivalent in self.equivalents:
            greg = equivalent["greg"]
            cyprian = equivalent["cyprian"]
            if greg.day == 1 or cyprian.day == 1:
                greg_str = greg.strftime("%d %b %Y")
                cyprian_str = cyprian.to_latex()
                row = f"        {greg_str} & {cyprian_str} \\\\"
                lines.append(row)
        lines += [
            "        \\hline",
            "    \\end{tabular}",
            "\\end{table}"
        ]
        result = "\n".join(lines)
        return result
