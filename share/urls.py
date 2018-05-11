from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),

    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^post/', views.post, name='post')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
