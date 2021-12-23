from django.views import generic
from . import models, forms, parser
from django.http import HttpResponseRedirect


class FilmView(generic.ListView):
    template_name = 'parser_film/film_index.html'

    def get_queryset(self):
        return models.Film.objects.all()


class ParserAnimeView(generic.FormView):
    template_name = 'parser_film/parser.html'
    form_class = forms.ParserForm
    success_url = '/anime/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parse_data()
            return HttpResponseRedirect(self.success_url)
        else:
            return super(ParserAnimeView, self).post(request, *args, **kwargs)
