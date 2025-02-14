from django import forms


# Create a form class
class ScanForm(forms.Form):
    target_url = forms.URLField(label="Enter API URL", required=True) # Create a URL field
