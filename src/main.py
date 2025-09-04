"""
IM_DataAnalysisReport

This script performs the following functions: data loading, cleaning,
preprocessing, and generation of reports using HTML elements from the dataset.
Additionally, it sends the generated report via Outlook email.

Functions:
    main(): Initializes the data processing and report generation workflow.
"""

# Import some sub functions from data_loader.py
from data_loader import load_dataset
from data_cleaner import cleanup_dataset
from data_preprocessor import pre_process_dataset
from column_renamer import rename_columns_name
from category_converter import convert_category_data_to_discrete_data


# Import some sub functions from report_generator.py
from report_generator import (
    report_html_element_1_0,
    report_html_element_1_1,
    report_html_element_1_2,
    report_html_element_2_0,
    report_html_element_2_1,
    report_html_element_2_2,
    report_html_element_2_3,
    report_html_element_3_0,
    report_html_element_3_1,
    report_html_element_3_2,
    report_html_element_4_0,
    report_html_element_4_1,
    report_html_element_4_2,
    report_html_element_5_0,
    report_html_element_5_1,
    report_html_element_5_2,
    report_html_element_6_0,
    report_html_element_6_1,
    report_html_element_6_2)
from email_sender import send_mail_outlook


# Main function
def main():
    """ Init all process. """
    df_inc_latam_eus_pre_close = load_dataset('./src/data/incident.csv')
    df_inc_latam_eus_pre_close = pre_process_dataset(
        df_inc_latam_eus_pre_close)
    df_inc_latam_eus_pre_close = cleanup_dataset(df_inc_latam_eus_pre_close)
    df_inc_latam_eus_pre_close = rename_columns_name(
        df_inc_latam_eus_pre_close)
    df_inc_latam_eus_pre_close = convert_category_data_to_discrete_data(
        df_inc_latam_eus_pre_close)
    report_html_element_1_0(df_inc_latam_eus_pre_close)
    report_html_element_1_1(df_inc_latam_eus_pre_close)
    report_html_element_1_2(df_inc_latam_eus_pre_close)
    report_html_element_2_0(df_inc_latam_eus_pre_close)
    report_html_element_2_1(df_inc_latam_eus_pre_close)
    report_html_element_2_2(df_inc_latam_eus_pre_close)
    report_html_element_2_3(df_inc_latam_eus_pre_close)
    report_html_element_3_0(df_inc_latam_eus_pre_close)
    report_html_element_3_1(df_inc_latam_eus_pre_close)
    report_html_element_3_2(df_inc_latam_eus_pre_close)
    report_html_element_4_0(df_inc_latam_eus_pre_close)
    report_html_element_4_1(df_inc_latam_eus_pre_close)
    report_html_element_4_2(df_inc_latam_eus_pre_close)
    report_html_element_5_0(df_inc_latam_eus_pre_close)
    report_html_element_5_1(df_inc_latam_eus_pre_close)
    report_html_element_5_2(df_inc_latam_eus_pre_close)
    report_html_element_6_0(df_inc_latam_eus_pre_close)
    report_html_element_6_1(df_inc_latam_eus_pre_close)
    report_html_element_6_2(df_inc_latam_eus_pre_close)
    # Continue chamando as funções de relatório...
    send_mail_outlook()
    print("End...")


if __name__ == "__main__":
    # Run the main function
    main()
