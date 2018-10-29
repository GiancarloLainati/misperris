from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Rescatado
from django.contrib.auth.decorators import login_required, permission_required
from .forms import RescatadoForm
from django.views.generic import CreateView
from misperris import settings

# Create your views here.

def index(request):
    return render(request, 'blog/index.html', {})

def rescatado_list(request):
    user = request.user
    rescatados = Rescatado.objects.filter(estado='disponible').order_by('estado')
    if user.has_perm('blog.admin'):
        return render(request, 'blog/rescatado_list_admin.html', {'rescatados': rescatados})
    else:
        return render(request, 'blog/rescatado_list.html', {'rescatados': rescatados})

def rescatado_detail(request, pk):
    rescatado = get_object_or_404(Rescatado, pk=pk)
    return render(request, 'blog/rescatado_detail.html', {'rescatado': rescatado})


def rescatado_new(request):
    if request.method == "POST":
            form = RescatadoForm(request.POST, request.FILES)
            if form.is_valid():
                rescatado = form.save(commit=False)
                rescatado.author = request.user
                rescatado.published_date = timezone.now()
                rescatado.save()
                return redirect('rescatado_detail', pk=rescatado.pk)
    else:
        form = RescatadoForm()
    return render(request, 'blog/rescatado_edit.html', {'form': form})

def rescatado_edit(request, pk):
    rescatado = get_object_or_404(Rescatado, pk=pk)
    if request.method == "POST":
        form = RescatadoForm(request.POST, request.FILES, instance=rescatado)
        if form.is_valid():
            rescatado = form.save(commit=False)
            rescatado.author = request.user
            rescatado.save()
            return redirect('rescatado_detail', pk=rescatado.pk)
    else:
        form = RescatadoForm(instance=rescatado)
    return render(request, 'blog/rescatado_edit.html', {'form': form})

def rescatado_delete(request, pk):
    rescatado = get_object_or_404(Rescatado, pk=pk)
    rescatado.delete()
    return render(request, 'blog/exito_delete.html')


