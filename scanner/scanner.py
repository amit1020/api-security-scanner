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
    
   
# Get the status of the scanning process 
def Get_Scan_Status(ScanID):
    status_url = f"{OWASP_ZAP_URL}/JSON/ascan/view/status/?scanId={ScanID}"
    response = requests.get(status_url)
    if response.status_code == 200:
        return response.json().get('status')
    
    
def get_result(target_url):
    results_url = f"{OWASP_ZAP_URL}/JSON/core/view/alerts/?baseurl={target_url}"
    response = requests.get(results_url)
    alerts = response.json().get("alerts", [])
    # Save the results to a JSON file  
    with open("results.json", "w") as fp:
        json.dump(alerts, fp, indent=4)
        
    return alerts