import requests
from datetime import datetime
from dotenv import load_dotenv
from uptime import get_cost
import os

load_dotenv()
WHCMS_URL = os.getenv("WHMCS_API_URL")
WHCMS_IDENTIFIER = os.getenv("WHCMS_API_IDENTIFIER")
WHCMS_SECRET = os.getenv("WHCMS_API_SECRET")
WHCMS_KEY = os.getenv("WHCMS_API_KEY")
cost = get_cost('node', 'vmid', 0.0001)

headers = {
    'Accept': 'application/json',
}

payload = {
    'action': 'CreateInvoice',
    'identifier': WHCMS_IDENTIFIER,
    'secret': WHCMS_SECRET,
    'accesskey': WHCMS_KEY,
    'userid': 'client_user_id',
    'date': datetime.now().strftime('%Y-%m-%d'),
    'duedate': datetime.now().strftime('%Y-%m-%d'),
    'paymentmethod': 'paypal',
    'itemdescription1': 'Usage Charges',
    'itemamount1': cost,
    'itemtaxed1': '0',
    'responsetype': 'json',
}

response = requests.post(WHCMS_URL, headers=headers, data=payload)
invoice = response.json()
print(invoice)
