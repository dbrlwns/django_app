from django.urls import path
from blog.views import blog_list, view_blog, blog_add

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', blog_list),
    path('<int:post_id>/', view_blog),
    path('add/', blog_add),
]
