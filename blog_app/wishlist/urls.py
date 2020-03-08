from django.urls import path
from wishlist import views as wishlist_views

urlpatterns = [
    path('', wishlist_views.WishListView.as_view(), name='wishlist_index'),
]
