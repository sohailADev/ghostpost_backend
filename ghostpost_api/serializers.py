from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import models


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.BoastsRoastsModel
        fields = '__all__'



class UpVoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.BoastsRoastsModel
        fields = '__all__'

class downVoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.BoastsRoastsModel
        fields = '__all__'