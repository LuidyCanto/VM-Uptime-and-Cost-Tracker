#bibliotecas para, respectivamente: HHTP requests, uso do formato json, variaveis de ambiente, e acesso ao sistema operacional
import requests
import json
from dotenv import load_dotenv
import os

#Carrega as variaves de ambientes contidas no arquivo .env
load_dotenv()
TICKET = os.getenv("TICKET")
PROXMOX_URL = os.getenv("PROXMOX_API_URL")

#funcao para pegar o uptime da VM
def get_vm_uptime(node, vmid):
    url = f"{PROXMOX_URL}/nodes/{node}/qemu/{vmid}/status/uptime"
    headers = {'Cookie': f'PVEAuthCookie={TICKET}'}
    response = requests.get(url, headers=headers, verify=False)
    data = response.json()
    uptime_seconds = data['data']['uptime']
    return uptime_seconds

#funcao para calcular o custo 
def calculate_cost(uptime_seconds, rate_per_second):
    return uptime_seconds * rate_per_second

def get_cost(node, vmid, rate_per_second):
    uptime_seconds = get_vm_uptime(node, vmid)
    return calculate_cost(uptime_seconds, rate_per_second)
#informe o node e o vmid da VM que deseja calcular o custo
node = "your_node_name"
vmid = "your_vmid"

#informe a taxa de custo por segundo    
rate_per_second = 0.0001  

#Pega o uptime da VM
uptime_seconds = get_vm_uptime(node, vmid)

#Calcula o custo
cost = calculate_cost(uptime_seconds, rate_per_second)


