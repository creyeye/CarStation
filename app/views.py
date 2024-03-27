from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostCreationForm, PostUpdateForm


def index(request):
    return render(request, 'app/index.html')


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'app/about.html', {"posts": posts})


def post_detail(request, pk):

    post = get_object_or_404(Post, id=pk)

    if request.method == 'POST':
        form = PostCreationForm(request.POST,  instance=post)

        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    form = PostUpdateForm(instance=post)
    return render(
        request,
        'app/post_detail.html',
        {
            'post': post,
            'form': form
        })


