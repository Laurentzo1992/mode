from django import forms
from gestion.models import Client, Tenue, ModelTenue, Command, Livraison, Ville, Post, Couturier
from django.core.validators import RegexValidator


### FORM CONTRAT ###

class ClientForm(forms.ModelForm):
    

    nom = forms.CharField(
        label='Nom',
        widget=forms.TextInput(attrs={'placeholder': 'Nom du client'})
    )
    
    prenom = forms.CharField(
        label='Prenom',
        widget=forms.TextInput(attrs={'placeholder': 'Prenom du client'})
    )
    
    telephone = forms.CharField(
        label='telephone',
        widget=forms.TextInput(attrs={'placeholder': 'Telephone du client'})
    )
    
    
    avcar = forms.CharField(
        label='Carrure avant',
        widget=forms.TextInput(attrs={'placeholder': 'Carrure avant'})
    )
     
    arcar = forms.CharField(
        label='Carrure arrière',
        widget=forms.TextInput(attrs={'placeholder': 'Carrure arrière'})
    )


    class Meta:
        model = Client
        fields = '__all__'
        
        
        
class VilleForm(forms.ModelForm):
    
    libelle = forms.CharField(
        label='Ville',
        widget=forms.TextInput(attrs={'placeholder': 'Ville'})
    )
    
    class  Meta:
        model = Ville
        fields = '__all__'
        
        
        
        
class TenueForm(forms.ModelForm):
    
    libelle = forms.CharField(
        label='Nom de la tenue',
        widget=forms.TextInput(attrs={'placeholder': 'Nom de la tenue'})
    )
    
    price = forms.FloatField(
        label='Prix',
        widget=forms.TextInput(attrs={'placeholder': 'Prix'})
    )
    
    class  Meta:
        model = Tenue
        fields = '__all__'
        



class ModelTenueForm(forms.ModelForm):
    
    libelle = forms.CharField(
        label='Model',
        widget=forms.TextInput(attrs={'placeholder': 'Model'})
    )
    
    class  Meta:
        model = ModelTenue
        fields = '__all__'
        


class PostForm(forms.ModelForm):
    
    libelle = forms.CharField(
        label='Post',
        widget=forms.TextInput(attrs={'placeholder': 'Post'})
    )
    
    class  Meta:
        model = Post
        fields = '__all__'
        
        
        
class CouturierForm(forms.ModelForm):
    
    class  Meta:
        model = Couturier
        fields = '__all__'
        
        
        
        
class LivraisonForm(forms.ModelForm):
    date_livaison = forms.DateField(
        label='Date de livraison',
        widget=forms.TextInput(attrs={'type': 'date'})
    )
    class Meta:
        model = Livraison
        fields = '__all__'
        
        widgets = {
            'commande': forms.HiddenInput(),
        }
         