from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import WishListItem


# Create your views here.

class WishListView(ListView):
    model = WishListItem
    template_name = 'wishlist/index.html'
    context_object_name = 'items'
    ordering = ['-date_posted']
    paginate_by = 5
