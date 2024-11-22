from django.db import models

# Create your models here.
class Facture(models.Model):
    ETAT_FACTURE = {
        ('0', 'Non payé'),
        ('1', 'Payé')
    }
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    etat = models.CharField(max_length=1, choices=ETAT_FACTURE, default='0')
    montant = models.FloatField(max_length=100, default=0.00)

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.get_etat_display()} - {self.montant} €"