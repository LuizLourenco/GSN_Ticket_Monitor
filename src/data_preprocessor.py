"""
### `pre_process_dataset(df_processing)`

Pre-processes a DataFrame by converting its columns to appropriate data types.

- **Parameters:**
  - `df_processing` (pd.DataFrame): The DataFrame to be processed.

- **Returns:**
  - `pd.DataFrame`: The processed DataFrame with columns converted to appropriate data types.

- **Details:**
  - Converts 'object' columns to numeric if possible, otherwise attempts to parse as dates.
  - Ensures 'float64', 'int64', and 'bool' columns retain their types.
  - Re-parses datetime columns using predefined date formats.
  - Converts any other types to 'object'.
"""
import pandas as pd

def pre_process_dataset(df_processing):
    """ 
    Pre-process the dataset by converting columns to appropriate data types. 
    """
    date_formats = ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d', '%d-%b-%Y']

    for column in df_processing.columns:
        if df_processing[column].dtype == 'object':
            if pd.to_numeric(df_processing[column], errors='coerce').notnull().all():
                df_processing[column] = pd.to_numeric(df_processing[column])
            else:
                for date_format in date_formats:
                    try:
                        df_processing[column] = pd.to_datetime(df_processing[column], format=date_format, errors='raise')
                        break
                    except ValueError:
                        continue
        elif df_processing[column].dtype == 'float64':
            continue
        elif df_processing[column].dtype == 'int64':
            df_processing[column] = df_processing[column].astype('int64')
        elif df_processing[column].dtype == 'bool':
            df_processing[column] = df_processing[column].astype('bool')
        elif pd.api.types.is_datetime64_any_dtype(df_processing[column]):
            for date_format in date_formats:
                try:
                    df_processing[column] = pd.to_datetime(df_processing[column], format=date_format, errors='raise')
                    break
                except ValueError:
                    continue
        else:
            df_processing[column] = df_processing[column].astype('object')

    return df_processing
