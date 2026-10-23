import pandas as pd

def build_features(series):
    """Create inputs and targets for 5-minute occupancy prediction.

    Args:
        series: Observed headcount at 5-minute intervals.

    Returns:
        DataFrame containing three inputs and the next headcount.
        Rows with missing observations are excluded.
    """
    return pd.DataFrame({
        "now": series,
        "lag5": series.shift(1),
        "lag10": series.shift(2),
        "next5": series.shift(-1)
    }).dropna()
