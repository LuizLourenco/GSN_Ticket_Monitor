""" This module contains functions to convert categorical data to discrete data. """
def convert_category_data_to_discrete_data(df_processing):
    """
    Converts categorical data to discrete data by applying factorization.
    Returns:
    None
    """
    df_data_proc = df_processing.copy()
    #df_data_proc['Incident_State_disc'], uniques   = pd.factorize(df_data_proc['Incident_State'])
    #df_data_proc['caller_disc'], uniques           = pd.factorize(df_data_proc['Caller'])
    #df_data_proc['site_disc'], uniques             = pd.factorize(df_data_proc['Site'])
    #df_data_proc['assignment_group_disc'], uniques = pd.factorize(df_data_proc['Assignment_Group'])
    #df_data_proc['incident_type_disc'], uniques    = pd.factorize(df_data_proc['Incident_Type'])
    #df_data_proc['impact_disc'], uniques           = pd.factorize(df_data_proc['Impact'])
    #df_data_proc['bu_disc'], uniques               = pd.factorize(df_data_proc['BU'])
    #df_data_proc['supplier_disc'], uniques         = pd.factorize(df_data_proc['Supplier'])    
    
    return df_data_proc

