from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^edit/profile/$',views.edit_profile,name='edit_profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/hood$', views.new_hood, name='new-hood'),
    url(r'^hoods/new/post/(\d+)$', views.post_new, name='new-post'),
    url(r'^map$', views.maps, name='maps'),
    url(r'^hoods/new/business/(\d+)$',views.post_business, name='new-business'),
    url(r'^hoods/(\d+)',views.hoods,name='hoods'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
