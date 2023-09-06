from django.contrib import admin
from django.urls import path,include
from .views import signup,loginn,logout_view,home,table,download,api_viewset
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r"downloadapi",api_viewset)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name='home'),
    path("signup/",signup,name='signup'),
    path("login/",loginn,name='login'),
    path("logout/",logout_view,name='logout'),
    path("table/",table,name='table'),
    path("download/<int:id>/",download,name='download'),
    path("api/",include(router.urls)),
    path("auth/",include('rest_framework.urls'))
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
