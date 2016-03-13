from django.conf.urls import patterns, include, url
from django.contrib import admin
from Emilie import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'Emilie.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^searchSimilarImages/$', views.search_similar_images),    #返回图片相关信息
    url(r'^Images/(.*)/$', views.get_similar_image),                #返回图片本身
    url(r'^protocol/$', views.get_protocol),
    url(r'^license/$', views.get_liscense),
    url(r'^FAQ/$', views.get_faq),
    url(r'^about/$', views.get_about),
    url(r'^admin/', include(admin.site.urls)),
    url(r'uploadImage/',views.get_uploadImage),
]
