from django.urls import path
from blog.views import blog_list, view_blog, blog_add, comment_delete

from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'
urlpatterns = [
    path('', blog_list),
    path('<int:post_id>/', view_blog, name='view-blog'),
    path('add/', blog_add),
    path('delete/comment/<int:comment_id>/', comment_delete),
]
