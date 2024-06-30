# Importa a biblioteca requests para realizar requisições HTTP
import requests
# Importa exceções específicas da biblioteca requests para tratamento de erros
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
# Importa a biblioteca de logging para registrar logs
import logging
# Importa datetime para manipulação de datas e horas
from datetime import datetime
# Importa load_dotenv para carregar variáveis de ambiente do arquivo .env
from dotenv import load_dotenv
# Importa a função get_cost do módulo uptime
from uptime import get_cost
# Importa o módulo os para interação com o sistema operacional
import os

# Configura o logging básico com nível de log INFO
logging.basicConfig(level=logging.INFO)

# Carrega as variáveis de ambiente
load_dotenv()
# Recupera as variáveis de ambiente relacionadas à API WHMCS
WHCMS_URL = os.getenv("WHMCS_API_URL")
WHCMS_IDENTIFIER = os.getenv("WHCMS_API_IDENTIFIER")
WHCMS_SECRET = os.getenv("WHCMS_API_SECRET")
WHCMS_KEY = os.getenv("WHCMS_API_KEY")
# Calcula o custo usando a função get_cost importada
cost = get_cost('node', 'vmid', 0.0001)

# Define os cabeçalhos para a requisição HTTP
headers = {
    'Accept': 'application/json',
}

# Define o payload (corpo) da requisição com os dados para a criação da fatura
payload = {
    'action': 'CreateInvoice',
    'identifier': WHCMS_IDENTIFIER,
    'secret': WHCMS_SECRET,
    'accesskey': WHCMS_KEY,
    'userid': 'client_user_id',
    'date': datetime.now().strftime('%Y-%m-%d'),  # Define a data atual como data da fatura
    'duedate': datetime.now().strftime('%Y-%m-%d'),  # Define a data atual como data de vencimento
    'paymentmethod': 'paypal',  # Define o método de pagamento
    'itemdescription1': 'Usage Charges',  # Descrição do item na fatura
    'itemamount1': cost,  # Valor do item baseado no custo calculado
    'itemtaxed1': '0',  # Indica que o item não é taxado
    'responsetype': 'json',  # Define o tipo de resposta esperada como JSON
}

# Tenta realizar a requisição POST para a API WHMCS
try:
    response = requests.post(WHCMS_URL, headers=headers, data=payload, timeout=10)
    response.raise_for_status()  # Levanta um erro HTTPError para respostas com erro
    try:
        invoice = response.json()  # Tenta decodificar a resposta JSON
        print(invoice)  # Imprime a fatura decodificada
    except ValueError:  # Inclui JSONDecodeError
        logging.error("Decoding JSON has failed")  # Registra um erro se a decodificação falhar
except HTTPError as http_err:
    logging.error(f'HTTP error occurred: {http_err}')  # Registra um erro se ocorrer um erro HTTP
except ConnectionError as conn_err:
    logging.error(f'Connection error occurred: {conn_err}')
except Timeout as timeout_err:
    logging.error(f'Request timed out: {timeout_err}')
except RequestException as err:
    logging.error(f'Unexpected error occurred: {err}')
