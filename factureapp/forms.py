from django import forms

from factureapp.models import Facture

class FactureForm(forms.Form):

    ETAT_FACTURE = {
        ('0', 'Non payé'),
        ('1', 'Payé')
    }
    nom = forms.CharField()
    prenom = forms.CharField()
    etat = forms.ChoiceField()
    montant = forms.FloatField()

class AddFactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['nom', 'prenom', 'etat', 'montant']