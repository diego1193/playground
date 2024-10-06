#from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.admin.views.decorators import staff_member_required
"""
Decoradores de validaciones a para metodos de clases
login_required -> Para especificar que el login es requeridos, no staff
permission_required -> Para especificar que el permiso es requerido 
"""

from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from .models import Page
from .forms import PageForm

# def pages(request):
#     pages = get_list_or_404(Page)
#     return render(request, 'pages/pages.html', {'pages': pages})

# def page(request, page_id, page_slug):
#     page = get_object_or_404(Page, id=page_id)
#     return render(request, 'pages/page.html', {'page': page})


class StaffRiquiredMixin(object):
    """
    Este mixin requerira q el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required) # el metodo decorator, es para poder colocarle un decorador de restriccion a un metodo
    def dispatch(self, request, *args, **kwargs): # Controla la propia peticion
        """
        Apenas ejecute la peticion, el detecta que no es miembro y lo lleva a la pagina de login
        """
        # TODO: eL DECORADOR staff_member_required HACE LO MISMOS QUE LA CONDICIONAL DE ABAJO
        # if not request.user.is_staff:
        #    return redirect(reverse_lazy('admin:login'))

        return super(StaffRiquiredMixin, self).dispatch(request, *args, **kwargs)

class PageListView(ListView):

    model = Page

class PageDetailView(DetailView):

    model = Page

@method_decorator(staff_member_required, name="dispatch") # le idicamos q queremos aplicar el decorador staff_member_required en el metodo dispatch
class PageCreateView(CreateView):

    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages') # Cuando se cree la pagina el redirige a la pagina de pages

    #def get_success_url(self) -> str:
    #    return reverse('pages:pages')

class PagesUpdateView(StaffRiquiredMixin, UpdateView):

    model = Page
    form_class = PageForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + "?ok"

class PagesDeleteView(StaffRiquiredMixin, DeleteView):
    model = Page
    success_url = reverse_lazy("pages:pages")







