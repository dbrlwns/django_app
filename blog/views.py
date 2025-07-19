from django.shortcuts import render, redirect
from blog.models import Post, Comment

# Create your views here.
def blog_list(request):
    posts = Post.objects.all()
    content = {
        'posts': posts,
    }
    return render(request, 'blog/blog_list.html', content)


def view_blog(request, post_id):

    post = Post.objects.get(id=post_id)
    content = {
        'post': post,
    }
    return render(request, 'blog/blog.html', content)

def blog_add(request):

    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        thumbnail = request.FILES['thumbnail']

        post = Post.objects.create(
            title=title,
            content=content,
            thumbnail=thumbnail,
        )

        return redirect(f'/blog/{post.id}/')

    return render(request, 'blog/blog_add.html')