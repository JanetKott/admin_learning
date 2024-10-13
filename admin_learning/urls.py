
from django.contrib import admin
from django.urls import path



urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.conf.urls import include
urlpatterns += [
    path(r'firstapp/', include('firstapp.urls')),
]
from django.views.generic import RedirectView
urlpatterns += [
    path(r'', RedirectView.as_view(url='/firstapp/', permanent=True)),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)