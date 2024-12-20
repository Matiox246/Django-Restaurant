from django.shortcuts import render, redirect
from django.contrib import messages
from .fomrs import ContactForm

def contact_form(request):
    contact_form = ContactForm()
    
    if request.method == "POST":
        print("post")
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            
        # No need to reinitialize contact_form here; you can reuse it
        # Context remains the same
    context = {
        "contact_form": contact_form
    }
    # Render the template for both GET and POST requests
    return render(request, "contact/contact_new.html", context)