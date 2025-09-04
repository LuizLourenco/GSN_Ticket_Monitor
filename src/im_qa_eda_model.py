# src/im_qa_eda_model.py
"""
IM-QA-EDA-Model 
Incident Management - Quality Assurance - Exploratory Data Analysis Model
The module provides the functionality to analyse data from incidents in progress (pre-closure).
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from win32com.client import Dispatch
import base64
import datetime


def load_dataset():
    """ 
    Load the dataset from a CSV file.
    """
    data_file_path = './input_data/incident.csv'
    df_processing = pd.read_csv(data_file_path)
    return df_processing


def cleanup_dataset(df_processing):
    """
    Clean up the dataset by converting columns to appropriate data types.
    Returns: None
    # Adicionar mais passos de limpeza conforme necessário
    df_processing.ffill(inplace=True)  # Exemplo de imputação
    """
    #df_processing.ffill(inplace=True)
    return df_processing


def pre_process_dataset(df_processing):
    """
    Pre-process the dataset by converting columns to appropriate data types.
    """
    date_format = '%Y-%m-%d %H:%M:%S'

    # Iterate through all columns of the DataFrame
    for column in df_processing.columns:
        # Check if the column is of object type (string)
        if df_processing[column].dtype == 'object':
            # Check if the column can be converted to numeric
            if pd.to_numeric(df_processing[column], errors='coerce').notnull().all():
                df_processing[column] = pd.to_numeric(df_processing[column])
            # Check if the column can be converted to datetime
            elif pd.to_datetime(df_processing[column], format=date_format, errors='coerce').notnull().all():
                df_processing[column] = pd.to_datetime(
                    df_processing[column], format=date_format, errors='coerce')
        # Check if the column is of float type
        elif df_processing[column].dtype == 'float64':
            continue  # Mantém a coluna como float64
        # Check if the column is of int type
        elif df_processing[column].dtype == 'int64':
            df_processing[column] = df_processing[column].astype('int64')
        # Check if the column is of bool type
        elif df_processing[column].dtype == 'bool':
            df_processing[column] = df_processing[column].astype('bool')
        # Check if the column is of datetime type
        elif pd.api.types.is_datetime64_any_dtype(df_processing[column]):
            df_processing[column] = pd.to_datetime(
                df_processing[column], format=date_format, errors='coerce')
        # Convert other types to object
        else:
            df_processing[column] = df_processing[column].astype('object')
    return df_processing


def rename_columns_name(df_processing): 
    """
    Rename columns names to a more readable format.
    """
    df_processing.rename(columns={
        'number'                        : 'Number', 
        'opened_at'                     : 'Opened',
        'u_target_resolution_time'      : 'TRT',
        'short_description'             : 'Short_Description',
        'assigned_to'                   : 'Assigned',
        'u_reporting_level'             : 'Level',
        'incident_state'                : 'Incident_State',
        'caller_id'                     : 'Caller', 
        'u_site'                        : 'Site',
        'assignment_group'              : 'Assignment_Group', 
        'u_resolution_sla.percentage'   : 'SLA',
        'u_accepted_at'                 : 'Accepted',
        'u_service'                     : 'Service',
        'sys_updated_on'                : 'Updated',
        'u_incident_type'               : 'Incident_Type',
        'impact'                        : 'Impact',
        'u_supplier'                    : 'Supplier', 
        'assigned_to.email'             : 'Assigned_Email',
        'u_impacted_area'               : 'Area',
        'u_impacted_business_unit'      : 'BU',
        'cmdb_ci'                       : 'CI_CMDB'
    }, inplace=True)
    return df_processing


def customising_order_of_columns(df_processing, format_view):
    """
    Format the columns list according to the view selected.
    Parameters:
    df_processing (pandas.DataFrame): The dataset containing the columns to be formatted.
    format_view (str): The view format to apply. It can be one of the following:
                       - "std_view": Standard view with a predefined set of columns.
                       - "incident_view": Incident view with a different set of columns.
                       - "ci_view": Configuration Item (CI) view with another set of columns.
    Returns:
    pandas.DataFrame: A DataFrame containing the columns formatted according to the selected view.
    """
    if format_view == "std_view":
        columns_list = df_processing[['Number','Caller','Area','BU','Opened','TRT','Service','Assignment_Group','Assigned','Updated','Incident_Type','Impact']].copy()

    if format_view == "incident_view":
        columns_list = df_processing[['Number','Service','Area','BU','Opened','TRT','Caller','Assignment_Group','Assigned','Updated','Incident_Type','Impact']].copy()

    if format_view == "ci_view":
        columns_list = df_processing[['Number','Service','Area','BU','Opened','Caller','Assignment_Group','Assigned','Incident_Type','Impact','CI_CMDB']].copy()

    if format_view == "supplier_view":
        columns_list = df_processing[['Number','Service','Area','BU','Opened','Caller','Assignment_Group','Assigned','Incident_Type','Impact','Supplier']].copy()

    return columns_list


def convert_category_data_to_discrete_data(df_processing):
    """
    Converts categorical data to discrete data by applying factorization.
    Returns:
    None
    
    df_processing['incident_state_disc'], uniques   = pd.factorize(df_processing['Incident_State'])
    df_processing['caller_disc'], uniques           = pd.factorize(df_processing['Caller'])
    df_processing['site_disc'], uniques             = pd.factorize(df_processing['Site'])
    df_processing['assignment_group_disc'], uniques = pd.factorize(df_processing['Assignment_Group'])
    df_processing['incident_type_disc'], uniques    = pd.factorize(df_processing['Incident_Type'])
    df_processing['impact_disc'], uniques           = pd.factorize(df_processing['Impact'])
    df_processing['bu_disc'], uniques               = pd.factorize(df_processing['BU'])
    df_processing['supplier_disc'], uniques         = pd.factorize(df_processing['Supplier'])
    """
    return df_processing


def report_html_element_1_0(df_processing):
    """
    1.0 - Heatmap for correlation analysis between Incident Types and Impact
    """
    label_incident_type_order = ['Security Incident','Complaint','Incident', 'Request for Information','Request for Change Ticket','Request for Standard Change']
    label_impact_order = ['None / Minor', 'User(s)','Department','Location','Country','Region','Global']
    cmap = LinearSegmentedColormap.from_list("custom_cmap",["#DCDCDC", "#FFCC00", "#D40511"])
    matrix_incident_type_w_impact = pd.crosstab(df_processing['Incident_Type'], df_processing['Impact']).reindex(
        index=label_incident_type_order, columns=label_impact_order, fill_value=0)
    plt.figure(figsize=(8, 6))
    sns.heatmap(matrix_incident_type_w_impact, annot=True, cmap=cmap, center=8, linewidths=0.5, fmt=".0f")    
    plt.title('Correlation between Incident type and Impact').set_weight('bold')
    plt.xlabel('Impact').set_animated(True)
    plt.ylabel('Incident_Type')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('./output_data/html_element_1_0.png', dpi=150)

def report_html_element_1_1(df_processing):
    """
    Report listing the incident type filtered as "Incident" and the impact filtered as "None / Minor".
    """
    df_html_element_1_1 = df_processing[(df_processing['Incident_Type'] == 'Incident') & (df_processing['Impact'] == 'None / Minor')]
    var_html_element_1_1 = customising_order_of_columns(df_html_element_1_1, 'incident_view')
    var_html_element_1_1.head(20).to_html('./output_data/html_element_1_1.html', index=False)   


def report_html_element_1_2(df_processing):
    """
    Report listing the incident type filtered as "Request for ..." and the impact filtered as different of "None / Minor"
    """
    df_html_element_1_2 = df_processing[(df_processing['Incident_Type'].str.startswith("Request for", na=False)) & (df_processing['Impact'] != "None / Minor")]
    var_html_element_1_2 = customising_order_of_columns(df_html_element_1_2, 'incident_view') 
    var_html_element_1_2.head(20).to_html('./output_data/html_element_1_2.html', index=False)   


def report_html_element_2_0(df_processing):
    """
    2.0 - Heatmap for correlation analysis between Impacted Service and Impacted BU.
    """
    cmap = LinearSegmentedColormap.from_list("custom_cmap",["#DCDCDC", "#AFAFAF", "#D40511"])
    cross_tab = pd.crosstab(df_processing['Service'], df_processing['BU'])
    plt.figure(figsize=(8, 6))
    sns.heatmap(cross_tab, annot=True, cmap=cmap, linewidths=0.5, fmt=".0f")
    plt.title('Impacted Service vs Impacted BU - Heatmap')
    plt.xlabel('Impacted BU').set_animated(True)
    plt.ylabel('Impacted Service')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('./output_data/html_element_2_0.png', dpi=150)


def report_html_element_2_1(df_processing):
    """
    2.1 - Report that lists the incidents in which the Service does not contain the word "...LATAM".
    """
    df_html_element_2_1 = df_processing[~df_processing['Service'].str.contains(" LATAM", regex=False, na=False)]
    var_html_element_2_1 = customising_order_of_columns(df_html_element_2_1, 'incident_view')
    var_html_element_2_1.head(20).to_html('./output_data/html_element_2_1.html', index=False)   


def report_html_element_2_2(df_processing):
    """
    2.2 - Report that lists the incidents in which the Service is "DESKTOP SUPPORT DSC LATAM" and the BU is different from "DSC".
    """
    df_html_element_2_2 = df_processing[(df_processing['Service'] == "DESKTOP SUPPORT DSC LATAM") & (df_processing['BU'] != "DSC")]
    var_html_element_2_2 = customising_order_of_columns(df_html_element_2_2, 'incident_view')
    var_html_element_2_2.head(20).to_html('./output_data/html_element_2_2.html', index=False)   


def report_html_element_2_3(df_processing):
    """
    2.3 - Report that lists the incidents in which the Service is "DESKTOP SUPPORT EXP LATAM" and the BU is different from "Express".
    """
    df_html_element_2_3 = df_processing[(df_processing['Service'] == "DESKTOP SUPPORT EXP LATAM") & (df_processing['BU'] != "Express")]
    var_html_element_2_3 = customising_order_of_columns(df_html_element_2_3, 'incident_view')
    var_html_element_2_3.head(20).to_html('./output_data/html_element_2_3.html', index=False)   


def report_html_element_3_0(df_processing):
    """
    3.0 - Heatmap for correlation analysis between Assigned Group and Impacted Service
    """
    cmap = LinearSegmentedColormap.from_list("custom_cmap",["#DCDCDC", "#FFCC00", "#D40511"])
    grouped_data = df_processing.groupby(['Service', 'Assignment_Group']).size().unstack(fill_value=0)
    grouped_data = grouped_data.sort_values(by='Service', ascending=False)
    plt.figure(figsize=(8, 6))
    sns.heatmap(grouped_data, annot=True, cmap=cmap, center=9, linewidths=0.5, fmt=".0f")
    plt.title('Heatmap of Assigned Group VS Impacted Service').set_weight('bold')
    plt.xlabel('Assigned Group', labelpad=10)
    plt.ylabel('Impacted Service', labelpad=10).set_animated(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    ax = plt.gca()
    for tick in ax.get_xticklabels():
        tick.set_horizontalalignment('right')
        tick.set_x(tick.get_position()[0] - 1)
    plt.savefig('./output_data/html_element_3_0.png', dpi=150)


def report_html_element_3_1(df_processing):
    """
    Content not available. Awaiting further instructions.
    """
    # Create a sample DataFrame with lorem ipsum data
    data = {
        'Column1': ['Lorem ipsum', 'dolor sit amet', 'consectetur adipiscing'],
        'Column2': ['sed do eiusmod', 'tempor incididunt', 'ut labore et dolore'],
        'Column3': ['magna aliqua', 'Ut enim ad minim', 'veniam quis nostrud']
    }
    df_sample = pd.DataFrame(data)
    # Export the DataFrame to an HTML file
    df_sample.to_html('./output_data/html_element_3_1.html', index=False)


def report_html_element_3_2(df_processing):
    """
    Content not available. Awaiting further instructions.
    """
    # Create a sample DataFrame with lorem ipsum data
    data = {
        'Column1': ['Lorem ipsum', 'dolor sit amet', 'consectetur adipiscing'],
        'Column2': ['sed do eiusmod', 'tempor incididunt', 'ut labore et dolore'],
        'Column3': ['magna aliqua', 'Ut enim ad minim', 'veniam quis nostrud']
    }
    df_sample = pd.DataFrame(data)
    # Export the DataFrame to an HTML file
    df_sample.to_html('./output_data/html_element_3_2.html', index=False)


def report_html_element_4_0(df_processing):
    """
    4.0 - The field "Configuration Item" as Null value or "NoRecord". 
    """
    df_processing['Configuration_Item_Status'] = df_processing['CI_CMDB'].apply(lambda x: 'NoRecord' if x == 'NORECORD' else ('Null' if pd.isnull(x) else 'Others'))
    config_item_counts = df_processing['Configuration_Item_Status'].value_counts()
    custom_colors = ['#FFCC00', '#AFAFAF', '#D40511'] 
    plt.figure(figsize=(8, 6))
    sns.barplot(x=config_item_counts.index, y=config_item_counts.values, hue=config_item_counts.index, palette=custom_colors, legend=False)
    plt.title('Distribution of "Configuration Item"', fontsize=16)
    plt.xlabel("Configuration Item Data's", fontsize=11)
    plt.ylabel('Count', fontsize=11)
    for i, value in enumerate(config_item_counts.values):
        plt.text(i, value + 1, str(value), ha='center', va='bottom')

    plt.savefig('./output_data/html_element_4_0.png', dpi=150)


def report_html_element_4_1(df_processing):
    """
    4.1 Report listing the incidents in which the Configuration Item is null.
    """
    df_html_element_4_1 = df_processing[(df_processing['CI_CMDB'].isnull())]
    var_html_element_4_1 = customising_order_of_columns(df_html_element_4_1, 'ci_view')
    var_html_element_4_1.head(20).to_html('./output_data/html_element_4_1.html', index=False)   


def report_html_element_4_2(df_processing):
    """
    4.2 Report listing the incidents in which the Configuration Item is null.
    """
    df_html_element_4_2 = df_processing[df_processing['CI_CMDB'] == 'NORECORD']
    var_html_element_4_2 = customising_order_of_columns(df_html_element_4_2, 'ci_view')
    var_html_element_4_2.head(20).to_html('./output_data/html_element_4_2.html', index=False)   


def report_html_element_5_0(df_processing):
    """
    5.0 - The field "Incident Status" as Pending Supplier and field Supplier as "Null" value.
    """
    pending_supplier_df = df_processing[df_processing['Incident_State'] == "Pending Supplier"]
    opened_at_counts = df_processing['Opened'].dt.date.value_counts().sort_index()
    pending_supplier_counts = pending_supplier_df['Opened'].dt.date.value_counts().sort_index()
    plt.figure(figsize=(8, 6))
    plt.plot(opened_at_counts.index, opened_at_counts.values, label='Total Calls Opened', marker='o')
    plt.plot(pending_supplier_counts.index, pending_supplier_counts.values, label='Status as "Pending Supplier"', marker='o')
    plt.title('Number of INC registered by date')
    plt.xlabel('Date')
    plt.ylabel("Count of Recorded Incidents")
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('./output_data/html_element_5_0.png', dpi=150)


def report_html_element_5_1(df_processing):
    """
    5.1 - Report listing the incidents in which the State is "Pending Supplier" and the Supplier is null
    """
    df_html_element_5_1 = df_processing[(df_processing['Incident_State'] == "Pending Supplier") & (df_processing['Supplier'].isnull())]
    var_html_element_5_1 = customising_order_of_columns(df_html_element_5_1, 'supplier_view')
    var_html_element_5_1.head(20).to_html('./output_data/html_element_5_1.html', index=False)


def report_html_element_5_2(df_processing):
    """
    5.2 - Report listing the incidents in which the State is "Pending Supplier" and the Supplier is not null
    """
    df_html_element_5_2 = df_processing[(df_processing['Incident_State'] == "Pending Supplier") & (df_processing['Supplier'].notnull())]
    var_html_element_5_2 = customising_order_of_columns(df_html_element_5_2, 'supplier_view')
    var_html_element_5_2.head(20).to_html('./output_data/html_element_5_2.html', index=False)


def report_html_element_6_0(df_processing):
    """
    Awaiting further instructions.
    """
    pass


def report_html_element_6_1(df_processing):
    """
    6.1 - Descriptive statistics for categorical columns in the dataset.
    """
    df_processing.describe(include=['object']).transpose().to_html('./output_data/html_element_6_1.html')  



def report_html_element_6_2(df_processing):
    """
    Content not available. Awaiting further instructions.
    """
    # Create a sample DataFrame with lorem ipsum data
    data = {
        'Column1': ['Lorem ipsum', 'dolor sit amet', 'consectetur adipiscing'],
        'Column2': ['sed do eiusmod', 'tempor incididunt', 'ut labore et dolore'],
        'Column3': ['magna aliqua', 'Ut enim ad minim', 'veniam quis nostrud']
    }
    df_sample = pd.DataFrame(data)
    # Export the DataFrame to an HTML file
    df_sample.to_html('./output_data/html_element_6_2.html', index=False)


def send_mail_outlook():
    """
    Send an email with the analysis report as an attachment.
    """
    # Check if Outlook is open, if not, open it
    try:
        outlook = Dispatch('Outlook.Application')
    except Exception as e:
        print("Outlook is not open. Opening Outlook...")
        subprocess.Popen(['outlook.exe'])
        time.sleep(5)  # Wait for Outlook to open
        outlook = Dispatch('Outlook.Application')


    outlook = Dispatch('Outlook.Application')
    mail = outlook.CreateItem(0)
    mail.Subject = '[TEST] Incident Management: Exploratory Data Analysis Report - Pre-Closure'
    mail.To = 'br.its.eus@dhl.com'
    mail.CC = 'luiz.lourenco@dhl.com'


    # Estruturar o HTMLBody
    with open('src/Mail_Body_Model.html', 'r', encoding='utf-8') as file:
        html_body_model = file.read()

    # Codificar a imagem em base64
    with open("./output_data/html_element_1_0.png", "rb") as image_file:
        var_html_element_1_0 = base64.b64encode(image_file.read()).decode('utf-8')        

    # Carregar o conteúdo do arquivo html_element_1_1.html 
    with open('./output_data/html_element_1_1.html', 'r', encoding='utf-8') as file:
        var_html_element_1_1 = file.read()

    # Carregar o conteúdo do arquivo html_element_1_2.html 
    with open('./output_data/html_element_1_2.html', 'r', encoding='utf-8') as file:
        var_html_element_1_2 = file.read()

    # Codificar a imagem em base64
    with open("./output_data/html_element_2_0.png", "rb") as image_file:
        var_html_element_2_0 = base64.b64encode(image_file.read()).decode('utf-8')        

    # Carregar o conteúdo do arquivo html_element_2_1.html 
    with open('./output_data/html_element_2_1.html', 'r', encoding='utf-8') as file:
        var_html_element_2_1 = file.read()

    # Carregar o conteúdo do arquivo html_element_2_2.html 
    with open('./output_data/html_element_2_2.html', 'r', encoding='utf-8') as file:
        var_html_element_2_2 = file.read()

    # Carregar o conteúdo do arquivo html_element_2_3.html 
    with open('./output_data/html_element_2_3.html', 'r', encoding='utf-8') as file:
        var_html_element_2_3 = file.read()

    # Codificar a imagem em base64
    with open("./output_data/html_element_3_0.png", "rb") as image_file:
        var_html_element_3_0 = base64.b64encode(image_file.read()).decode('utf-8')        

    # Carregar o conteúdo do arquivo html_element_3_1.html 
    with open('./output_data/html_element_3_1.html', 'r', encoding='utf-8') as file:
        var_html_element_3_1 = file.read()

    # Carregar o conteúdo do arquivo html_element_3_2.html 
    with open('./output_data/html_element_3_2.html', 'r', encoding='utf-8') as file:
        var_html_element_3_2 = file.read()

    # Codificar a imagem em base64
    with open("./output_data/html_element_4_0.png", "rb") as image_file:
        var_html_element_4_0 = base64.b64encode(image_file.read()).decode('utf-8')        

    # Carregar o conteúdo do arquivo html_element_4_1.html 
    with open('./output_data/html_element_4_1.html', 'r', encoding='utf-8') as file:
        var_html_element_4_1 = file.read()

    # Carregar o conteúdo do arquivo html_element_4_2.html 
    with open('./output_data/html_element_4_2.html', 'r', encoding='utf-8') as file:
        var_html_element_4_2 = file.read()

    # Codificar a imagem em base64
    with open("./output_data/html_element_5_0.png", "rb") as image_file:
        var_html_element_5_0 = base64.b64encode(image_file.read()).decode('utf-8')        

    # Carregar o conteúdo do arquivo html_element_5_1.html 
    with open('./output_data/html_element_5_1.html', 'r', encoding='utf-8') as file:
        var_html_element_5_1 = file.read()

    # Carregar o conteúdo do arquivo html_element_5_2.html 
    with open('./output_data/html_element_5_2.html', 'r', encoding='utf-8') as file:
        var_html_element_5_2 = file.read()

    # Codificar a imagem em base64
    with open("./output_data/html_element_0_0.png", "rb") as image_file:
        var_html_element_6_0 = base64.b64encode(image_file.read()).decode('utf-8')        

    # Carregar o conteúdo do arquivo html_element_6_1.html 
    with open('./output_data/html_element_6_1.html', 'r', encoding='utf-8') as file:
        var_html_element_6_1 = file.read()

    # Carregar o conteúdo do arquivo html_element_6_2.html 
    with open('./output_data/html_element_6_2.html', 'r', encoding='utf-8') as file:
        var_html_element_6_2 = file.read()

    # Get the current date
    current_date_server = (
        datetime.datetime.now(datetime.timezone.utc)
        .strftime("%Y-%m-%d %H:%M:%S")
    )

    # Inserir as variáveis HTML e a string base64 e no modelo HTML dentro do html_body_model
    html_body_model = html_body_model.format(
        html_element_1_0=var_html_element_1_0,
        html_element_1_1=var_html_element_1_1,
        html_element_1_2=var_html_element_1_2,

        html_element_2_0=var_html_element_2_0,
        html_element_2_1=var_html_element_2_1,
        html_element_2_2=var_html_element_2_2,
        html_element_2_3=var_html_element_2_3,

        html_element_3_0=var_html_element_3_0,
        html_element_3_1=var_html_element_3_1,
        html_element_3_2=var_html_element_3_2,

        html_element_4_0=var_html_element_4_0,
        html_element_4_1=var_html_element_4_1,
        html_element_4_2=var_html_element_4_2,

        html_element_5_0=var_html_element_5_0,
        html_element_5_1=var_html_element_5_1,
        html_element_5_2=var_html_element_5_2,

        html_element_6_0=var_html_element_6_0,
        html_element_6_1=var_html_element_6_1,
        html_element_6_2=var_html_element_6_2,
        html_element_current_date=current_date_server
        )

    # Definir o corpo do HTML do e-mail
    mail.HTMLBody = html_body_model

    # Adicionar anexos
    # mail.Attachments.Add('./output_data/file.txt')

    # 8. Envio do Email
    mail.Send()


def main():
    """
    Init all process.
    """
    my_dataset = load_dataset()
    my_dataset = cleanup_dataset(my_dataset)
    my_dataset = pre_process_dataset(my_dataset)
    my_dataset = rename_columns_name(my_dataset)
    my_dataset = convert_category_data_to_discrete_data(my_dataset)
    report_html_element_1_0(my_dataset)
    report_html_element_1_1(my_dataset)
    report_html_element_1_2(my_dataset)
    report_html_element_2_0(my_dataset)
    report_html_element_2_1(my_dataset)
    report_html_element_2_2(my_dataset)
    report_html_element_2_3(my_dataset)
    report_html_element_3_0(my_dataset)
    report_html_element_3_1(my_dataset)
    report_html_element_3_2(my_dataset)
    report_html_element_4_0(my_dataset)
    report_html_element_4_1(my_dataset)
    report_html_element_4_2(my_dataset)
    report_html_element_5_0(my_dataset)
    report_html_element_5_1(my_dataset)
    report_html_element_5_2(my_dataset)
    report_html_element_6_0(my_dataset)
    report_html_element_6_1(my_dataset)
    report_html_element_6_2(my_dataset)
    send_mail_outlook()
    print("Processamento concluído.")


main()


# End of script
