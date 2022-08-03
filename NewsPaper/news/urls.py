from django.urls import path
from .views import PostsList, PostDetail, SearchList, PostCreateView

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('search/', SearchList.as_view()),
    path('create/', PostCreateView.as_view(), name='post_create')

]

