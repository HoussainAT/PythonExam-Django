from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Facture
from .forms import AddFactureForm


# Create your views here.
def home_page(request):
    factures = Facture.objects.all()
    nb_facture = len(factures)
    context = {
        'factures': factures,
        'nb_facture': nb_facture
    }
    return render(request, 'index.html', context=context)

def add_facture(request):
    if request.method == 'POST':
        form = AddFactureForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = AddFactureForm()

    return render(request, 'ajout_facture.html', context={'form': form})

def delete_facture(request, id):
    facture = Facture.objects.get(id=id)
    facture.delete()
    return HttpResponseRedirect('/')

def update_facture(request, id):
    facture = Facture.objects.get(id=id)
    form = AddFactureForm(request.POST or None, instance=facture)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, 'update_facture.html', context={'form': form})