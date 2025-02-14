import os,dotenv 

dotenv.load_dotenv()


# OWASP ZAP URL running on Docker container
OWASP_ZAP_URL = 'http://localhost:8080'

# OWASP ZAP API Key - defined by the user
DEFAULT_TARGET_URL = os.getenv('MY_API_KEY')