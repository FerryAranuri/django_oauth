from django.contrib import admin
from django.urls import include, path
from .views import index, IndexView, loginView, logoutView

urlpatterns = [
    path('logout/', logoutView, name="logout"),
    path('login/', loginView, name="login"),
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    
]
