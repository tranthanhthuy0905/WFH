from rest_framework import serializers
from .models import reportTracking

class reportTrackingSerializers(serializers.ModelSerializer):
    class Meta:
        model = reportTracking
        fields = ['created', 'domain', 'tasks', 'code_commit', 'docs']

    def create(self, validated_data):
        """
        Check the valid input
        """
        return reportTracking.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing TaskTracking, given the validated data
        """
        instance.created = validated_data.get('created', instance.created)
        instance.domain = validated_data.get('domain', instance.domain)
        instance.tasks = validated_data.get('tasks', instance.tasks)
        instance.code_commit = validated_data.get('code_commit', instance.code_commit)
        instance.docs = validated_data.get('docs', instance.docs)
        #instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        return instance
