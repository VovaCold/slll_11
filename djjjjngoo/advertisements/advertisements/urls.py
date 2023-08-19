from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from djjjjngoo.advertisements.advertisements import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lesson_4', include('app_lesson_4.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, documrnt_root=settings.MEDIA_ROOT)

