import requests,json,time
from scanner.config import OWASP_ZAP_URL




def Start_Scanning(target_url):
    try:
        # Start the scanning process
        scan_url = f"{OWASP_ZAP_URL}/JSON/ascan/action/scan/?url={target_url}" # URL to start scanning
        response = requests.get(scan_url)
        
        # Check if the response is successful
        if response.status_code == 200:
            ScanID = response.json().get('scan')
            if ScanID:
                return ScanID 
            
            else:
                print("Error: Unable to start scanning process")
                return None
    except Exception as e:
        print(f"Error: {e}")
        return None 
    
    
