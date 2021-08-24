from django.urls import path,include
from rest_framework.routers import DefaultRouter

from movies import views

app_name = 'movies'

router = DefaultRouter()


router.register('comments',views.CommentViewSet)
router.register('',views.MovieViewSet)


from rest_framework.routers import SimpleRouter



urlpatterns = [
    path('',include(router.urls))
]