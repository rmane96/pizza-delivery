from rest_framework import generics
from authentication.models import User
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderCreateSerializer , OrderDetailSerializer, OrderStatusUpdateSerializer
from orders.models import Order
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema


User=get_user_model()

class OrderListView(generics.GenericAPIView):
    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    @swagger_auto_schema(operation_summary="List of all Orders")
    def get(self,request):
        orders = Order.objects.all()
        serializer=self.serializer_class(instance=orders,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    # @swagger_auto_schema(operation_summary="List of all Orders")
    # def post(self,request):
    #     data=request.data
    #     serializer=self.serializer_class(data=data)
    #     user = request.user    
        
    #     if serializer.is_valid():
    #         serializer.save(customer=user)
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class OrderDetailView(generics.GenericAPIView):


    serializer_class = OrderDetailSerializer
    permission_classes = [IsAdminUser]
    
    @swagger_auto_schema(operation_summary="Get Order Detail")
    def get(self,request,order_id):
        
        order=get_object_or_404(Order,pk=order_id)
        serializer = self.serializer_class(instance=order)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    @swagger_auto_schema(operation_summary="Update Order Detail")
    def put(self,request,order_id):
        data=request.data  
        serializer=self.serializer_class(data=data)
        order=get_object_or_404(Order,pk=order_id)
        user = request.user
        

        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
        
    
    @swagger_auto_schema(operation_summary="Delete Order")
    def delete(self,request,order_id):
        order=get_object_or_404(Order,pk=order_id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class OrderStatusUpdate(generics.GenericAPIView):


    serializer_class = OrderStatusUpdateSerializer
    permission_classes = [IsAdminUser]
         
    @swagger_auto_schema(operation_summary="Update Order Status")
    def put(self,request,order_id):
   
        order=get_object_or_404(Order,pk=order_id)
        data = request.data 
        serializer = self.serializer_class(data=data,instance=order)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK) 
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
        
class UserOrdersView(generics.GenericAPIView):


    serializer_class = OrderDetailSerializer
    
    @swagger_auto_schema(operation_summary="View specific user's Order")        
    def get(self,request,user_id):
        user=User.objects.get(pk=user_id)
        order = Order.objects.all().filter(customer=user)
        serializer = self.serializer_class(instance=order,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class UserOrderDetail(generics.GenericAPIView):
    serializer_class = OrderDetailSerializer
    
    @swagger_auto_schema(operation_summary="View specific user's specific Order")    
    def get(self,request,user_id,order_id):
        user=User.objects.get(pk=user_id)
        order = Order.objects.all().filter(customer=user).get(pk=order_id)
        serializer = self.serializer_class(instance=order)
        return Response(serializer.data,status=status.HTTP_200_OK)
