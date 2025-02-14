from django.shortcuts import render
from django.http import JsonResponse
from .forms import ScanForm
from scanner.scanner import Start_Scanning, get_scan_status, get_result

# Create your views here.

def home(request):
    if request == 'POST': 
        form = ScanForm(request.POST) # Create a form instance and populate it with data from the request
        if form.is_valid():
            target_url = form.cleaned_data['target_url'] # Get the target URL from the form
            scan_id = Start_Scanning(target_url) # Start the scanning process

            if scan_id:
                return render(request, "index.html", {"scan_id": scan_id, "target_url": target_url}) # Render the index.html template with the scan ID and target URL
            else:
                return render(request, "index.html", {"error": "Failed to start scan!"})
    else:
        form = ScanForm() # Create an empty form
    return render(request, "index.html", {"form": form}) # Render the index.html template with the form



def scan_status(request, scan_id):
    """Check scan progress."""
    status = get_scan_status(scan_id)
    return JsonResponse({"status": status})

def scan_results(request):
    """Fetch scan results."""
    target_url = request.GET.get("target_url")
    results = get_result(target_url)
    return JsonResponse({"alerts": results})