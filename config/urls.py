from django.contrib import admin
from django.urls import path, include

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.views.generic import TemplateView

schema_view = get_schema_view(
   openapi.Info(
      title="Calorie counter API",
      default_version='v1',
      description="Calculate daily calories",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="info@info.info"),
      license=openapi.License(name="No licence"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/foods/', include('app_calory.urls')),
    path('calc/', TemplateView.as_view(template_name="calc.html"), name='calc'),
    path('', TemplateView.as_view(template_name="home.html")),
#   For API documentation
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
