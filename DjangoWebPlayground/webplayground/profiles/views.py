from django.shortcuts import get_object_or_404
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import Profile

class ProfileListView(ListView):
    model = Profile
    template_name = "profiles/profile_list.html"
    paginate_by = 3

class ProfileDetailView(DetailView):
    model = Profile
    template_name = "profiles/profile_detail.html"

    def get_object(self):
        print(self.kwargs)
        return get_object_or_404(Profile, user__username=self.kwargs['username'])



