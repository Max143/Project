from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('branches/autocomplete', views.BankDetailView)
router.register('branches', views.BankBranchView)

urlpatterns = [
    path('api/', include(router.urls)),

    
]

  