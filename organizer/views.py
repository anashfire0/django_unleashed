from django.template import loader, Context, Template
from django.http import HttpResponse, Http404
from .models import Tag, StartUp, NewsLink
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .forms import TagForm, StartUpForm, NewsLinkForm
from .utils import ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from django.urls import reverse_lazy


def tag_list(request):
    tag_list = Tag.objects.all()
    template = loader.get_template('organizer/tag_list.html')
    rendered_template = template.render({'tag_list': tag_list})
    return HttpResponse(rendered_template)


def tag_detail(request, slug):
    print(str(type(request)).center(300, '|'))
    # try
    #     tag = Tag.objects.get(slug__iexact='hi')
    # except Tag.DoesNotExist:
    #     raise Http404
    tag = get_object_or_404(Tag, slug__iexact=slug)
    # template = loader.get_template('organizer/tag_detail.html')
    # rendered_template = template.render({'tag':tag})
    # return HttpResponse(rendered_template)
    return render(request, 'organizer/tag_detail.html', {'tag': tag})


def startup_list(request):
    return render(request, 'organizer/startup_list.html', {'startup_list': StartUp.objects.all()})


def startup_detail(request, slug):
    startup = get_object_or_404(StartUp, slug__iexact=slug)
    return render(request, 'organizer/startup_detail.html', {'startup': startup})

# def tag_create(request):
#     if request.method == 'POST':
#         form = TagForm(request.POST)
#         if form.is_valid():
#             new_tag = form.save()
#             return redirect(new_tag)
#     else:  # request.method != 'POST'
#         form = TagForm()
#     return render(request, 'organizer/tag_form.html', {'form': form})


class TagCreate(ObjectCreateMixin, View):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'


class StartUpCreate(ObjectCreateMixin, View):
    form_class = StartUpForm
    template_name = 'organizer/startup_form'


class StartUpDelete(ObjectDeleteMixin, View):
    model = StartUp
    success_url = reverse_lazy('organizer_startup_list')
    template_name = 'organizer/startup_confirm_delete.html'


class NewsLinkCreate(ObjectCreateMixin, View):
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
    model = TagForm
    template = 'organizer/tag_form_update.html'


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
