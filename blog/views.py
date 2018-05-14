from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.views.generic import View
from .forms import PostForm
# Create your views here.


class PostList(View):
    template_name = 'blog/post_list.html'

    def get(self, request, parent_template=None):
        return render(request, PostList.template_name, {'post_list': Post.objects.all(), 'parent_template': parent_template})


def post_detail(request, year, month, slug, parent_template=None):
    post = get_object_or_404(Post, pub_date__year=year,
                             pub_date__month=month, slug__iexact=slug)
    return render(request, 'blog/post_detail.html', {'post': post, 'parent_template': parent_template})


class PostCreate(View):
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        bound_data = self.form_class(request.POST)
        if bound_data.is_valid():
            return redirect(bound_data.save())
        else:
            return render(request, self.template_name, {'form': bound_data})


class PostUpdate(View):
    form_class = PostForm
    model = Post
    template_name = 'blog/post_form_update.html'

    def get_object(self, year, month, slug):
        post = get_object_or_404(Post, pub_date__year=year, pub_date__month=month, slug=slug)
        return post

    def get(self, request, year, month, slug):
        post = self.get_object(year, month, slug)
        return render(request, self.template_name, {'form': self.form_class(instance=post), 'post': post})

    def post(self, request, year, month, slug):
        post = self.get_object(year, month, slug)
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            return redirect(bound_form.save())
        else:
            return render(request, self.template_name, {'form': bound_form, 'post': post})


class PostDelete(View):

    def get(self, request, year, month, slug):
        post = get_object_or_404(Post, year=year, month=month, slug__iexact=slug)
        return render(request, 'blog/post_delete_confirm.html', {'post':post})

    def post(self, request, year, month, slug):
        post = get_object_or_404(Post, year=year, month=month, slug__iexact=slug)
        post.delete()
        return redirect('blog_post_list')
