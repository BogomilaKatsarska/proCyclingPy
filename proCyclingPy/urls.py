from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('proCyclingPy.auth_app.urls')),
    path('cyclist/', include('proCyclingPy.cyclist.urls')),
    path('team-manager/', include('proCyclingPy.team_manager.urls')),
    path('calories/', include('proCyclingPy.calories.urls')),
    path('', include('proCyclingPy.common.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
