from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta: 
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        # Customises the form input to be 80cols wide not default 40
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}