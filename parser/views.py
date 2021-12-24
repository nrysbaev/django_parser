from django.shortcuts import get_object_or_404
from django.views.generic import ListView, FormView, DetailView
from . import models, forms
from django.http import HttpResponseRedirect


class FilmView(ListView):
    template_name = 'film_index.html'

    def get_queryset(self):
        return models.Film.objects.all()


class ParserView(FormView):
    template_name = 'parser.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        media_type = form.data['media_type']
        if form.is_valid():
            form.parse_data()
            if media_type == 'anime':
                return HttpResponseRedirect('/anime/')
            elif media_type == 'smartphone':
                return HttpResponseRedirect('/smartphones/')
        else:
            return super(ParserView, self).post(request, *args, **kwargs)


class SmartphoneListView(ListView):
    template_name = 'smartphone_list.html'

    def get_queryset(self):
        return models.Smartphone.objects.all()


class SmartphoneDetailView(DetailView):
    template_name = 'smartphone_detail.html'

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get('id')
        return get_object_or_404(models.Smartphone, id=phone_id)
