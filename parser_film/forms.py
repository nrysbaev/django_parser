from django import forms
from . import parser, models


class ParserForm(forms.Form):
    MEDIA_CHOICES = {
        ('anime', 'anime'),
    }
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parse_data(self):
        if self.data['media_type'] == 'anime':
            anime_data = parser.parser()
            for i in anime_data:
                models.Film.objects.create(**i)
        # elif self.data['media_type'] == 'tvshows':

