""" Clean up the dataset by converting columns to appropriate data types. """
def cleanup_dataset(df_processing):
    """ 
    Clean up the dataset by converting columns to appropriate data types. 
    """
    df_data_proc = df_processing
    
    # The .ffill method is used in pandas to fill in missing values (NaN) in a DataFrame or Series.
    # It performs a forward fill, i.e. it fills the missing values with the last non-missing value previously found in the same column.
    #.ffill() or method='ffill' for forward fill (fill with the previous value).
    #.bfill() or method='bfill' for backward fill (fill with the next value).
    # Example of use:
    #                df_data_proc.ffill(inplace=True) or df_data_proc.bfill(inplace=True) 
    #                df_data_proc..fillna(method='ffill',inplace=True) or df_data_proc..fillna(method='bfill',inplace=True)

    # Remove duplicated records
    # df_data_proc.drop_duplicates(inplace=True)

    # Removes records with null values or missing
    # df_data_proc.dropna(inplace=True)
 
    # Fill missing values with appropriate strategies
    # For numeric columns, fill with the mean
    # Example of use:
    #       numeric_cols = df_data_proc.select_dtypes(include=['float64', 'int64']).columns
    #       df_data_proc[numeric_cols] = df_data_proc[numeric_cols].fillna(df_data_proc[numeric_cols].mean())

    # For categorical columns, fill with the mode
    # Example of use:
    #       categorical_cols = df_data_proc.select_dtypes(include=['object']).columns
    #       df_data_proc[categorical_cols] = df_data_proc[categorical_cols].fillna(df_data_proc[categorical_cols].mode().iloc[0])

    # For categorical columns, fill with a specific value
    categorical_cols = df_data_proc.select_dtypes(include=['object']).columns
    df_data_proc[categorical_cols] = df_data_proc[categorical_cols].fillna('(empty)')

    # For datetime columns, fill with the most recent date
    # Example of use:
    #       datetime_cols = df_data_proc.select_dtypes(include=['datetime64']).columns
    #       df_data_proc[datetime_cols] = df_data_proc[datetime_cols].fillna(df_data_proc[datetime_cols].max())
    
    
    return df_data_proc