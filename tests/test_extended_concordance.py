"""
This code tests the LiturgicalSummary class.
"""

# Source imports.
from source.extended_concordance import ExtendedConcordance

#########
# TESTS #
#########

def test_extended_concordance():
    """ Test the main class. """
    year = 2025
    concordance_obj = ExtendedConcordance(year)
    found_easter = False
    for equivalent in concordance_obj.equivalents:
        if equivalent.liturgical == "Easter Sunday":
            found_easter = True
            assert equivalent.greg.year == year
            assert equivalent.greg.month == 4
            assert equivalent.greg.day == 20
            assert equivalent.cyprian.year == 12
            assert equivalent.cyprian.month == 1
            assert equivalent.cyprian.day == 23
            break
    assert found_easter
    concordance_obj.export_latex_file()
