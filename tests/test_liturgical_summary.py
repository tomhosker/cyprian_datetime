"""
This code tests the LiturgicalSummary class.
"""

# Source imports.
from source.liturgical_summary import LiturgicalSummary

#########
# TESTS #
#########

def test_liturgical_summary():
    """ Test the main class. """
    year = 2025
    summary = LiturgicalSummary(year)
    lookup = summary.to_lookup()
    assert lookup[f"{year}-04-20T00:00:00"] == "Easter Sunday"
    assert lookup[f"{year}-12-01T00:00:00"] == "Advent Sunday"
    assert lookup[f"{year}-12-25T00:00:00"] == "Christmas"
