from source.extended_concordance import ExtendedConcordance

YEAR = 2025

def run():
    concordance_obj = ExtendedConcordance(YEAR)
    print(f"File written to: {concordance_obj.export_latex_file()}")

if __name__ == "__main__":
    run()
