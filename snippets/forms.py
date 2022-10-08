from socket import fromshare
from django import forms

from snippets.models import Snippet

class SnippetForm(form.ModelsForm):
    class Meta:
        model = Snippet
        fields = ('title', 'code', 'description')



