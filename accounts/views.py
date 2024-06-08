from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib import messages
from .models import Veterinaria, Producto, TipDeCuidado, CitaMedica, Producto, Carrito, CarritoProducto
from .forms import CitaMedicaForm 

def home_view(request):
    return render(request, 'home.html')


def nosotros_view(request):
    return render(request, 'nosotros.html')

def contact_view(request):
    if request.method == 'POST':
        # Aquí podrías manejar el envío del formulario, por ejemplo, enviando un correo electrónico.
        # Por simplicidad, solo mostraremos un mensaje de éxito.
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        mensaje = request.POST.get('mensaje')
        
        # Aquí puedes agregar la lógica para manejar el mensaje, como enviarlo por correo electrónico.
        
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('ingreso')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def ingreso_view(request):
    context = {
        'is_ingreso': True
    }
    return render(request, 'accounts/ingreso.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Usuario creado exitosamente.')
                return redirect('login')  # Redirige a la página de inicio u otra página después del registro exitoso
            else:
                messages.error(request, 'Error en la autenticación. Verifique sus credenciales e intente nuevamente.')
        else:
            messages.error(request, 'Error al crear el usuario. Verifique los datos e intente nuevamente.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def citas_medicas(request):
    if request.method == 'POST':
        form = CitaMedicaForm(request.POST)
        if form.is_valid():
            cita = form.save(commit=False)
            cita.user = request.user
            cita.save()
            messages.success(request, 'Cita agendada exitosamente.')
            return redirect('citas_medicas')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = CitaMedicaForm()
    
    veterinarias = Veterinaria.objects.all()
    return render(request, 'main/citas_medicas.html', {'veterinarias': veterinarias, 'form': form})

@login_required
def listar_citas(request):
    citas = CitaMedica.objects.filter(user=request.user)
    return render(request, 'main/listar_citas.html', {'citas': citas})

@login_required
def cancelar_cita(request, cita_id):
    cita = get_object_or_404(CitaMedica, id=cita_id, user=request.user)
    if request.method == 'POST':
        cita.delete()
        messages.success(request, 'Cita cancelada exitosamente.')
        return redirect('listar_citas')
    return render(request, 'main/cancelar_cita.html', {'cita': cita})

@login_required
def tienda(request):
    productos = Producto.objects.all()
    carrito = None
    productos_en_carrito = {}
    
    if request.user.is_authenticated:
        carrito, created = Carrito.objects.get_or_create(usuario=request.user)
        productos_en_carrito = {item.producto.id: item.cantidad for item in CarritoProducto.objects.filter(carrito=carrito)}
    
    return render(request, 'main/tienda.html', {'productos': productos, 'productos_en_carrito': productos_en_carrito})


@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    carrito_producto, created = CarritoProducto.objects.get_or_create(carrito=carrito, producto=producto)
    if not created:
        carrito_producto.cantidad += 1
        carrito_producto.save()
    messages.success(request, 'Producto agregado al carrito.')
    return redirect('tienda')

@login_required
def ver_carrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    productos = CarritoProducto.objects.filter(carrito=carrito)
    total = sum(item.producto.precio * item.cantidad for item in productos)
    
    # Precalcular los totales para cada producto
    productos_info = []
    for item in productos:
        productos_info.append({
            'producto': item.producto,
            'cantidad': item.cantidad,
            'subtotal': item.producto.precio * item.cantidad,
        })
    
    return render(request, 'main/ver_carrito.html', {'productos_info': productos_info, 'total': total})


@login_required
def quitar_del_carrito(request, producto_id):
    carrito = get_object_or_404(Carrito, usuario=request.user)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito_producto = get_object_or_404(CarritoProducto, carrito=carrito, producto=producto)
    if carrito_producto.cantidad > 1:
        carrito_producto.cantidad -= 1
        carrito_producto.save()
    else:
        carrito_producto.delete()
    messages.success(request, 'Producto quitado del carrito.')
    return redirect('ver_carrito')

@login_required
def realizar_compra(request):
    carrito = get_object_or_404(Carrito, usuario=request.user)
    productos = CarritoProducto.objects.filter(carrito=carrito)
    total = sum(item.producto.precio * item.cantidad for item in productos)
    
    # Por simplicidad, solo vaciaremos el carrito y mostraremos un mensaje.
    carrito.productos.clear()
    messages.success(request, f'Compra realizada. Total: ${total:.2f}')
    return redirect('tienda')
@login_required
def tips_cuidado(request):
    tips = TipDeCuidado.objects.all()
    return render(request, 'main/tips_cuidado.html', {'tips': tips})