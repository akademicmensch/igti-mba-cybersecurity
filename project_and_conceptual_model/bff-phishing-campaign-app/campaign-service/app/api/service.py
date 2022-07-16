import os
import httpx

ORTOGONAL_ADVANCE_SERVICE_HOST_URL = 'http://localhost:8002/api/v1/ortogonal/'

def is_cast_present(cast_id: int):
    url = os.environ.get('ORTOGONAL_ADVANCE_SERVICE_HOST_URL') or ORTOGONAL_ADVANCE_SERVICE_HOST_URL
    r = httpx.get(f'{url}{cast_id}')
    return True if r.status_code == 200 else False