from django.shortcuts import render
from .models import Client
from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect , get_object_or_404
from django.contrib import messages
from django.http import JsonResponse

from .forms import AddClientForm


@login_required
def client_list(request,):
        client = Client.objects.filter(created_by=request.user)
        return render(request, 'client/show_clients.html', {
        'clients': client
    })

@login_required
def update_priority_client_bulk(request):
    if request.method == "POST":
        client_ids = request.POST.getlist('client_ids[]')
        priorities = request.POST.getlist('priorities[]')
        
        for client_id, priority in zip(client_ids, priorities):
            client = get_object_or_404(Client, pk=client_id)
            client.priority = priority
            client.save()
        
        messages.success(request, "Priorities updated successfully!")
        return redirect('client_list')
        
    return JsonResponse({'success': False})


@login_required
def add_client(request):
    if request.method == "POST":
        form = AddClientForm(request.POST)
        if form.is_valid():
            client=form.save(commit=False)
            client.created_by=request.user
            client.save()
            messages.success(request, "client added successfully!")
            return redirect('/dashboard/')
    else:
        form=AddClientForm()
    return render(request, 'client/add_client.html',{
        'form': form,
    })
    

@login_required
def delete_client(request, pk):
    client = get_object_or_404(Client , created_by=request.user , pk=pk)
    client.delete()
    messages.success(request, "client deleted successfully!")
    return redirect('client_list')

@login_required
def client_details(request, pk):
    client =get_object_or_404(Client , created_by=request.user , pk=pk)
    return render(request, 'client/client_details.html', {'client': client})

@login_required
def client_edit(request , pk):
    client = get_object_or_404(Client , created_by=request.user , pk=pk)
    
    if request.method == "POST":
        form = AddClientForm(request.POST, instance=client)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, "client updated successfully!")
            
            return redirect('client_list')
    else:
        form= AddClientForm(instance=client )
        
    return render(request, 'client/client_edit.html',{
        'form': form,
    })
        
from django.http import JsonResponse