from django.shortcuts import render, redirect, get_object_or_404


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
