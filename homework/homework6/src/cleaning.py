from __future__ import annotations

from collections.abc import Iterable
import pandas as pd


def _resolve_columns(df: pd.DataFrame, columns: Iterable[str] | None) -> list[str]:
    """Return a validated list of columns."""
    if columns is None:
        return df.select_dtypes(include="number").columns.tolist()

    columns = list(columns)
    missing = [col for col in columns if col not in df.columns]
    if missing:
        raise KeyError(f"Columns not found in DataFrame: {missing}")
    return columns


def fill_missing_median(
    df: pd.DataFrame,
    columns: Iterable[str] | None = None,
) -> pd.DataFrame:
    result = df.copy()
    columns = _resolve_columns(result, columns)

    for col in columns:
        if not pd.api.types.is_numeric_dtype(result[col]):
            raise TypeError(f"Median imputation requires a numeric column: {col}")
        median = result[col].median()
        if pd.isna(median):
            raise ValueError(f"Cannot compute a median for an all-missing column: {col}")
        result[col] = result[col].fillna(median)

    return result


def drop_missing(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    if not 0 <= threshold <= 1:
        raise ValueError("threshold must be between 0 and 1")

    result = df.copy()
    missing_fraction = result.isna().mean()
    columns_to_drop = missing_fraction[missing_fraction > threshold].index.tolist()
    result = result.drop(columns=columns_to_drop)
    result = result.dropna().reset_index(drop=True)
    return result


def normalize_data(
    df: pd.DataFrame,
    columns: Iterable[str] | None = None,
) -> pd.DataFrame:
    """Apply Min-Max normalization to selected numeric columns.

    Each selected feature is transformed to the interval [0, 1] using
    ``(x - min) / (max - min)``. A constant-valued column is mapped to 0.0 to
    avoid division by zero.

    Parameters
    ----------
    df:
        Input DataFrame.
    columns:
        Numeric columns to normalize. If omitted, all numeric columns are used.

    Returns
    -------
    pandas.DataFrame
        A normalized copy of ``df``.
    """
    result = df.copy()
    columns = _resolve_columns(result, columns)

    for col in columns:
        if not pd.api.types.is_numeric_dtype(result[col]):
            raise TypeError(f"Normalization requires a numeric column: {col}")
        minimum = result[col].min()
        maximum = result[col].max()
        value_range = maximum - minimum
        if pd.isna(value_range):
            continue
        if value_range == 0:
            result[col] = 0.0
        else:
            result[col] = (result[col] - minimum) / value_range

    return result
