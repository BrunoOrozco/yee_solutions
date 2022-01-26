from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

def login_view(request):
    """Iniciar sesisón"""
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        log_auth = authenticate(request, username=username, password= password)

        if log_auth:
            login(request, log_auth)
            return redirect('kpi')

        else:
            return render(request, 'ventas/index.html', {'error' : 'El usuario o la constraseña son incorrectos, intenta de nuevo.'})

    return render(request, 'ventas/index.html')


@login_required(login_url='login')
def logout_view(request):
    """" Salida sesión"""
    logout(request)

    return redirect('login')


class Error404View(TemplateView):
    template_name = "ventas/error_404.html"

class Error500View(TemplateView):
    template_name = "ventas/error_500.html"

    @classmethod

    def as_error_view(cls):
        v = cls.as_view()
        def view(request):
            r = v(request)
            r.render()

            return r
        return view