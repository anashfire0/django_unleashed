from django.template import loader, Context, Template
from django.http import HttpResponse, Http404
from .models import Tag, StartUp, NewsLink
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, DetailView as OrigDetailView
from .forms import TagForm, StartUpForm, NewsLinkForm
from .utils import (
    CreateView, ObjectUpdateMixin, ObjectDeleteMixin,
    DetailView)
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import method_decorator, login_required


# def tag_list(request):
#     tag_list = Tag.objects.all()
#     template = loader.get_template('organizer/tag_list.html')
#     rendered_template = template.render({'tag_list': tag_list})
#     return HttpResponse(rendered_template)

class TagList(View):
    template_name = 'organizer/tag_list.html'
    model = Tag

    def get(self, request, page_number=None):
        return render(request, self.template_name, {'tag_list': self.model.objects.all()})


class TagPageList(View):
    template_name = 'organizer/tag_list.html'
    paginate_by = 5

    def get(self, request, page_number):
        tags = Tag.objects.all()
        paginator = Paginator(tags, self.paginate_by)
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)

        if page.has_previous():
            prev_url = reverse(
                'organizer_tag_page',
                args=(
                    page.previous_page_number(),
                ))
        else:
            prev_url = None
        if page.has_next():
            next_url = reverse(
                'organizer_tag_page',
                args=(
                    page.next_page_number(),
                ))
        else:
            next_url = None

        context = {
            'is_paginated':
            page.has_other_pages(),
            'next_page_url': next_url,
            'paginator': paginator,
            'previous_page_url': prev_url,
            'tag_list': page,
        }
        return render(
            request, self.template_name, context)


# def tag_detail(request, slug):
#     print(str(type(request)).center(300, '|'))
#     # try
#     #     tag = Tag.objects.get(slug__iexact='hi')
#     # except Tag.DoesNotExist:
#     #     raise Http404
#     tag = get_object_or_404(Tag, slug__iexact=slug)
#     # template = loader.get_template('organizer/tag_detail.html')
#     # rendered_template = template.render({'tag':tag})
#     # return HttpResponse(rendered_template)
#     return render(request, 'organizer/tag_detail.html', {'tag': tag})


class TagDetail(OrigDetailView):
    template_name = 'organizer/tag_detail.html'
    context_object_name = 'tag'

    def get_queryset(self):
        return Tag.objects.all()


class StartUpDetail(DetailView):
    template_name = 'organizer/startup_detail.html'
    model = StartUp
    context_object_name = 'startup'


class StartUpList(View):
    template_name = 'organizer/startup_list.html'
    model = StartUp
    paginate_by = 5
    page_kwarg = 'page'
    model = StartUp

    def get(self, request):
        paginator = Paginator(self.model.objects.all(), self.paginate_by)
        # page_number = request.GET.get(self.page_kwarg, 1)
        page_number = request.GET.get(self.page_kwarg,)
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)

        print(str(request.path).center(600,'%'))
        if page.has_previous():
            prev_url = f'?{self.page_kwarg}={page.previous_page_number()}'
        else:
            prev_url = None
        if page.has_next():
            next_url = f'?{self.page_kwarg}={page.next_page_number()}'
        else:
            next_url = None
        print(str(request.GET).center(500, '%'))
        return render(request, self.template_name, {'startup_list': page,
                                                    'paginator': paginator,
                                                    'is_paginated': page.has_other_pages(),
                                                    'previous_page_url': prev_url,
                                                    'next_page_url': next_url})


# def tag_create(request):
#     if request.method == 'POST':
#         form = TagForm(request.POST)
#         if form.is_valid():
#             new_tag = form.save()
#             return redirect(new_tag)
#     else:  # request.method != 'POST'
#         form = TagForm()
#     return render(request, 'organizer/tag_form.html', {'form': form})


class TagCreate(CreateView, View):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class StartUpCreate(CreateView, View):
    form_class = StartUpForm
    template_name = 'organizer/startup_form'


class StartUpDelete(ObjectDeleteMixin, View):
    model = StartUp
    success_url = reverse_lazy('organizer_startup_list')
    template_name = 'organizer/startup_confirm_delete.html'


class NewsLinkCreate(CreateView, View):
    form_class = NewsLinkForm
    template_name = 'organizer/newslink_form.html'


class NewsLinkUpdate(View):
    form_class = NewsLinkForm
    template_name = 'organizer/newslink_form_update.html'

    def get(self, request, pk):
        newslink = get_object_or_404(NewsLink, pk=pk)
        return render(request, self.template_name, {
            'form': self.form_class(instance=NewsLink),
            'newslink': newslink,
        })

    def post(self, request, pk):
        newslink = get_object_or_404(NewsLink, pk=pk)
        bound_form = self.form_class(request.POST, instance=newslink)
        if bound_form.is_valid():
            return redirect(bound_form.save())
        else:
            return render(request, self.template_name, {'form': bound_form,
                                                        'newslink': newslink})


class TagUpdate(ObjectUpdateMixin, View):
    form_class = TagForm
    model = Tag
    template_name = 'organizer/tag_form_update.html'


class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    success_url = reverse_lazy('organizer_tag_list')
    template_name = 'organizer/tag_confirm_delete.html'


class StartUpUpdate(ObjectUpdateMixin, View):
    form_class = StartUpForm
    model = StartUp
    template = 'organizer/start_form_update.html'


class NewsLinkDelete(View):

    def get(self, request, pk):
        newslink = get_object_or_404(NewsLink, pk=pk)
        return render(request, 'organizer/newslink_confirm_delete.html', {'newslink': newslink})

    def post(self, request, pk):
        newslink = get_object_or_404(NewsLink, pk=pk)
        startup = newslink.startup
        newslink.delete()
        return redirect(startup)
