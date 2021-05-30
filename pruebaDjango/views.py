from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from .models import Tweet, Noticias, Datos_Cripto, AuthUser, Datos_Transacciones

from django.contrib import messages
from .forms import CreateUserForm


# Create your views here.

def home(request):
    datos_bitcoin = Datos_Cripto.objects.filter(nombre__exact="Bitcoin EUR").order_by('hora').distinct()
    datos_ethereum = Datos_Cripto.objects.filter(nombre__exact="Ethereum EUR").order_by('hora').distinct()
    datos_binance = Datos_Cripto.objects.filter(nombre__exact="BinanceCoin EUR").order_by('hora').distinct()
    datos_tether = Datos_Cripto.objects.filter(nombre__exact="Tether EUR").order_by('hora').distinct()
    datos_doge = Datos_Cripto.objects.filter(nombre__exact="Dogecoin EUR").order_by('hora').distinct()
    datos = Datos_Cripto.objects.filter(nombre__icontains="").order_by('hora').distinct()[:16]
    user = None
    print(request.user)

    if request.user.is_authenticated:
        user = AuthUser.objects.filter(username__exact=request.user)

    if request.method == "POST":
        query = request.POST.get('buscar')
        print(query)
        tweets = Tweet.objects.using('mongo').filter(texto__icontains=query).distinct()[:6]
        print(tweets)

        return render(request, "pruebaDjango/inicio.html",
                      {'tweets': tweets, 'datos': datos, 'datos_bitcoin': datos_bitcoin,
                       'datos_ethereum': datos_ethereum, 'datos_binance': datos_binance,
                       'datos_tether': datos_tether, 'datos_doge': datos_doge,
                       'user': user})

    tweets = Tweet.objects.using('mongo').all()[:6]

    # datos_bitcoin = Datos_Cripto.objects.filter(nombre__exact="Bitcoin EUR").distinct()

    print(tweets)
    print(datos_bitcoin)

    return render(request, "pruebaDjango/inicio.html",
                  {'tweets': tweets, 'datos': datos, 'datos_bitcoin': datos_bitcoin, 'datos_ethereum': datos_ethereum,
                   'datos_binance': datos_binance,
                   'datos_tether': datos_tether, 'datos_doge': datos_doge,
                   'user': user})


def news(request):
    user = None
    print(request.user)

    if request.user.is_authenticated:
        user = AuthUser.objects.filter(username__exact=request.user)

    if request.method == "POST":
        query = request.POST.get('cat_noticia')
        mas_noticias = request.POST.get('mas_noticias')
        print(query)
        print(mas_noticias)

        if mas_noticias == "false":
            noticias = Noticias.objects.using('mongo').filter(articulo__icontains=query).distinct()[:3]

        else:
            noticias = Noticias.objects.using('mongo').filter(articulo__icontains=query).distinct()[:6]

        return render(request, "pruebaDjango/noticias.html", {'noticias': noticias, 'user': user})

        '''tweets = Tweet.objects.filter(texto__icontains=query)[:6]
        return render(request, "pruebaDjango/inicio.html", {'tweets': tweets})'''

    noticias = Noticias.objects.using('mongo').all()[:3]
    return render(request, "pruebaDjango/noticias.html", {'noticias': noticias, 'user': user})


def resources(request):
    return render(request, "pruebaDjango/noticias.html")


def simulator(request):

    if request.user.is_authenticated:

        datos_bitcoin = Datos_Cripto.objects.filter(nombre__exact="Bitcoin EUR").order_by('hora').distinct()
        datos_ethereum = Datos_Cripto.objects.filter(nombre__exact="Ethereum EUR").order_by('hora').distinct()
        datos_binance = Datos_Cripto.objects.filter(nombre__exact="BinanceCoin EUR").order_by('hora').distinct()
        datos_tether = Datos_Cripto.objects.filter(nombre__exact="Tether EUR").order_by('hora').distinct()
        datos_doge = Datos_Cripto.objects.filter(nombre__exact="Dogecoin EUR").order_by('hora').distinct()
        datos_transacciones = Datos_Transacciones.objects.filter(usuario__exact=request.user).distinct()[:10]
        error = None

        if request.method == "POST":

            operacion = request.GET.get('operacion')
            user = AuthUser.objects.get(username=request.user)
            error = True
            transaccion_nueva = Datos_Transacciones(usuario=request.user)
            # sfgsfg
            if operacion == 'comprar':

                cantidad = float(request.POST.get('cantidad'))
                euros = float(request.POST.get('euros'))
                cripto = request.POST.get('cripto1')

                print(operacion, cantidad, euros)

                print("antes:", type(user.cartera), type(euros))

                print("bit, cant:", type(user.bitcoin), type(cantidad))

                if euros < user.cartera:
                    error = False

                    print("antes:", user.cartera, user.bitcoin)

                    user.cartera -= euros

                    if cripto == 'Bitcoin':
                        user.bitcoin += cantidad

                    elif cripto == 'BinanceCoin':
                        user.binancecoin += cantidad

                    elif cripto == 'Ethereum':
                        user.ethereum += cantidad

                    transaccion_nueva.cantidad = cantidad
                    transaccion_nueva.precio = euros
                    transaccion_nueva.tipo = 'compra'
                    transaccion_nueva.criptomoneda = cripto

                    transaccion_nueva.save()
                    user.save()
                    print("después:", user.cartera, user.bitcoin)

            elif operacion == 'vender':

                cantidad = float(request.POST.get('cantidad2'))
                euros = float(request.POST.get('euros2'))
                cripto = request.POST.get('cripto2')

                print(operacion, cantidad, euros)

                print("antes:", type(user.cartera), type(euros))

                print("bit, cant:", type(user.bitcoin), type(cantidad))

                if cripto == 'Bitcoin' and cantidad < user.bitcoin:
                    user.bitcoin -= cantidad
                    error = False

                elif cripto == 'BinanceCoin' and cantidad < user.binancecoin:
                    user.binancecoin -= cantidad
                    error = False

                elif cripto == 'Ethereum' and cantidad < user.ethereum:
                    user.ethereum -= cantidad
                    error = False

                if error == False:
                    print("antes:", user.cartera, user.bitcoin)
                    user.cartera += euros

                    transaccion_nueva.cantidad = cantidad
                    transaccion_nueva.precio = euros
                    transaccion_nueva.tipo = 'venta'
                    transaccion_nueva.criptomoneda = cripto

                    transaccion_nueva.save()
                    user.save()
                    print("después:", user.cartera, user.bitcoin)

        print(request.user)
        user = AuthUser.objects.filter(username__exact=request.user)

        print(error)
        return render(request, "pruebaDjango/simulador.html",
                      {'datos_transacciones': datos_transacciones, 'datos_bitcoin': datos_bitcoin,
                       'datos_ethereum': datos_ethereum,
                       'datos_binance': datos_binance,
                       'datos_tether': datos_tether, 'datos_doge': datos_doge,
                       'user': user,
                       'error': error})

    # En otro caso redireccionamos al login
    return redirect('/login')


def register(request):
    form = CreateUserForm(request.POST)
    if form.is_valid():
        form.save()
        nombre = form.cleaned_data.get('username')
        user = AuthUser.objects.get(username=nombre)

        user.cartera = 500000
        user.bitcoin = 0
        user.binancecoin = 0
        user.ethereum = 0

        user.save()

        messages.success(request, 'Account was created for ' + nombre)
        return redirect('/login')
    context = {"form": form}
    return render(request, 'pruebaDjango/register.html', context)


def loginPage(request):

    pagina = request.GET.get('next')
    print(pagina)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if pagina is None:
                return redirect('/simulador')
            else:
                return redirect(pagina)

        else:
            messages.info(request, 'Username Or Password is incorrect')
            return render(request, 'pruebaDjango/login.html')

    return render(request, 'pruebaDjango/login.html')


# Cartera y criptomonedas
def logoutUser(request):
    logout(request)
    return redirect('/login')
