from django.shortcuts import render, redirect, get_object_or_404
from .models import Periodista
from .forms import ObjetoForm


# Create your views here.
def Inicio(request):
    return render(request,'Inicio.html')


def Lista(request):
    periodistas = Periodista.objects.all()
    return render(request,'Lista.html', context={'periodistas': periodistas},)

def form_objeto(request):
    if request.method == "POST":
        objeto_form = ObjetoForm(request.POST,request.FILES)
        if objeto_form.is_valid():
            post = objeto_form.save(commit=False)
            post.save()
            return redirect('Lista')
    else:
        objeto_form = ObjetoForm()
        return render(request, 'core/form_objeto.html', {'objeto_form': objeto_form})

def mod_objeto(request, pk):
    post = get_object_or_404(Periodista, pk=pk)
    if request.method == "POST":
        objeto_form = ObjetoForm(request.POST, request.FILES, instance=post)
        if objeto_form.is_valid():
            post = objeto_form.save()
            post.save()
            return redirect('Lista')
    else:
        objeto_form = ObjetoForm(instance=post)
    return render(request, 'core/mod_objeto.html', {'objeto_form': objeto_form})

def delete_objeto(request, pk):
    objeto = Periodista.objects.get(pk=pk)
    objeto.delete()
    return redirect('Lista')
