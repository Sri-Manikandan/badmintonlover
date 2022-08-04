from django.contrib import admin
from django.urls import path, include
from home.views import home
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('store/', include('store.urls')),
    path('cart/', include('cart.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
