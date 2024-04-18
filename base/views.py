from django.shortcuts import render, redirect, HttpResponse
from .models import Material, Comanda, RaportCalitate
from .forms import ComandaForm
# Create your views here.
def homeFabrica(request):
    materiale = Material.objects.all()
    comenzi_recente = Comanda.objects.order_by('-data_plasare')[:10]
    context = {'materiale':materiale, 'comenzi_recente':comenzi_recente}
    return render(request, './baza/homeBaza.html', context)
    # return HttpResponse('sunt in fabrica')


def plaseazaComanda(request):
    if request.method == 'POST':
        form = ComandaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ComandaForm()
    
    context = {'form':form}
    return render(request, 'baza/plaseazaComanda.html', context)
        


