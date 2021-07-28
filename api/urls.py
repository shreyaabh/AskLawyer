from django.urls import path
from django.urls.conf import include
from api import views
from rest_framework.routers import DefaultRouter



router=DefaultRouter()

router.register('askUserapi',views.askUserModelViewset,basename='askUser')
router.register('questionapi',views.questionModelViewset,basename='question')
router.register('askLawyerapi',views.askLawyerModelViewset,basename='askLawyer')
router.register('answerapi',views.answerModelViewset,basename='answer')
router.register('pointsallocateapi',views.pointsAllocateModelViewset,basename='pointsallocate')
router.register('pointsapi',views.pointsModelViewset,basename='points')


urlpatterns = [
    path('',include(router.urls)),
    
]