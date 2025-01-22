from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views import ProductViewSet, CategoryViewSet

# router = DefaultRouter()
# router.register(r'v1/product', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', ProductViewSet.as_view({'get': 'list'})),
    path('category/', CategoryViewSet.as_view({'get': 'list'})),
    # path(r'', include(router.urls)),
]

urlpatterns += debug_toolbar_urls()
