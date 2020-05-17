"""restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from core import views as core_views
from posts import views as post_views

# JWT Authentication
from rest_framework_simplejwt import views as jwt_views

# Swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Restful API",
      default_version='v1',
      description="Restful API Boilerplate",
      terms_of_service="https://example.com/policies/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'users', core_views.UserViewSet)
# router.register(r'groups', core_views.GroupViewSet)
router.register(r'posts', post_views.PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', schema_view, name='openapi-schema'),

    ##  Restful API
    # Core
    path('api/ping/', core_views.PingView.as_view(), name='client_ping'),
    
    # Authentication
    path('api/', include('authjwt.urls'), name='auth'),

    # Router for resources
    path('api/', include(router.urls), name='restful'),

    # Swagger docs
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)