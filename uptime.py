# Importa as bibliotecas necessárias para realizar requisições HTTP, manipular JSON, carregar variáveis de ambiente e interagir com o sistema operacional
import requests
import json
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente definidas no arquivo .env
load_dotenv()
TICKET = os.getenv("TICKET")  # Recupera a variável de ambiente TICKET
PROXMOX_URL = os.getenv("PROXMOX_API_URL")  # Recupera a variável de ambiente PROXMOX_API_URL

# Define uma função para obter o tempo de atividade (uptime) de uma VM
def get_vm_uptime(node, vmid):
    url = f"{PROXMOX_URL}/nodes/{node}/qemu/{vmid}/status/uptime"  # Constrói a URL para a API
    headers = {'Cookie': f'PVEAuthCookie={TICKET}'}  # Define o cookie de autenticação no cabeçalho da requisição
    response = requests.get(url, headers=headers, verify=False)  # Realiza a requisição GET, desabilitando a verificação SSL
    data = response.json()  # Converte a resposta JSON em um dicionário Python
    uptime_seconds = data['data']['uptime']  # Extrai o tempo de atividade em segundos da resposta
    return uptime_seconds  # Retorna o tempo de atividade em segundos

# Define uma função para calcular o custo com base no tempo de atividade e na taxa por segundo
def calculate_cost(uptime_seconds, rate_per_second):
    return uptime_seconds * rate_per_second  # Retorna o produto do tempo de atividade pela taxa como o custo

# Define uma função para obter o custo de uma VM com base no seu nó, vmid e taxa por segundo
def get_cost(node, vmid, rate_per_second):
    uptime_seconds = get_vm_uptime(node, vmid)  # Obtém o tempo de atividade em segundos para a VM
    return calculate_cost(uptime_seconds, rate_per_second)  # Calcula e retorna o custo

# Define o nó e o vmid da VM para a qual deseja calcular o custo
node = "your_node_name"
vmid = "your_vmid"

# Obtém o tempo de atividade da VM
uptime_seconds = get_vm_uptime(node, vmid)

# Calcula o custo
cost = calculate_cost(uptime_seconds, rate_per_second)



