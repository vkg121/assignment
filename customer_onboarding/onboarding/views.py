
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomerForm, DocumentUploadForm
from .aws import extract_text_from_document
from .models import *
import json

@login_required
def create_customer(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        document_form = DocumentUploadForm(request.POST, request.FILES)
        if customer_form.is_valid() and document_form.is_valid():
            customer = customer_form.save(commit=False)
            customer.created_by = request.user
            customer.save()
            document = document_form.save(commit=False)
            document.customer = customer
            document.save()
            extracted_data = extract_text_from_document(document.attached_file.path)
            document.extracted_json = json.dumps(extracted_data)
            document.save()
            return redirect('/list_customers/')
    else:
        customer_form = CustomerForm()
        document_form = DocumentUploadForm()
    return render(request, 'create_customer.html', locals())

def list_customers(request):
    customers = CustomerModel.objects.filter(created_by=request.user)
    return render(request, "list_customer.html",locals())
