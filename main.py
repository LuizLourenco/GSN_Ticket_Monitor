# ./main.py
"""
Este módulo contém funções para análise de dados de incidentes em andamento.

Project: GSN_Ticket_Monitor
Department: End User Service from ITS Brazil
Author: luiz.lourenco@dhl.com
Creation Date: Jun-3-2024
Version: 1.0.0
Description: GSN_Ticket_Monitor is a project that monitors the quality of tickets filled out on Global ServiceNow. 
------------------------------------
Copyright (c) DHL Group. All rights reserved.
Licensed under the MIT License.
See the License file in the project root for license information.

"""

# Importando os algoritmos
from . import im_qa_eda_model 


def main():
    """
    Função principal do módulo.
    """
    # Caminho para os dados de entrada
    input_data_path = "./input_data/"
    
    # Caminho para os dados de saída
    output_data_path = "./output_data/"
    
    # Executando o primeiro algoritmo
    print("Executando o algoritmo 1...")
    im_qa_eda_model(input_data_path, output_data_path)
    # im_qa_eda_model()
    
    print("Processamento concluído.")


if __name__ == "__main__":
    main()
