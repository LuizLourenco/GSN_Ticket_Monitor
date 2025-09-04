import unittest
from src.data_loader import load_dataset
from src.data_cleaner import cleanup_dataset
from src.data_preprocessor import pre_process_dataset
from src.column_renamer import rename_columns_name
from src.column_formatter import customising_order_of_columns
from src.category_converter import convert_category_data_to_discrete_data
from src.report_generator import (
    report_html_element_1_0,
    # Continue importando as funções de relatório...
)
from src.email_sender import send_mail_outlook

class TestMain(unittest.TestCase):
    def test_load_dataset(self):
        data = load_dataset()
        self.assertIsNotNone(data)

    # Continue adicionando testes para as outras funções...

if __name__ == "__main__":
    unittest.main()