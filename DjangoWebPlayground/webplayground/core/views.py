from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):

    template_name = "core/home.html"
    
    # estamos sobre escribiendo las respoestas en si mismas
    # siempre que estemos sobre escribiendo de la vista basada en clase se debe pasar  *args, **kwargs
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"title": "Mi super web playground" })

class SamplePageView(TemplateView):

    template_name = "core/sample.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Mi super web playground" 
        return context
    