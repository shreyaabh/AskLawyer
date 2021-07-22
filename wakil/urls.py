from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()

router.register('profileapi',views.profileModelViewset,basename='profile')
router.register('educationapi',views.educationModelViewset,basename='education')
router.register('experienceapi',views.experienceModelViewset,basename='experience')
router.register('awardsapi',views.awardsModelViewset,basename='awards')
router.register('linkapi',views.linkModelViewset,basename='link')


urlpatterns = [
    path('',include(router.urls)),
]