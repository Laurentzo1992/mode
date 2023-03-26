from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from urllib import request, response
from django.http import JsonResponse, HttpResponseRedirect
from  django.contrib import messages
from .forms import ClientForm, LivraisonForm, VilleForm, ModelTenueForm, TenueForm, PostForm, CouturierForm
from gestion.models import Client, Couturier, LigneCommande, Tenue, ModelTenue, Ville, Command, Livraison, Post
from django.contrib.auth.decorators import login_required, permission_required
from  django.views.decorators.cache import cache_control 
from datetime import date
from django.db import transaction, models
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


##################################################################################


#Zone to manage Post

def post(request):
    posts = Post.objects.all()
    context={"posts":posts}
    return render(request, 'gestion/post/post.html', context)



def add_post(request):
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Post ajouter avec succès !")
            return redirect('post')
        else:
            return render(request, 'gestion/post/add_post.html', {"form":form})
    else:
        form = PostForm()
        return render(request, 'gestion/post/add_post.html', {"form":form})
    
    
    

def edit_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save(id)
            messages.success(request, f"Post {post} modifiéé avec succès !")
            return redirect('post')
    else:
        form = PostForm(instance=post)
    return render(request, 'gestion/post/edit_post.html', {'form':form})




def delete_post(request, id):
    post = Post.objects.get(id = id)
    if request.method=='POST':
        post.delete()
        messages.success(request, f'Post {post} supprimer avec susccès !')
        return redirect("post")
    return render(request, 'gestion/post/delete_post.html', {"post":post})




##################################################################################


#Zone to manage Personnel

def personnel(request):
    couturiers = Couturier.objects.all()
    context={"couturiers":couturiers}
    return render(request, 'gestion/personnel/personnel.html', context)



def add_personnel(request):
    if request.method=="POST":
        form = CouturierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Personnel ajouter avec succès !")
            return redirect('personnel')
        else:
            return render(request, 'gestion/personnel/add.html', {"form":form})
    else:
        form = CouturierForm()
        return render(request, 'gestion/personnel/add.html', {"form":form})
    
    
    

def edit_personnel(request, id):
    personnel = Couturier.objects.get(id=id)
    if request.method == 'POST':
        form = CouturierForm(request.POST, instance=personnel)
        if form.is_valid():
            form.save(id)
            messages.success(request, f"Personnel {personnel} modifiéé avec succès !")
            return redirect('personnel')
    else:
        form = CouturierForm(instance=personnel)
    return render(request, 'gestion/personnel/edit.html', {'form':form})




def delete_personnel(request, id):
    personnel = Couturier.objects.get(id = id)
    if request.method=='POST':
        personnel.delete()
        messages.success(request, f'Personnel {personnel} supprimer avec susccès !')
        return redirect("personnel")
    return render(request, 'gestion/personnel/delete.html', {"personnel":personnel})




############################################################################

#Zone to manage Order


def commande(request):
    commandes=Command.objects.all()
    nbr_commande = commandes.count()
    context={"nbr_commande":nbr_commande, "commandes":commandes}
    return render(request, 'gestion/commande/commande.html', context)



#@login_required 
#@permission_required('gestion.add_commande', login_url='acces_denied')
#@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add_commande(request):
    if request.method == 'POST':
        supplier_id = request.POST.get('client')
        supplier = Client.objects.get(pk=supplier_id)
        adresse_livraison = request.POST.get('adresse_livraison')
        date_commande = request.POST.get('date_commande')
        num_commande = request.POST.get('num_commande')
        couturier_id = request.POST.get('couturier')
        couturier = Couturier.objects.get(pk=couturier_id)
        commande = Command.objects.create(client=supplier,
                                            date_commande=date_commande,
                                            adresse_livraison=adresse_livraison,
                                            num_commande=num_commande,
                                            couturier=couturier
                                            )
        selected_products = request.POST.getlist('articles')
        number = 0
        with transaction.atomic():
            for article_id in selected_products:
                number += 1
                quantity = int(request.POST.get(f'quantity-{number}'))
                article = Tenue.objects.get(id=article_id)
                # Vérifiez si la quantité demandée est disponible
                # if article.stock >= quantity:
                #     article.stock = models.F('stock') - quantity
                article.save()

                LigneCommande.objects.create(commande=commande,
                                                     article=article,
                                                     quantite=quantity)

                # else:
                        # Si la quantité n'est pas disponible, annulez la commande et affichez un message d'erreur
                    # commande.delete()
                    # messages.error(request, f"La quantité demandée pour '{article.name}' n'est pas disponible.")

                #return redirect('commande')

            Livraison.objects.create(commande=commande,
                                      num_livraison=commande.num_commande,
                                      status=False,
                                      )

        messages.success(request, 'Votre commande a été passée avec succès!')
        return redirect('commande')

    else:
        articles = Tenue.objects.all()
        suppliers = Client.objects.all()
        couturiers = Couturier.objects.all()
        prefixe = 'CMD-'
        idc = f'{Command.objects.count()+1:05d}'
        suffixe = date.today()
        sep = '-'
        num_commande = prefixe + idc + sep  + str(suffixe)
        context = {'articles': articles, "suppliers":suppliers, "couturiers":couturiers, "num_commande":num_commande}
        return render(request, 'gestion/commande/add.html', context)


def edit_commande(request, commande_id):
    commande = Command.objects.get(pk=commande_id)
    if request.method == 'POST':
        supplier_id = request.POST.get('client')
        supplier = Client.objects.get(id=supplier_id)
        adresse_livraison = request.POST.get('adresse_livraison')
        date_commande = request.POST.get('date_commande')
        num_commande = request.POST.get('num_commande')
        couturier_id = request.POST.get('couturier')
        couturier = Couturier.objects.get(id=couturier_id)
        with transaction.atomic():
            # Supprimer les anciennes lignes de commande
            LigneCommande.objects.filter(commande=commande).delete()
            selected_products = request.POST.getlist('articles')
            number = 0
            for article_id in selected_products:
                number += 1
                quantity = request.POST.get(f'quantity-{number}')
                quantity = int(quantity)
                article = Tenue.objects.get(id=article_id)
                # Vérifiez si la quantité demandée est disponible
                # if article.stock >= quantity:
                #     article.stock = models.F('stock') - quantity
                article.save()

                LigneCommande.objects.create(commande=commande,
                                                     article=article,
                                                     quantite=quantity)

                # else:
                        # Si la quantité n'est pas disponible, annulez la commande et affichez un message d'erreur
                    # commande.delete()
                    # messages.error(request, f"La quantité demandée pour '{article.name}' n'est pas disponible.")

            # Mettre à jour les informations de la commande
            commande.client = supplier
            commande.adresse_livraison = adresse_livraison
            commande.date_commande = date_commande
            commande.num_commande = num_commande
            commande.couturier = couturier
            commande.save()

            # Créer une nouvelle livraison pour la commande mise à jour
            Livraison.objects.create(commande=commande,
                                      num_livraison=commande.num_commande,
                                      status=False,
                                      )

        messages.success(request, 'Votre commande a été modifiée avec succès!')
        return redirect('commande')

    else:
        articles = Tenue.objects.all()
        suppliers = Client.objects.all()
        couturiers = Couturier.objects.all()
        commandes = LigneCommande.objects.filter(commande=commande)
        context = {"commandes":commandes, 'articles': articles, "suppliers":suppliers, "couturiers":couturiers, "commande":commande}
        return render(request, 'gestion/commande/edit.html', context)

    
  

def delete_commande(request, id):
    com_id = Command.objects.get(id=id)
    commandes=LigneCommande.objects.filter(commande=com_id)
    if request.method=='POST':
        com_id.delete()
        for commande in commandes:
            commande.delete()
        messages.success(request, 'supresions effectué avec succès')
        return redirect('commande')
    return render(request, 'gestion/commande/delete.html', {"com_id":com_id, "commandes":commandes})


def valide_livraison(request, id):
    livraison = get_object_or_404(Livraison, id=id)
    commande = livraison.commande
    form = LivraisonForm(request.POST or None, instance=livraison)
    if form.is_valid():
        livraison = form.save(commit=False)
        commande.save()
        livraison.status = True
        livraison.save()
        messages.success(request, 'commande livréé avec succès!')
        return redirect('livraison')
    return render(request, 'gestion/livraison/livraison.html', {'form': form, 'livraison': livraison})


def items_commande(request, id):
    com_id = Command.objects.get(id=id)
    commandes=LigneCommande.objects.filter(commande_id=com_id)
    return render(request, 'gestion/commande/items_commande.html', {"com_id":com_id, "commandes":commandes})



def bon_livraison(request, id):
    com_id = Livraison.objects.get(id=id)
    commandes=LigneCommande.objects.filter(commande_id=com_id)
    return render(request, 'gestion/commande/bon_livraison.html', {"com_id":com_id, "commandes":commandes})


def livraison(request):
    livraisons = Livraison.objects.all().filter(status=False).order_by('-id')
    nbr_livraison = livraisons.count()
    paginator = Paginator(livraisons, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"nbr_livraison":nbr_livraison, "page_obj":page_obj}
    return render(request, 'gestion/livraison/livraison.html', context)




