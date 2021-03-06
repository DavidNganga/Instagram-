from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$',views.welcome,name='welcome'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^post/', views.photo_post, name='post'),
    url(r'^profile/', views.prof, name='profile'),
    url(r'^viewprofile/(\d+)', views.viewprofile, name='viewprofile'),
    url(r'^search/',views.search_results, name='search_results'),
    url(r'^comment/(\d+)',views.post_comment, name='comment'),
    url(r'^likes/(\d+)',views.likes, name='likes'),
    url(r'^imagedetails/(\d+)', views.imagedetails, name='imagedetails'),
    url(r'^follow/(\d+)', views.follow, name='follow'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
