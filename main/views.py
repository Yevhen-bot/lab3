from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .repositories import StoreRepository
from .serializers import *
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# class StoreViewSet(viewsets.ModelViewSet):
#     """
#     A viewset for viewing and editing user instances.
#     """
#     serializer_class = getSerializer(Store)
#     queryset = Store.objects.all()

class StoreDetailAPIView(APIView):
    def get(self, request, id):
        sr = StoreRepository()
        ser = getSerializer(Store)

        obj = sr.get_by_id(id)
        if obj is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(ser(obj).data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        sr = StoreRepository()
        try:
            res = sr.delete_by_id(id)
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        if res == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


class StoreListCreateUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        sr = StoreRepository()
        ser = getSerializer(Store)
        serializer = ser(sr.get_all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        ser = getSerializer(Store)
        serializer = ser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        sr = StoreRepository()
        id = request.data.get('id')
        if not id:
            return Response({"Error": "ID is required for update"}, status=status.HTTP_400_BAD_REQUEST)
        
        res = sr.update_by_id(
            id,
            request.data.get('name'),
            request.data.get('country'),
            request.data.get('street'),
            request.data.get('city'),
            request.data.get('house_number')
        )

        if res > 0:
            ser = getSerializer(Store)
            serializer = ser(sr.get_by_id(id))
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)