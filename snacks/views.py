from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack
from django.urls import reverse_lazy

# Create your views here.
class HomePageView(TemplateView):
    template_name="home.html"

class AboutPageView(TemplateView):
    template_name="about.html"

class SnackListView(ListView):
    template_name="snack_list.html"
    model=Snack
    context_object_name = "snacks"

class SnackDetailsView(DetailView):
    template_name="snack_detail.html"
    model=Snack

class SnackCreateView(CreateView):
    template_name="create_snack.html"
    model=Snack
    fields=['name','purchaser','desc','image']

class SnackUpdateView(UpdateView):
    template_name="update_snack.html"
    model=Snack
    fields="__all__"
    success_url=reverse_lazy('snack-list')

class SnackDeleteView(DeleteView):
    template_name="delete_snack.html"
    model=Snack
    fields=['name','purchaser','desc','image']
    success_url=reverse_lazy('snack-list')