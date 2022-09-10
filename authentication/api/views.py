from django.shortcuts import render
from rest_framework import generics
from authentication.models import User
from authentication.api.serializers import UserCreateSerializer, serializers
from rest_framework.response import Response
from rest_framework import status

class register(generics.GenericAPIView):
    
    serializer_class = UserCreateSerializer
    
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        

