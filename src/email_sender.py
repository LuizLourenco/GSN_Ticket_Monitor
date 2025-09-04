""" This module is responsible for sending the email with the analysis report as an attachment. """

import base64 # Import the base64 module
import datetime # Import the datetime3 module
from win32com.client import Dispatch # Import the Dispatch module


def send_mail_outlook():
    """ Send an email with the analysis report as an attachment. """
    try:
        outlook = Dispatch('Outlook.Application')
    except Exception:
        print("Outlook is not open. Opening Outlook...")
        subprocess.Popen(['outlook.exe'])
        time.sleep(5)
        outlook = Dispatch('Outlook.Application')

    outlook = Dispatch('Outlook.Application')
    mail = outlook.CreateItem(0)
    mail.Subject = '[TEST] Incident Management - Data Analysis Report - Pre-Closure'
    mail.To = 'br.its.eus@dhl.com'
    mail.CC = 'luiz.lourenco@dhl.com'

    # HTMLBody - Loading the HTML template as body mail. 
    with open('./src/template/Mail_Body_Model.html', 'r', encoding='utf-8') as file:
        html_body_model = file.read()

    # Carregar e codificar a imagem em base64 - DHL Group Banner ITS
    with open("./src/template/DHL_Group_banner_ITS.png", "rb") as image_file:
        var_DHL_Group_banner_ITS = base64.b64encode(image_file.read()).decode('utf-8')

    # Carregar e codificar a imagem em base64 - html_element_1_0
    with open("./src/output/html_element_1_0.png", "rb") as image_file:
        var_html_element_1_0 = base64.b64encode(image_file.read()).decode('utf-8')

    # Carregar o conteúdo do arquivo html_element_1_1.html 
    with open('./src/output/html_element_1_1.html', 'r', encoding='utf-8') as file:
        var_html_element_1_1 = file.read()

    # Carregar o conteúdo do arquivo html_element_1_2.html 
    with open('./src/output/html_element_1_2.html', 'r', encoding='utf-8') as file:
        var_html_element_1_2 = file.read()

    # Codificar a imagem em base64
    with open("./src/output/html_element_2_0.png", "rb") as image_file:
        var_html_element_2_0 = base64.b64encode(image_file.read()).decode('utf-8')

    # Carregar o conteúdo do arquivo html_element_2_1.html 
    with open('./src/output/html_element_2_1.html', 'r', encoding='utf-8') as file:
        var_html_element_2_1 = file.read()

    # Carregar o conteúdo do arquivo html_element_2_2.html 
    with open('./src/output/html_element_2_2.html', 'r', encoding='utf-8') as file:
        var_html_element_2_2 = file.read()

    # Carregar o conteúdo do arquivo html_element_2_3.html 
    with open('./src/output/html_element_2_3.html', 'r', encoding='utf-8') as file:
        var_html_element_2_3 = file.read()

    # Codificar a imagem em base64
    with open("./src/output/html_element_3_0.png", "rb") as image_file:
        var_html_element_3_0 = base64.b64encode(image_file.read()).decode('utf-8')

    # Carregar o conteúdo do arquivo html_element_3_1.html 
    with open('./src/output/html_element_3_1.html', 'r', encoding='utf-8') as file:
        var_html_element_3_1 = file.read()

    # Carregar o conteúdo do arquivo html_element_3_2.html 
    with open('./src/output/html_element_3_2.html', 'r', encoding='utf-8') as file:
        var_html_element_3_2 = file.read()

    # Codificar a imagem em base64
    with open("./src/output/html_element_4_0.png", "rb") as image_file:
        var_html_element_4_0 = base64.b64encode(image_file.read()).decode('utf-8')

    # Carregar o conteúdo do arquivo html_element_4_1.html 
    with open('./src/output/html_element_4_1.html', 'r', encoding='utf-8') as file:
        var_html_element_4_1 = file.read()

    # Carregar o conteúdo do arquivo html_element_4_2.html 
    with open('./src/output/html_element_4_2.html', 'r', encoding='utf-8') as file:
        var_html_element_4_2 = file.read()

    # Codificar a imagem em base64
    with open("./src/output/html_element_5_0.png", "rb") as image_file:
        var_html_element_5_0 = base64.b64encode(image_file.read()).decode('utf-8')

    # Carregar o conteúdo do arquivo html_element_5_1.html 
    with open('./src/output/html_element_5_1.html', 'r', encoding='utf-8') as file:
        var_html_element_5_1 = file.read()

    # Carregar o conteúdo do arquivo html_element_5_2.html 
    with open('./src/output/html_element_5_2.html', 'r', encoding='utf-8') as file:
        var_html_element_5_2 = file.read()

    # Codificar a imagem em base64
    with open("./src/output/html_element_6_0.png", "rb") as image_file:
        var_html_element_6_0 = base64.b64encode(image_file.read()).decode('utf-8')

    # Carregar o conteúdo do arquivo html_element_6_1.html 
    with open('./src/output/html_element_6_1.html', 'r', encoding='utf-8') as file:
        var_html_element_6_1 = file.read()

    # Carregar o conteúdo do arquivo html_element_6_2.html 
    with open('./src/output/html_element_6_2.html', 'r', encoding='utf-8') as file:
        var_html_element_6_2 = file.read()

    # Continue carregando e codificando os arquivos necessários...
    current_date_server = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    
    
    # Merge and insert the images and html table files into the HTML template 
    html_body_model = html_body_model.format(
        DHL_Group_banner_ITS=var_DHL_Group_banner_ITS,
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
    
    mail.HTMLBody = html_body_model

    mail.Send()
    print("Email sent successfully.")
