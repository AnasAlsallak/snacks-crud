from django.urls import path
from .views import HomePageView,AboutPageView,SnackListView,SnackDetailsView,SnackCreateView,SnackUpdateView,SnackDeleteView

urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('about-us',AboutPageView.as_view(), name='about'),
    path('snack-list',SnackListView.as_view(), name='snack-list'),
    path('<int:pk>/',SnackDetailsView.as_view(), name='snack-detail'),
    path('create-snack',SnackCreateView.as_view(), name='create-snack'),
    path('update-snack/<int:pk>',SnackUpdateView.as_view(), name='update-snack'),
    path('delete-snack/<int:pk>',SnackDeleteView.as_view(), name='delete-snack')
]