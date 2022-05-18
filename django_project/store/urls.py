from django.urls import path
from . import views

urlpatterns = [
    path('', views.FlowersListView.as_view(), name='home'),
    path('product/', views.FlowersView.as_view(), name='product'),
    path('search/', views.Search.as_view(), name='search'),
    path("<slug:slug>/", views.FlowersDetailView.as_view(), name='store_detail'),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
]
