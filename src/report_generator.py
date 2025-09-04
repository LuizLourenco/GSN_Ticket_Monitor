"""  Module for generating the HTML report elements. """

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from column_formatter import customising_order_of_columns 


def report_html_element_1_0(df_processing):
    """ 
    1.0 - Heatmap for correlation analysis between Incident Types and Impact
    """
    label_inc_type_order = ['Security Incident', 'Complaint', 'Incident', 'Request for Information', 'Request for Change Ticket', 'Request for Standard Change']
    label_impact_order = ['None / Minor', 'User(s)', 'Department', 'Location', 'Country', 'Region', 'Global']
    cmap = LinearSegmentedColormap.from_list("custom_cmap", ["#DCDCDC", "#FFCC00", "#D40511"])
    matrix = pd.crosstab(df_processing['Incident_Type'], df_processing['Impact']).reindex(index=label_inc_type_order, columns=label_impact_order, fill_value=0)
    plt.figure(figsize=(8, 6))
    sns.heatmap(matrix, annot=True, cmap=cmap, center=50, linewidths=0.5, fmt=".0f")    
    plt.title('Correlation between Incident type and Impact').set_weight('bold')
    plt.xlabel('Impact').set_animated(True)
    plt.ylabel('Incident_Type')
    plt.xticks(rotation=45)
    plt.tight_layout()
        
    plt.savefig('./src/output/html_element_1_0.png', dpi=150)


def report_html_element_1_1(df_processing):
    """
    1.1 - Report listing the incident type filtered as "Incident" and the impact filtered as "None / Minor".
    """
    df_1_1 = df_processing[(df_processing['Incident_Type'] == 'Incident') & (df_processing['Impact'] == 'None / Minor')].sort_values(by=['Area', 'BU', 'Assignment_Group', 'Assigned'])
    df_1_1 = customising_order_of_columns(df_1_1, 'incident_type_impact_view')
    df_1_1.head(20).to_html('./src/output/html_element_1_1.html', index=False)


def report_html_element_1_2(df_processing):
    """
    1.2 - Report listing the incident type filtered as "Request for ..." and the impact filtered as different of "None / Minor"
    """
    df_1_2 = df_processing[(df_processing['Incident_Type'].str.startswith("Request for", na=False)) & (df_processing['Impact'] != "None / Minor")].sort_values(by=['Area', 'BU', 'Assignment_Group', 'Assigned'])
    df_1_2 = customising_order_of_columns(df_1_2, 'incident_type_impact_view')
    df_1_2.head(20).to_html('./src/output/html_element_1_2.html', index=False)


def report_html_element_2_0(df_processing):
    """
    2.0 - Heatmap for correlation analysis between Impacted Service and Impacted BU.
    """
    cmap = LinearSegmentedColormap.from_list("custom_cmap",["#DCDCDC", "#D40511"])
    cross_tab = pd.crosstab(df_processing['Service'], df_processing['BU'])
    plt.figure(figsize=(8, 6))
    sns.heatmap(cross_tab, annot=True, cmap=cmap, center=30, linewidths=0.5, fmt=".0f")
    plt.title('Impacted Service vs Impacted BU - Heatmap')
    plt.xlabel('Impacted BU').set_animated(True)
    plt.ylabel('Impacted Service')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('./src/output/html_element_2_0.png', dpi=150)


def report_html_element_2_1(df_processing):
    """
    2.1 - Report that lists the incidents in which the Service does not contain the word "...LATAM".
    """
    df_2_1 = df_processing[~df_processing['Service'].str.contains(" LATAM", regex=False, na=False)].sort_values(by=['Area', 'BU', 'Assignment_Group', 'Assigned'])
    df_2_1 = customising_order_of_columns(df_2_1, 'incident_type_impact_view')
    df_2_1.head(20).to_html('./src/output/html_element_2_1.html', index=False)


def report_html_element_2_2(df_processing):
    """
    2.2 - Report that lists the incidents in which the Service is "DESKTOP SUPPORT DSC LATAM" and the BU is different from "DSC".
    """
    df_2_2 = df_processing[(df_processing['Service'] == "DESKTOP SUPPORT DSC LATAM") & (df_processing['BU'] != "DSC")].sort_values(by=['Area', 'BU', 'Assignment_Group', 'Assigned'])
    df_2_2 = customising_order_of_columns(df_2_2, 'incident_type_impact_view')
    df_2_2.head(20).to_html('./src/output/html_element_2_2.html', index=False)


def report_html_element_2_3(df_processing):
    """
    2.3 - Report that lists the incidents in which the Service is "DESKTOP SUPPORT EXP LATAM" and the BU is different from "Express".
    """
    df_2_3 = df_processing[(df_processing['Service'] == "DESKTOP SUPPORT EXP LATAM") & (df_processing['BU'] != "Express")].sort_values(by=['Area', 'BU', 'Assignment_Group', 'Assigned'])
    df_2_3 = customising_order_of_columns(df_2_3, 'incident_type_impact_view')
    df_2_3.head(20).to_html('./src/output/html_element_2_3.html', index=False)


def report_html_element_3_0(df_processing):
    """
    3.0 - Heatmap for correlation analysis between Assigned Group and Impacted Service
    """
    cmap = LinearSegmentedColormap.from_list("custom_cmap",[ '#EBEBEB', '#DCDCDC', '#FFCC00'])

    grouped_data = df_processing.groupby(['Service', 'Assignment_Group']).size().unstack(fill_value=0)
    grouped_data = grouped_data.sort_values(by='Service', ascending=False)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(grouped_data, annot=True, cmap=cmap, center=10, linewidths=0.5, fmt=".0f")
    
    plt.title('Heatmap of Assigned Group VS Impacted Service').set_weight('bold')
    plt.xlabel('Assigned Group', labelpad=10)
    plt.ylabel('Impacted Service', labelpad=10).set_animated(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    ax = plt.gca()
    for tick in ax.get_xticklabels():
        tick.set_horizontalalignment('right')
        tick.set_x(tick.get_position()[0] - 1)
    
    plt.savefig('./src/output/html_element_3_0.png', dpi=150)


def report_html_element_3_1(df_processing):
    """
    3.1 - Report listing the number of incidents by Area, Business Unit and Assigned to
    """
    df_3_1 = df_processing.groupby(['Area', 'BU', 'Assigned']).agg(Number_Count=('Number', 'count')).reset_index()
    df_3_1.index = df_3_1.index + 1
    df_3_1 = df_3_1.sort_values(['Area', 'Assigned', 'BU'])
    df_3_1.head(len(df_processing)).to_html('./src/output/html_element_3_1.html')


def report_html_element_3_2(df_processing):
    """
     3.2 - Report that lists the number of incidents by Area, Business Unit and Assignment group.
    """
    df_3_2 = df_processing.groupby(['Area', 'BU', 'Assignment_Group']).agg(Number_Count=('Number', 'count')).reset_index()
    df_3_2.index = df_3_2.index + 1
    df_3_2 = df_3_2.sort_values(['Area', 'Assignment_Group', 'BU'])
    df_3_2.head(len(df_processing)).to_html('./src/output/html_element_3_2.html')


def report_html_element_4_0(df_processing):
    """
    4.0 - The Configuration Item field as ‘(empty)’, ‘NoRecord’ or other value. 
    """
    df_processing['CI_CMDB_Status'] = df_processing['CI_CMDB'].apply(lambda x: 'NoRecord' if x == 'NORECORD' else ('(empty)' if x == '(empty)' else 'Others'))
    config_item_counts = df_processing['CI_CMDB_Status'].value_counts()
    custom_colors = ['#FFCC00', '#AFAFAF', '#D40511'] 
    plt.figure(figsize=(8, 6))
    sns.barplot(x=config_item_counts.index, y=config_item_counts.values, hue=config_item_counts.index, palette=custom_colors, legend=False)
    plt.title('Distribution of "Configuration Item"', fontsize=16)
    plt.xlabel("Configuration Item Data's", fontsize=11)
    plt.ylabel('Count', fontsize=11)
    for i, value in enumerate(config_item_counts.values):
        plt.text(i, value + 1, str(value), ha='center', va='bottom')
    plt.tight_layout()
    plt.savefig('./src/output/html_element_4_0.png', dpi=150)


def report_html_element_4_1(df_processing):
    """
    4.1 Report listing the incidents in which the Configuration Item is null.
    """
    df_4_1 = df_processing[df_processing['CI_CMDB'] == '(empty)']
    df_4_1 = customising_order_of_columns(df_4_1, 'ci_view').sort_values(by=['Area', 'BU', 'Service', 'Assigned'])
    df_4_1.head(20).to_html('./src/output/html_element_4_1.html', index=False)


def report_html_element_4_2(df_processing):
    """
    4.2 Report listing the incidents in which the Configuration Item is null.
    """
    df_4_2 = df_processing[df_processing['CI_CMDB'] == 'NORECORD']
    df_4_2 = customising_order_of_columns(df_4_2, 'ci_view').sort_values(by=['Area', 'BU', 'Service', 'Assigned'])
    df_4_2.head(20).to_html('./src/output/html_element_4_2.html', index=False)


def report_html_element_5_0(df_processing):
    """
    5.0 - The field "Incident Status" as Pending Supplier and field Supplier as "Null" value.
    """
    # Filtrar os dados para os estados "Pending Supplier" e "Pending Customer"
    pending_supplier_df = df_processing[df_processing['Incident_State'] == "Pending Supplier"]
    pending_customer_df = df_processing[df_processing['Incident_State'] == "Pending Customer"]
    in_progress_df      = df_processing[df_processing['Incident_State'] == "In Progress"]

    # Contar a quantidade de incidentes por dia para cada estado
    pending_supplier_counts = pending_supplier_df.groupby(pending_supplier_df['Updated'].dt.date).size().sort_index()
    pending_customer_counts = pending_customer_df.groupby(pending_customer_df['Updated'].dt.date).size().sort_index()
    in_progress_counts      = in_progress_df.groupby(in_progress_df['Updated'].dt.date).size().sort_index()

    # Criar o gráfico de linhas
    plt.figure(figsize=(10, 6))
    plt.plot(pending_supplier_counts.index, pending_supplier_counts.values, label='Pending Supplier', marker='o', color='red')
    plt.plot(pending_customer_counts.index, pending_customer_counts.values, label='Pending Customer', marker='o', color='orange')
    plt.plot(in_progress_counts.index, in_progress_counts.values, label='In Progress', marker='o', color='green')
    plt.title('Incidents by Date of Updated (In Progress, Pending Supplier, Pending Customer)')
    plt.xlabel('Date')
    plt.ylabel('Count of Incidents')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)

    # Ajustar a escala do eixo y para ir de 1 em 1
    max_count = max(pending_supplier_counts.max(), pending_customer_counts.max(), in_progress_counts.max())
    plt.yticks(range(0, max_count + 1, 1))

    plt.tight_layout()
    plt.savefig('./src/output/html_element_5_0.png', dpi=150)


def report_html_element_5_1(df_processing):
    """
    5.1 - Report listing the incidents in which the State is "Pending Supplier" and the Supplier is (empty)
    """
    df_5_1 = df_processing[(df_processing['Incident_State'] == "Pending Supplier") & (df_processing['Supplier'] == "(empty)")].sort_values(by=['Area', 'BU', 'Service', 'CI_Model_ID'])
    df_5_1 = customising_order_of_columns(df_5_1, 'supplier_view')
    df_5_1.head(20).to_html('./src/output/html_element_5_1.html', index=False)


def report_html_element_5_2(df_processing):
    """
    5.2 - Report listing the incidents in which the State is "Pending Supplier" and the Supplier is not null
    """
    df_5_2 = df_processing[(df_processing['Incident_State'] == "Pending Supplier") & (df_processing['Supplier'] != "(empty)")].sort_values(by=['Area', 'BU', 'Service', 'Supplier', 'CI_Model_ID'])
    df_5_2 = customising_order_of_columns(df_5_2, 'supplier_view')
    df_5_2.head(20).to_html('./src/output/html_element_5_2.html', index=False)    


def report_html_element_6_0(df_processing):
    """
    6.0 - SLA Business Percentage by Impacted Area, Business Unit, and Assignment Group
    """
    # Extract the relevant columns
    df_filtered = df_processing[['SLA_Business_Percentage', 'Area', 'BU', 'Assignment_Group']]

    # Group by 'Impacted Area', 'Impacted Business Unit' and 'Assignment Group' and calculate the average 'Resolution SLA Percentage'
    df_grouped = df_filtered.groupby(['Area', 'BU', 'Assignment_Group']).mean().reset_index()

    # Plot the data as a bar chart
    plt.figure(figsize=(9, 6))
    df_grouped.pivot(index='Assignment_Group', columns=['Area', 'BU'], values='SLA_Business_Percentage').plot(kind='bar', ax=plt.gca())

    plt.title('Average SLA by Assignment Group, Impacted Area, and Business Unit')
    plt.xlabel('Assignment Group').set_animated(True)   # Set the x-axis label
    plt.ylabel('Resolution SLA Average in Percent (%)')
    plt.legend(title='Impacted Area / Impacted BU')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.ylim(0, 100)
    plt.tight_layout()

    # Show the graph
    #plt.show()
    plt.savefig('./src/output/html_element_6_0.png', dpi=150)    


def report_html_element_6_1(df_processing):
    """
    6.1 - Reporting describing the average SLA Business Percentage by Impacted Area, Business Unit and Assignment Group
    """
    # Group by 'Impacted Area', 'Impacted Business Unit' and 'Assignment Group' and calculate the average 'Resolution SLA Percentage'
    df_6_1 = df_processing.groupby(['Area', 'BU','Assignment_Group'])['SLA_Business_Percentage'].agg(
        Count='count',
        Mean='mean',
        Std='std',
        Min='min',
        q25=lambda x: x.quantile(0.25),
        Median='median',
        q75=lambda x: x.quantile(0.75),
        Max='max',
        Var='var',
        Mode=lambda x: x.mode().iloc[0] if not x.mode().empty else None
    )
    #df_6_1.describe(include=['object']).transpose().to_html('./src/output/html_element_6_1.html')
    df_6_1.to_html('./src/output/html_element_6_1.html')


def report_html_element_6_2(df_processing):
    """
    6.2 - Reporting describing the average SLA Business Percentage by Impacted Area, Business Unit and Service
    """
    # Group by 'Impacted Area', 'Impacted Business Unit' and 'Service' and calculate the average 'Resolution SLA Percentage'
    df_6_2 = df_processing.groupby(['Area', 'BU','Service'])['SLA_Business_Percentage'].agg(
        Count='count',
        Mean='mean',
        Std='std',
        Min='min',
        q25=lambda x: x.quantile(0.25),
        Median='median',
        q75=lambda x: x.quantile(0.75),
        Max='max',
        Var='var',
        Mode=lambda x: x.mode().iloc[0] if not x.mode().empty else None
    )
    #df_6_2.describe(include=['object']).transpose().to_html('./src/output/html_element_6_2.html')
    df_6_2.to_html('./src/output/html_element_6_2.html')
