from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from Forum import views

router=DefaultRouter()

router.register('forumapi',views.forumModelViewset,basename='forum')
router.register('Discussionapi',views.DiscussionModelViewset,basename='Discussion')


urlpatterns = [
    path('',include(router.urls)),
]