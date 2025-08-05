from django.http import Http404
from django.shortcuts import render, redirect
from blog.models import Post, Comment
from users.models import User

# Create your views here.
def blog_list(request):
    posts = Post.objects.all()
    content = {
        'posts': posts,
    }
    return render(request, 'blog/blog_list.html', content)


def comment_delete(request, comment_id):
    cmt = None
    try:
        cmt = Comment.objects.filter(id=comment_id).first()
    except Comment.DoesNotExist:
        raise Http404
    if request.user == cmt.author:
        cmt.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))

def view_blog(request, post_id):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        Comment.objects.create( author=request.user,
                                content=comment,
                                post_id=post_id )
        return redirect(request.META.get('HTTP_REFERER', '/blog'))

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