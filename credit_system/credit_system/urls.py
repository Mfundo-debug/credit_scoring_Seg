"""
URL configuration for credit_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # new
from rest_framework.routers import DefaultRouter # new
from credit_score_app import views # new
from credit_score_app.views import CreditScoringPrediction # updated

router=DefaultRouter() # new
router.register(r'customers', views.CustomerViewSet) # new
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), # new
    path('api/predict-credit-score/', CreditScoringPrediction.as_view(), name='predict_credit_score'), # new
]
