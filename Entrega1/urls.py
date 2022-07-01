from msilib.schema import Error
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404
from AppGimnasios.views import Error404View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppGimnasios.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = Error404View.as_view()
