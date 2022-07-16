import os
from gophish import Gophish

api_key = 'API_KEY'
api = Gophish(api_key, host='http://admin_server', verify=False)