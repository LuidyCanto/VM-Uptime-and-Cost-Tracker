# VM Uptime and Cost Tracker

## Descrição
Este projeto permite calcular o tempo de atividade (uptime) de uma Máquina Virtual (VM) em um servidor Proxmox e determinar o custo associado ao uso da VM com base no tempo de atividade. Além disso, ele gera automaticamente uma fatura através da API WHMCS, integrando-se com sistemas de pagamento como PayPal.

## Funcionalidades
- **Cálculo de Uptime**: Utiliza a API do Proxmox para recuperar o tempo de atividade de uma VM.
- **Cálculo de Custo**: Baseia-se no tempo de atividade e em uma taxa definida por segundo para calcular o custo de uso da VM.
- **Integração com WHMCS**: Gera faturas automaticamente para clientes utilizando a API do WHMCS, com detalhes de cobrança e método de pagamento.
- **Tratamento de Erros**: Implementa tratamento para erros comuns como falha de conexão, tempo de requisição excedido, e problemas ao decodificar o JSON de retorno da API.

## Dependências
- **Bibliotecas Python**: 
  - `requests`: Para realizar requisições HTTP.
  - `dotenv`: Para carregar variáveis de ambiente de um arquivo `.env`.
  - `os`: Para interagir com o sistema operacional e acessar variáveis de ambiente.
  - `json`: Para manipulação de dados em formato JSON.

## Requisitos
- Python 3.x
- Variáveis de ambiente:
  - `TICKET`: Token de autenticação Proxmox.
  - `PROXMOX_API_URL`: URL da API do Proxmox.
  - `WHCMS_URL`: URL da API WHMCS.
  - `WHCMS_IDENTIFIER`, `WHCMS_SECRET`, `WHCMS_API_KEY`: Chaves e identificadores necessários para a autenticação na API WHMCS.
  
## Instruções de Instalação e Uso

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
2. Instale as dependências necessárias:
    ```bash
    pip install requests python-dotenv
3. Crie um arquivo .env na raiz do projeto com as seguintes variáveis:
    ```bash
    TICKET=<seu-ticket>
    PROXMOX_API_URL=<url-da-api-proxmox>
    WHCMS_URL=<url-da-api-whmcs>
    WHCMS_IDENTIFIER=<seu-identificador>
    WHCMS_SECRET=<seu-segredo>
    WHCMS_API_KEY=<sua-api-key>
4. Execute Script:
    ```bash 
    python main.py
## Contribuição

Se desejar contribuir com melhorias, faça um fork do projeto e envie um pull request com suas modificações.

