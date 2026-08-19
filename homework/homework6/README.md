# Homework 6 — Data Preprocessing

This project implements a simple, reproducible data-preprocessing workflow. The notebook loads the raw sample dataset, applies reusable cleaning functions from `src/cleaning.py`, saves the cleaned dataset, and compares the original data with the processed result.

## Cleaning Strategy

The preprocessing workflow follows these rules:

- **Median imputation:** Missing values in the continuous numerical columns `age`, `income`, and `score` are filled with the median of the corresponding column. The median is used because it is less sensitive to extreme values than the mean.
- **Remove highly incomplete columns:** Columns with more than 50% missing values are dropped. In the sample dataset, `extra_data` has 5 missing values out of 7 observations (about 71.4%), so it is removed.
- **Min-Max normalization:** The continuous numerical features `age`, `income`, and `score` are normalized to the range `[0, 1]`.
- **Preserve categorical and identifier-like data:** `zipcode` is treated as an identifier/categorical feature rather than a continuous numerical variable, so it is not normalized. `city` is also categorical and is left unchanged.
- **Treat `Unknown` as a category:** The string `Unknown` in the `city` column is treated as a valid categorical value rather than a missing value.
- **Preserve rows when possible:** No rows are intentionally removed because the numerical missing values can be imputed and the highly incomplete `extra_data` column can be dropped instead.

The cleaned dataset is saved as:

`data/processed/sample_data_cleaned.csv`

## Project Structure

```text
homework6/
├── data/
│   ├── raw/
│   │   └── sample_data.csv
│   └── processed/
│       └── sample_data_cleaned.csv
├── notebooks/
│   └── stage06_data-preprocessing_homework-starter.ipynb
├── src/
│   └── cleaning.py
└── README.md
```

The notebook is intended to be run from the `notebooks/` directory, so its data paths use `../data/...` and the project root is added to Python's module search path before importing `src.cleaning`.
