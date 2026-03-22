import pandas as pd

def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    result = samples.copy()

    result["has_start"] = result["dna_sequence"].str.startswith("ATG").astype(int)

    result["has_stop"] = result["dna_sequence"].str.endswith(
        ("TAA", "TAG", "TGA")
    ).astype(int)

    result["has_atat"] = result["dna_sequence"].str.contains("ATAT").astype(int)

    result["has_ggg"] = result["dna_sequence"].str.contains("G{3,}").astype(int)

    result = result.sort_values("sample_id")

    return result