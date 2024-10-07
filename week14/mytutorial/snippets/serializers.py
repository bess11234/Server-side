from rest_framework import serializers
from snippets.models import Snippet, SnippetCategory

from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'category', 'owner', 'highlighted']
    
    # Field-level validation
    def validate_linenos(self, value):
        """
        Check that line number cannot be negative.
        """
        if value and value < 0:
            raise serializers.ValidationError("Line number cannot be negative")
        return value
    
    def validate(self, data):
        """
        Check that if the language is Python the snippet's title must contains 'django'
        """
        if data['language'] == 'python' and 'django' not in data['title'].lower():
            raise serializers.ValidationError("For Python, snippets must be about Django")
        return data
    
class SnippetCategorySerializer(serializers.ModelSerializer):
    snippet_set = SnippetSerializer(many=True, read_only=True)

    class Meta:
        model = SnippetCategory
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']