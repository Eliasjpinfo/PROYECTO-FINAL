"""
URL configuration for blog project.

The urlpatterns list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    
Add an import:  from my_app import views
Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    
Add an import:  from other_app.views import Home
Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    
Import the include() function: from django.urls import include, path
Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from django.conf import settings # type: ignore
from blog.views import IndexView, not_found_view, internal_error_view, forbidden_view
from django.conf.urls.static import static # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='home'),
    path('', include('apps.user.urls')),
    path('', include('apps.post.urls')),
]


# Manejadores de errores
handler404 = not_found_view
handler500 = internal_error_view
handler403 = forbidden_view
# Los manejadores estan disponibles en cualquier parte de la aplicación,
# por lo que no es necesario importarlos en cada vista.
# o incluso aqui en blog\blog\urls.py

if settings.DEBUG:
    from django.conf.urls.static import static # type: ignore
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)