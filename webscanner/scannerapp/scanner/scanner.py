import requests,json,time

ZAP_URL = "http://zap:8080"


def start_scan(target_url):
    """Start an active scan on the target API using OWASP ZAP."""
    scan_url = f"{ZAP_URL}/JSON/ascan/action/scan/?url={target_url}"
    response = requests.get(scan_url)
    scan_id = response.json().get("scan")

    if scan_id:
        print(f"🔍 Scan started (ID: {scan_id})...")
        return scan_id
    else:
        print("❌ Failed to start scan")
        return None

def get_scan_status(scan_id):
    """Check the progress of the scan."""
    status_url = f"{ZAP_URL}/JSON/ascan/view/status/?scanId={scan_id}"
    response = requests.get(status_url)
    return response.json().get("status")

def get_scan_results(target_url):
    """Retrieve scan results."""
    results_url = f"{ZAP_URL}/JSON/core/view/alerts/?baseurl={target_url}"
    response = requests.get(results_url)
    alerts = response.json().get("alerts", [])

    with open("scan_results.json", "w") as file:
        json.dump(alerts, file, indent=4)

    return alerts
