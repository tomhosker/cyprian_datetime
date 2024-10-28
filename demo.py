from datetime import datetime

from source.concordance import Concordance
from source.cyprian_date import CyprianDate

def run():
    concordance = Concordance()
    concordance.write()
    print(concordance.convert_gregorian())
    print(concordance.convert_gregorian(datetime(2025, 1, 1)))
    print(concordance.convert_cyprian(CyprianDate(11, 10, 3)))

if __name__ == "__main__":
    run()
