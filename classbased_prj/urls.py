"""
URL configuration for classbased_prj project.

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
from django.urls import path
from classbased_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sample',views.Read.as_view(),name='sample'),
    path('display/',views.Display.as_view(),name='display'),
    path('<int:pk>/update',views.Update.as_view(),name='update'),
    path('<int:pk>/delete',views.Delete.as_view(),name='delete')
]
