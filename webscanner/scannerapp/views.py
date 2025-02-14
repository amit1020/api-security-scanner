from django.shortcuts import render
from django.http import JsonResponse
from scannerapp.scanner.scanner import start_scan,get_scan_status,get_scan_results

try:
    from .forms import ScanForm
except ModuleNotFoundError:
    print("Warning: scannerapp/forms.py is missing!")

# Create your views here.

def home(request):
    if request.method == 'POST':  # ✅ Fixed POST check
        form = ScanForm(request.POST)  # Create a form instance
        if form.is_valid():
            target_url = form.cleaned_data['target_url']  # Get target URL
            scan_id = start_scan(target_url)  # Start scan

            if scan_id:
                return render(request, "index.html", {"scan_id": scan_id, "target_url": target_url})  # ✅ Pass scan ID
            else:
                return render(request, "index.html", {"error": "Failed to start scan!"})  # Show error

    else:
        form = ScanForm()  # Create an empty form

    return render(request, "index.html", {"form": form})  # Render template


def scan_status(request, scan_id):
    status = get_scan_status(scan_id)
    return JsonResponse({"status": status})


def scan_results(request):
    target_url = request.GET.get("target_url")  # Get target URL
    results = get_scan_results(target_url)  # Fetch scan results
    return JsonResponse({"alerts": results})  