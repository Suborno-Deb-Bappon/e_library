from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView  # Add this import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/ebooks/', permanent=False), name='root'),  # Redirect root to /ebooks/
    path('', include('elibrary.urls')),  # Keep existing include
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)