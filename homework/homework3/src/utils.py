
def get_summary_stats(df, group_col=None):
    """
    Generate basic summary statistics for a pandas DataFrame.

    Parameters:
        df: pandas DataFrame
        group_col: optional column name used for grouping

    Returns:
        A dictionary containing summary statistics
    """

    results = {}

    # Basic dataset information
    results["shape"] = df.shape
    results["columns"] = list(df.columns)

    # Missing values for each column
    results["missing_values"] = df.isnull().sum()

    # Summary statistics for numeric columns
    results["numeric_summary"] = df.describe()

    # Optional groupby analysis
    if group_col is not None:
        if group_col in df.columns:
            results["group_summary"] = (
                df.groupby(group_col)
                  .mean(numeric_only=True)
            )
        else:
            print(f"Warning: '{group_col}' is not a valid column.")

    return results