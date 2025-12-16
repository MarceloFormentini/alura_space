from django.shortcuts import get_object_or_404, render
from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.all()
    fotografias = fotografias.order_by('data_fotografia').filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards': fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})


def buscar(request):
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)

    if 'buscar' in request.GET:
        termo_busca = request.GET['buscar']
        if termo_busca:
            fotografias = fotografias.filter(
                nome__icontains=termo_busca
            )

    return render(request, 'galeria/buscar.html', {'cards': fotografias})