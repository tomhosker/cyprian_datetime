from source.extended_concordance import ExtendedConcordance

def run():
    concordance_obj = ExtendedConcordance(2025, 2026)
    concordance_obj.fill_equivalents()
    print(concordance_obj.export_latex_table())

if __name__ == "__main__":
    run()
