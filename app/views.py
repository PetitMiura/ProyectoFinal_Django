from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Movement
from .forms import CompraForm  # Asegúrate de haber creado este formulario Django equivalente a tu formulario Flask
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def index(request):
    movements = Movement.objects.all()
    return render(request, 'index.html', {'movements': movements, 'route': '/', 'title': 'Inicio'})

def purchase(request):
    form = CompraForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            # Aquí implementas la lógica de tu compra
            # Por ejemplo, si estás guardando un objeto Movement:
            movement = form.save()
            messages.success(request, 'Compra realizada exitosamente.')
            return redirect('/')
        else:
            for error in form.errors:
                messages.error(request, form.errors[error])

    return render(request, 'compra.html', {'form': form, 'route': '/compra', 'title': 'Compra'})

def status(request):
    # Aquí implementas la lógica para obtener el estado de la inversión
    # Por ejemplo, si tienes una función que calcula el estado:
    estado = calcular_estado()  # Esta es una función hipotética
    return render(request, 'status.html', {'estado': estado, 'route': '/status', 'title': 'Status'})