from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view


from django.shortcuts import render
from . import serializers



from haberler.models import Offenlage
from haberler.api.serializers import OffenlageSerializer



from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


@api_view(['GET','POST'])
#@csrf_exempt
def offenlage_list_create_api_view(request):
  
    if request.method == 'GET':
        offenlagen = Offenlage.objects.all()
        serializer = OffenlageSerializer(offenlagen,many=True)
        return Response(serializer.data)
        #return JsonResponse(serializer.data)    
    elif request.method == 'POST':
        #data=JSONParser().parse(request)
        
        serializer = OffenlageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return JsonResponse(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        #return  JsonResponse(status = status.HTTP_400_BAD_REQUEST )
        return  Response(status = status.HTTP_400_BAD_REQUEST )
   
       
@api_view(['GET', 'PATCH', 'DELETE'])
def offenlage_list_detail_api_view(request, pk):
    try: 
        offenlagen = Offenlage.objects.get(pk=pk) 
    except Offenlage.DoesNotExist: 
        return Response({'message': 'The offenlagen does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        serializer = OffenlageSerializer(offenlagen) 
        return Response(serializer.data) 
 
    elif request.method == 'PATCH':
      
        #offenlagen_data = JSONParser().parse(request)
        #serializer = OffenlageSerializer(data=request.data)
        offenlagen_serializer = OffenlageSerializer(offenlagen, data=request.data) 
        if offenlagen_serializer.is_valid(): 
            offenlagen_serializer.save()
            return Response(offenlagen_serializer.data) 
        return Response(offenlagen_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        offenlagen.delete() 
        return Response({'message': 'Offenlagen was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def offenlage_list_published_api_view(request):
    offenlagen = Offenlage.objects.filter(public=True)
        
    if request.method == 'GET': 
        offenlagen_serializer = OffenlageSerializer(offenlagen)
        return Response(offenlagen_serializer.data)
