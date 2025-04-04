from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

API_KEY = "mysecurekey123"  # Change this for security
API_KEY_NAME = "api-key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

def get_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key
