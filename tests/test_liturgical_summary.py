"""
This code tests the LiturgicalSummary class.
"""

# Standard imports.
from datetime import datetime

# Source imports.
from source.liturgical_summary import LiturgicalSummary

#########
# TESTS #
#########

def test_liturgical_summary():
    """ Test the main class. """
    summary = LiturgicalSummary(2025)
    assert summary.christmas == datetime(2025, 12, 25)