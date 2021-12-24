from django import forms
from . import parser, parser_phone, models


class ParserForm(forms.Form):
    MEDIA_CHOICES = {
        ('anime', 'anime'),
        ('smartphone', 'smartphone')
    }
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parse_data(self):
        if self.data['media_type'] == 'anime':
            anime_data = parser.parser_func()
            for i in anime_data:
                models.Film.objects.create(**i)
        elif self.data['media_type'] == 'smartphone':
            phone_data = parser_phone.parser_func()
            for i in phone_data:
                models.Smartphone.objects.create(**i)
