from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Rescatado
from django.contrib.auth.decorators import login_required, permission_required
from .forms import RescatadoForm
from django.views.generic import CreateView
from misperris import settings
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from blog.quickstart import serializers
from django.template.loader import get_template
from django.http import HttpResponse
import json

# Create your views here.

def index(request):
    return render(request, 'blog/index.html', {})

def base_layout(request):
    return render(request, 'blog/base.html', {})

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


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

def charcha_serviceworker(request, js):
    template = get_template('charcha-serviceworker.js')
    html = template.render()
    return HttpResponse(html, content_type="application/x-javascript")