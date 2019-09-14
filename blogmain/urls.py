from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
	url(r'^', include(('blog.urls', 'blog'), namespace = "blog")), 
    path('admin/', admin.site.urls),
]


