
from django.conf import settings
from django.conf.urls.static import static # 스태틱
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG: # 셋팅스에서 디버그 옵션을 켰을 때
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)