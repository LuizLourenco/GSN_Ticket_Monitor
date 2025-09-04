"""  This module contains the function to load the dataset from a CSV file. """
import pandas as pd


def load_dataset(file_path):
    """
    Load the dataset from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The loaded dataset as a pandas DataFrame.
    """
    dataframe = pd.read_csv(file_path)
    return dataframe
