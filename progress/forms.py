from django import forms

from .models import ProgressPost


class ProgressPostForm(forms.ModelForm):
    class Meta:
        model = ProgressPost
        fields = ['title', 'content', 'workout_focus', 'minutes_trained', 'image']
