from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

class WishListView(ListView):
    # model = Post
    template_name = 'wishlist/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
