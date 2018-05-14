from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$',views.welcome,name='welcome'),

    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^post/', views.photo_post, name='post'),
    url(r'^profile/', views.prof, name='profile'),
    url(r'^viewprofile/', views.viewprofile, name='viewprofile'),
    url(r'^search/',views.search_results, name='search_results'),
    url(r'^comment/',views.post_comment, name='comment'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
