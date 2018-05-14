from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.db.models import Model
from djanog.core.exceptions import ImproperlyConfigured

class ObjectCreateMixin:
    form_class = None
    template_name = ''

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            return redirect(bound_form.save())
        else:
            return render(request, self.template_name, {'form': bound_form})


class ObjectUpdateMixin:
    form_class = None
    template_name = ''
    model = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template_name, {
            'form': self.form_class(instance=obj), self.model.__name__.lower(): obj,
        })

    def post(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        bound_form = self.form_class(request.POST, instance=obj)
        if bound_form.is_valid():
            return redirect(bound_form.save())
        else:
            return render(request, self.template_name, {'form': bound_form, self.model.__name__.lower(): obj})


class ObjectDeleteMixin:
    model = None
    success_url = ''
    template_name = ''

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template_name, {self.model.__name__.lower(): obj, })

    def post(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        obj.delete()
        return HttpResponseRedirect(self.success_url)

class DetailView(View):
    model = None
    context_object_name = ''
    template_name = str()
    template_name_suffix = '_detail'

    def get(self, request, **kwargs):
        self.kwargs = kwargs
        self.object = self.get_object()
        template_name = self.get_templates_name()
        context = self.get_context_data()
        return render(request, template_name, context)

    def get_context_object_name(self):
        if self.context_object_name:
            return self.context_object_name
        elif isinstance(self.object, Model):
            return self.object._meta.model_name
        else:
            return None

    def get_templates_name(self):
        if self.template_name:
            return template_name
        return f'{self.object._meta.app_label}/{self.object._meta.model_name}{self.template_name_suffix}.html'

    def get_context_data(self):
        context = {}
        if self.object:
            context_object_name = self.get_context_object_name()
            if context_object_name:
                context[context_object_name] = self.object
        return context

    def get_object(self):
        slug = self.kwargs.get('slug')
        if slug is None:
            raise AttributeError(f'{self.__class__.__name__} expects'
                ' {slug} from URL pattern.')
        if self.model:
            return get_object_or_404(self.model, slug__iexact=slug)
        else:
            raise ImproperlyConfigured(f'{self.__class__.__name__} needs "model" attribute')