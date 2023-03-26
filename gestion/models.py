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
        return f'{self.nom} {self.prenom}'
    
    @property
    def fileURL(self):
        try:
            url = self.fichier.url
        except:
            url = ''
        return url
    
    
class Post(models.Model):
    
    libelle = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.libelle
    
      
# Model Couturier    
class Couturier(models.Model):
    
    SPECIALITE = (
        ('Femme', 'Femme'),
        ('Homme', 'Homme'),
        ('Mixte', 'Mixte'),
    )
    nom = models.CharField(max_length=100, null=True)
    prenom = models.CharField(max_length=100, null=True)
    num_cnib = models.CharField(max_length=100, null=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    specialite = models.CharField(max_length=100, null=True, blank=True, choices=SPECIALITE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.num_cnib
    
    
# Model Command   
class Command(models.Model):
    
    num_commande = models.CharField(unique=True, max_length=100, null=True, blank=True)
    articles = models.ManyToManyField(Tenue, through='LigneCommande')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    couturier = models.ForeignKey(Couturier, on_delete=models.CASCADE, null=True, blank=True)
    adresse_livraison = models.CharField(max_length=100, null=True, blank=True)
    date_commande = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.num_commande
    
    
class LigneCommande(models.Model):
    article = models.ForeignKey(Tenue, null=True, blank=True, on_delete=models.CASCADE)
    commande = models.ForeignKey(Command, null=True, blank=True, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    create_at = models.DateField(auto_now_add=True, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now_add=True)
  
    

  # Model Livraison   
class Livraison(models.Model):
    
    num_livraison = models.CharField(unique=True, max_length=100, null=True, blank=True)
    commande = models.ForeignKey(Command, on_delete=models.CASCADE, null=True, blank=True)
    date_livaison = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.num_livraison
    

    

    
# Create your models here.
