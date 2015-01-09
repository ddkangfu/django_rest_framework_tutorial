from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    pk = serializers.Field()
    title = serializers.CharField(reqired=False, max_length=100)
    code = serializers.CharField(widgets.TextArea, max_length=100000)
    linenos = serializers.BooleanField(required=True)
    language = serializers.CharField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def restore_project(self, attrs, instance=None):
        if instance:
            instance.title = attrs.get('title', instance.title)
            instance.code = attrs.get('code', instance.code)
            instance.linenos = attrs.get('linenos', instance.linenos)
            instance.language = attrs.get('language', instance.linenos)
            instance.style = attrs.get('style', instance.style)
            return instance

        return Snippet(**attrs)
