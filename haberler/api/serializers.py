from rest_framework import serializers
from haberler.models import Offenlage
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework_gis.filters import InBBoxFilter
from rest_framework_gis.filters import DistanceToPointFilter



class OffenlageSerializer(GeoFeatureModelSerializer):


    class Meta:

        model = Offenlage 
        fields = ('id','name', 'title', 'uuid', 'the_geom', 'offenlage_url', 'owner', 'stadt', 'public', 'offenlage_beginn',  'offenlage_ende',  'uvp_beginn', 'uvp_ende')
        geo_field='the_geom'
        #bbox_geo_field = 'bbox_geometry'
        

    def create(self, validated_data):
        return Offenlage.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id',instance.id)
        instance.name = validated_data.get('name',instance.name)
        instance.title = validated_data.get('title',instance.title)
        instance.the_geom = validated_data.get('the_geom', instance.the_geom)
        instance.the_geom_geojson = validated_data.get('the_geom_geojson', instance.the_geom)
        instance.save()
        return instance


