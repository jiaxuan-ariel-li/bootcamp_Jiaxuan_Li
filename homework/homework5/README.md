# Homework 5 — Data Storage

## Data Storage

This project uses separate folders for raw and processed data:

```text
data/
├── raw/
└── processed/
```

- `data/raw/` stores raw data in CSV format.
- `data/processed/` stores processed data in Parquet format.

CSV is used for raw data because it is simple, human-readable, and widely supported. Parquet is used for processed data because it preserves data types and provides efficient columnar storage.

The data paths are configured using environment variables in the `.env` file:

```text
DATA_DIR_RAW=data/raw
DATA_DIR_PROCESSED=data/processed
```

The notebook loads these variables with `python-dotenv` and uses them to determine where data should be stored and loaded.

The `write_df()` and `read_df()` utility functions automatically select the correct storage method based on the file suffix:

- `.csv` uses `to_csv()` and `read_csv()`
- `.parquet` uses `to_parquet()` and `read_parquet()`

The utility functions also create missing directories when needed and provide a clear error message if a Parquet engine such as `pyarrow` or `fastparquet` is not installed.