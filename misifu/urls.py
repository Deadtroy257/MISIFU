from django.contrib import admin
from django.urls import path, include
from accounts.views import home_view, nosotros_view, contact_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', home_view, name='home'),  # Ruta para la página de inicio
    path('nosotros/', nosotros_view, name='nosotros'),  # Ruta para la página de "Nosotros"
    path('contact/', contact_view, name='contact'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
