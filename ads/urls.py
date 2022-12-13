from django.urls import path
from .views import (
    AdsListView,
    AdsDeleteView,
    AdsDetailView,
    AdsUpdateView,
    AdsCreateView,
    CategoryFilterView,
)

urlpatterns = [
    path('', AdsListView.as_view(), name='ads_list'),
    path('<int:pk>/', AdsDetailView.as_view(), name='ads_detail'),
    path('<int:pk>/edit', AdsUpdateView.as_view(), name='ads_edit'),
    path('<int:pk>/delete', AdsDeleteView.as_view(), name='ads_delete'),
    path('new/', AdsCreateView.as_view(), name='ads_create'),
    path('filter/', CategoryFilterView.as_view(), name='filter')
]