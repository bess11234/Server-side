from django.db import models

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
# Create your models here.

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class SnippetCategory(models.Model):
    name = models.CharField(max_length=100)

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.IntegerField(default=0)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    category = models.ForeignKey(SnippetCategory, on_delete=models.CASCADE, null=True)
    class Meta:
        ordering = ['created']
    # ADD FIELD
    owner = models.ForeignKey('auth.User', related_name='snippets', null=True, on_delete=models.CASCADE)
    highlighted = models.TextField(null=True)