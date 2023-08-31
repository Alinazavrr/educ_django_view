from rest_framework import serializers

from homes.models import Home


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = [
            'title',
            'info',
            's',
            'district',
            'cost',
            'img',
            'manager',
            'category'
        ]
