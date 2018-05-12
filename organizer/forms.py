from django import forms
from organizer.models import Tag
from django.core.exceptions import ValidationError
from.models import Tag, StartUp, NewsLink


class SlugCleanMixin:
    def clean_slug(self):
        if self.cleaned_data['slug'].lower() == 'create':
            raise ValidationError('"create" cannot be used as a slug')
        return self.cleaned_data['slug'].lower()


class TagForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
    # name = forms.CharField(max_length=31,)
    # slug = forms.SlugField(max_length=31, help_text='A label for URL config')

    def clean_name(self):
        return self.cleaned_data['name'].lower()


class StartUpForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = StartUp
        fields = '__all__'


class NewsLinkForm(forms.ModelForm):
    class Meta:
        model = NewsLink
        fields = '__all__'
