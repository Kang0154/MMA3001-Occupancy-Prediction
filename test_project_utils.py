import pandas as pd
from project_utils import build_features

def test_features():
    s = pd.Series([0, 1, 2, 3, 4, 5])
    result = build_features(s)
    assert len(result) == 3
    assert result.loc[2, "next5"] == 3
    assert result.loc[2, "lag10"] == 0

def test_missing_data():
    s = pd.Series([0, 1, 2, 3, None, 5, 6])
    result = build_features(s)
    assert len(result) == 1
    assert not result.isna().any().any()

def test_short_data():
    s = pd.Series([1, 2, 3])
    assert build_features(s).empty
