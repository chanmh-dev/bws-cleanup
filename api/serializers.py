from dataclasses import field
from rest_framework import serializers
from vdeed_app.models import plastic


class plasticSerializer(serializers.ModelSerializer):
    class Meta:
        model = plastic
        fields = ['plastic_bag_counter', 'plastic_bottle_counter',
                  'plastic_wrapper_counter', 'plastic_cup_straw_counter']
