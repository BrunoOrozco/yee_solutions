from django.views.generic import *
from objetivos.models import *
from ventas.models import *


class UserDetailView(DetailView):
    
    queryset = ObjetivoCliente.objects.all() 

    template_name = 'ventas/dashboard__avances.html'

    slug_field = 'cliente'

    slug_url_kwarg = 'cliente'

    context_object_name = 'avance'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        cliente = self.get_object()
        context['facturas_cliente'] = Venta.objects.filter(cliente=cliente).order_by('fecha')

        print(context)
        return context