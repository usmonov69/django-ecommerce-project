
from django.contrib import admin
from django.urls import path, include

# from django.conf.urls import url
from django.conf import settings
from django.views.static import serve


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
]

# To display images

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

