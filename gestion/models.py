from tabnanny import verbose
from django.db import models

# Model Model de tenue   
class ModelTenue(models.Model):
    libelle = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.libelle
    
    
# Model Tenue     
class Tenue(models.Model):
    libelle = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    model = models.ForeignKey(ModelTenue, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='model_photo/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.libelle
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
 
# Model Ville     
class Ville(models.Model):
    libelle = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.libelle
    
# Model Client   
class Client(models.Model):
    nom = models.CharField(max_length=200, null=True)
    prenom = models.CharField(max_length=200, null=True)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Ville")
    telephone = models.CharField(max_length=200, null=True, blank=True, verbose_name="Téléphone")
    bas = models.CharField(max_length=20, null=True, blank=True)
    longpan = models.CharField(max_length=20, null=True, blank=True, verbose_name="Longueur pantalon")
    poignet = models.CharField(max_length=20, null=True, blank=True)
    longjupe = models.CharField(max_length=20, null=True, blank=True, verbose_name="Longueur jupe")
    genou = models.CharField(max_length=20, null=True, blank=True)
    cuiss = models.CharField(max_length=20, null=True, blank=True, verbose_name="Cuisse")
    bassin = models.CharField(max_length=20, null=True, blank=True)
    ceinture = models.CharField(max_length=20, null=True, blank=True)
    longchem = models.CharField(max_length=20, null=True, blank=True, verbose_name="Longueur Chemise")
    frappe = models.CharField(max_length=20, null=True, blank=True)
    longrobe = models.CharField(max_length=20, null=True, blank=True, verbose_name="Longueur Robe")
    longcami = models.CharField(max_length=20, null=True, blank=True, verbose_name="Longueur Camisole")
    pince = models.CharField(max_length=20, null=True, blank=True)
    tourtaille = models.CharField(max_length=20, null=True, blank=True, verbose_name="Tour de taille")
    coole = models.CharField(max_length=20, null=True, blank=True)
    longtaille = models.CharField(max_length=20, null=True, blank=True)
    tourmanch = models.CharField(max_length=20, null=True,blank=True, verbose_name="Tour de manche")
    longmanch = models.CharField(max_length=20, null=True, blank=True,verbose_name="Longueur manche")
    poitrine = models.CharField(max_length=20, null=True, blank=True)
    dos = models.CharField(max_length=20, null=True, blank=True)
    epaul = models.CharField(max_length=20, null=True,blank=True, verbose_name="Epaule")
    avcar = models.CharField(max_length=20, null=True, blank=True)
    arcar = models.CharField(max_length=20, null=True, blank=True)
    fichier = models.FileField(upload_to='uploads_files/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nom
    
    @property
    def fileURL(self):
        try:
            url = self.fichier.url
        except:
            url = ''
        return url
    
# Model Couturier    
class Couturier(models.Model):
    
    SPECIALITE = (
        ('FEMME', 'Femme'),
        ('HOMME', 'Homme'),
    )
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    num_cnib = models.CharField(max_length=100, null=True)
    specialite = models.CharField(max_length=100, null=True, choices=SPECIALITE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.num_cnib
    
# Model Command   
class Command(models.Model):
    
    ETAT = (
        ('FINIS', 'Finis'),
        ('ENCOURS', 'En cous'),
    )
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    couturier_id = models.ForeignKey(Couturier, on_delete=models.CASCADE, null=True, blank=True)
    date_command = models.DateField()
    transaction_id = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    etat = models.CharField(max_length=100, null=True, choices=ETAT)
    
    def __str__(self):
        return self.id
  # Model Livraison   
class Livraison(models.Model):
    
    ETAT = (
        ('LIVRE', 'livre'),
        ('NON_LIVRE', 'Non libre'),
    )
    
    comand_id = models.ForeignKey(Command, on_delete=models.CASCADE, null=True, blank=True)
    date_livraison = models.DateField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comand_id
    

    

    
# Create your models here.
