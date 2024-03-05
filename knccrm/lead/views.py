from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from django.contrib import messages

from .forms import AddLeadForm
from .models import Lead

from client.models import Client

@login_required
def lead(request):
    return render(request, 'lead/lead.html')

@login_required
def add_lead(request):
    if request.method == "POST":
        form = AddLeadForm(request.POST)
        if form.is_valid():
            lead=form.save(commit=False)
            lead.created_by=request.user
            lead.save()
            messages.success(request, "Lead added successfully!")
            return redirect('/dashboard/')
    else:
        form=AddLeadForm()
    return render(request, 'lead/add_lead.html',{
        'form': form,
    })
    
@login_required
def show_lead(request):
    lead = Lead.objects.filter(created_by=request.user, converted_to_clients=False)
    return render(request, 'lead/show_lead.html', {
        'leads': lead
    })

    
@login_required
def lead_details(request, pk):
    lead =get_object_or_404(Lead , created_by=request.user , pk=pk)
    return render(request, 'lead/lead_details.html', {'lead': lead})

@login_required
def delete_lead(request, pk):
    lead = get_object_or_404(Lead , created_by=request.user , pk=pk)
    lead.delete()
    messages.success(request, "Lead deleted successfully!")
    return redirect('show_lead')

@login_required
def lead_edit(request , pk):
    lead = get_object_or_404(Lead , created_by=request.user , pk=pk)
    
    if request.method == "POST":
        form = AddLeadForm(request.POST, instance=lead)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, "Lead updated successfully!")
            
            return redirect('show_lead')
    else:
        form= AddLeadForm(instance=lead )
        
    return render(request, 'lead/lead_edit.html',{
        'form': form,
    })
        
from django.http import JsonResponse

@login_required
def update_status_priority_bulk(request):
    if request.method == "POST":
        lead_ids = request.POST.getlist('lead_ids[]')
        priorities = request.POST.getlist('priorities[]')
        statuses = request.POST.getlist('statuses[]')
        
        for lead_id, priority, status in zip(lead_ids, priorities, statuses):
            lead = get_object_or_404(Lead, created_by=request.user, pk=lead_id)
            lead.priority = priority
            lead.status = status
            lead.save()
        messages.success(request, "Updated successfully!")
        return redirect('show_lead')
        
    return JsonResponse({'success': False})


@login_required
def convert_to_client(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    
    client = Client.objects.create(
        name=lead.name,
        email=lead.email,
        phone_number=lead.phone_number,
        company=lead.company,
        notes=lead.notes,
        created_by=request.user,
    )
    
    lead.converted_to_clients = True
    lead.save()
    
    messages.success(request, "Lead converted to client successfully!")
    
    return redirect('show_lead')

