"""This module is used to format the columns list according to the view selected."""

def customising_order_of_columns(df_processing, format_view):
    """ Format the columns list according to the view selected. """

    if format_view == None:
        columns_list = df_processing[df_processing.columns.tolist()].copy()

    elif format_view == "incident_view":
        columns_list = df_processing[['Number', 'Opened', 'Service', 'Area', 'BU', 'Caller', 'Assignment_Group', 'Assigned', 'Incident_Type', 'Impact', 'Updated']].copy()

    elif format_view == "incident_type_impact_view":
        columns_list = df_processing[['Number', 'Opened', 'Incident_Type', 'Impact', 'Area', 'BU', 'Caller', 'Service', 'Assignment_Group', 'Assigned', 'Updated']].copy()

    elif format_view == "ci_view":
        columns_list = df_processing[['Number', 'Opened', 'Incident_Type', 'Impact', 'Area', 'BU', 'Caller', 'Service', 'Assigned', 'CI_CMDB', 'Updated']].copy()

    elif format_view == "supplier_view":
        columns_list = df_processing[['Number', 'Opened', 'Incident_Type', 'Impact', 'Area', 'BU', 'Service', 'Incident_State', 'Supplier', 'CI_CMDB', 'CI_Category', 'CI_Folder', 'CI_Model_ID','Updated']].copy()

    elif format_view == "impact_view":
        columns_list = df_processing[['Number', 'Opened', 'Service', 'Area', 'BU', 'Caller', 'Assignment_Group', 'Assigned', 'Incident_Type', 'Impact', 'Updated']].copy()

    return columns_list

