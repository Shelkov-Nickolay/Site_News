from django import forms
from .models import News
from django.core.exceptions import ValidationError


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['name', 'text', 'author']

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        name = cleaned_data.get("name")

        if name == text:
            raise ValidationError(
                "Текст не должен быть идентичен названию."
            )

        return cleaned_data
