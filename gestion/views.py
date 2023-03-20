from multiprocessing import context
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from urllib import request, response
from django.http import JsonResponse, HttpResponseRedirect
from  django.contrib import messages
from .forms import ClientForm, VilleForm, ModelTenueForm, TenueForm
from gestion.models import Client, Couturier, Tenue, ModelTenue, Ville, Command, Livraison

############################################################################

#Zone to manage Client


def client(request):
    clients = Client.objects.all()
    context = {"clients":clients}
    return render(request, 'gestion/client/client.html', context)



def add_client(request):
    if request.method=="POST":
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Client added successfully !")
            return redirect('client')
        else:
            return render(request, 'gestion/client/add.html', {"form":form})
    else:
        form = ClientForm()
        return render(request, 'gestion/client/add.html', {"form":form})
    
    
    

def edit_client(request, id):
    client = Client.objects.get(id=id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save(id)
            messages.success(request, "Modification effectué avec susccès!")
            return redirect('client')
    else:
        form = ClientForm(instance=client)
    return render(request, 'gestion/client/edit.html', {'form':form})


def delete_client(request, id):
    client = Client.objects.get(id = id)
    if request.method=='POST':
        client.delete()
        messages.success(request, 'Client supprimer avec susccès !')
        return redirect("client")
    return render(request, 'gestion/client/delete.html', {"client":client})

def print_client(request, id):
    client = Client.objects.get(id = id)
    return render(request, 'gestion/client/print.html', {"client":client})


######################################################################################

#Zone to manage Ville

def ville(request):
    villes = Ville.objects.all()
    context={"villes":villes}
    return render(request, 'gestion/ville/ville.html', context)



def add_ville(request):
    if request.method=="POST":
        form = VilleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ville ajouter avec succès !")
            return redirect('ville')
        else:
            return render(request, 'gestion/ville/add.html', {"form":form})
    else:
        form = VilleForm()
        return render(request, 'gestion/ville/add.html', {"form":form})



def edit_ville(request, id):
    ville = Ville.objects.get(id=id)
    if request.method == 'POST':
        form = VilleForm(request.POST, instance=ville)
        if form.is_valid():
            form.save(id)
            messages.success(request, f"Ville {ville} modifiéé avec succès !")
            return redirect('ville')
    else:
        form = VilleForm(instance=ville)
    return render(request, 'gestion/ville/edit.html', {'form':form})



def delete_ville(request, id):
    ville = Ville.objects.get(id = id)
    if request.method=='POST':
        ville.delete()
        messages.success(request, f'Ville {ville} supprimer avec susccès !')
        return redirect("ville")
    return render(request, 'gestion/ville/delete.html', {"ville":ville})


 ########################################################################################
 
 #Zone to manage Tenue


def tenue(request):
    tenues = Tenue.objects.all()
    context={"tenues":tenues}
    return render(request, 'gestion/tenue/tenue.html', context)



def add_tenue(request):
    if request.method=="POST":
        form = TenueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Tenue ajouter avec succès !")
            return redirect('tenue')
        else:
            return render(request, 'gestion/tenue/add.html', {"form":form})
    else:
        form = TenueForm()
        return render(request, 'gestion/tenue/add.html', {"form":form})



def edit_tenue(request, id):
    tenue = Tenue.objects.get(id=id)
    if request.method == 'POST':
        form = TenueForm(request.POST, instance=tenue)
        if form.is_valid():
            form.save(id)
            messages.success(request, "modifiéé avec succès !")
            return redirect('tenue')
    else:
        form = TenueForm(instance=tenue)
    return render(request, 'gestion/tenue/edit.html', {'form':form})



def delete_tenue(request, id):
    tenue = Tenue.objects.get(id = id)
    if request.method=='POST':
        tenue.delete()
        messages.success(request, 'Tenue supprimer avec susccès !')
        return redirect("tenue")
    return render(request, 'gestion/tenue/delete.html', {"tenue":tenue})

##################################################################################


#Zone to manage Model Tenue

def modelle(request):
    modelles = ModelTenue.objects.all()
    context={"modelles":modelles}
    return render(request, 'gestion/modelle/modelle.html', context)



def add_modelle(request):
    if request.method=="POST":
        form = ModelTenueForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Modelle ajouter avec succès !")
            return redirect('modelle')
        else:
            return render(request, 'gestion/modelle/add.html', {"form":form})
    else:
        form = ModelTenueForm()
        return render(request, 'gestion/modelle/add.html', {"form":form})



def edit_modelle(request, id):
    modelle = ModelTenue.objects.get(id=id)
    if request.method == 'POST':
        form = ModelTenueForm(request.POST, instance=modelle)
        if form.is_valid():
            form.save(id)
            messages.success(request, f"Modlelle {modelle} modifiéé avec succès !")
            return redirect('modelle')
    else:
        form = ModelTenueForm(instance=modelle)
    return render(request, 'gestion/modelle/edit.html', {'form':form})



def delete_modelle(request, id):
    modelle = ModelTenue.objects.get(id = id)
    if request.method=='POST':
        modelle.delete()
        messages.success(request, f'Model {modelle} supprimer avec susccès !')
        return redirect("modelle")
    return render(request, 'gestion/modelle/delete.html', {"modelle":modelle})












