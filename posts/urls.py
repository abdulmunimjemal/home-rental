from django.urls import path
from .views import (
    AdsListView,
    AdsDeleteView,
    AdsDetailView,
    AdsUpdateView,
    AdsCreateView,
    CategoryFilterView,
    OwnPostsView,
    FavPostsView,
    PostLikeAction,
    newpost
)

urlpatterns = [
    path('<int:pk>/like', PostLikeAction.as_view(), name='like'),
    path('<int:pk>/edit', AdsUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete', AdsDeleteView.as_view(), name='delete'),
    path('<int:pk>/', AdsDetailView.as_view(), name='view'),
    # path('new/', AdsCreateView.as_view(), name='new'),
    path('new/', newpost, name='new'),
    path('filter/', CategoryFilterView.as_view(), name='filter'),
    path('own/', OwnPostsView.as_view(), name='my_posts'),
    path('favorite/', FavPostsView.as_view(), name='fav'),
    path('', AdsListView.as_view(), name='list'),
]
