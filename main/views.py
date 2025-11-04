from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .repositories import *
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

# ---------------------Store-----------------------
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
        
# ---------------------Worker-----------------------
class WorkerDetailAPIView(APIView):
    def get(self, request, id):
        sr = WorkerRepository()
        ser = getSerializer(Worker)

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
        
        sr = WorkerRepository()
        try:
            res = sr.delete_by_id(id)
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        if res == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


class WorkerListCreateUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        sr = WorkerRepository()
        ser = getSerializer(Worker)
        serializer = ser(sr.get_all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        ser = getSerializer(Worker)
        serializer = ser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        sr = WorkerRepository()
        id = request.data.get('id')
        if not id:
            return Response({"Error": "ID is required for update"}, status=status.HTTP_400_BAD_REQUEST)
        
        res = sr.update_by_id(
            id,
            request.data.get('last_name'),
            request.data.get('first_name'),
            request.data.get('email'),
            request.data.get('birth_date'),
            request.data.get('phone_number'),
            request.data.get('store'),
            request.data.get('role')
        )

        if res > 0:
            ser = getSerializer(Worker)
            serializer = ser(sr.get_by_id(id))
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
# ---------------------Role-----------------------
class RoleDetailAPIView(APIView):
    def get(self, request, id):
        sr = RoleRepository()
        ser = getSerializer(Role)

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
        
        sr = RoleRepository()
        try:
            res = sr.delete_by_id(id)
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        if res == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


class RoleListCreateUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        sr = RoleRepository()
        ser = getSerializer(Role)
        serializer = ser(sr.get_all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        ser = getSerializer(Role)
        serializer = ser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        sr = RoleRepository()
        id = request.data.get('id')
        if not id:
            return Response({"Error": "ID is required for update"}, status=status.HTTP_400_BAD_REQUEST)
        
        res = sr.update_by_id(
            id,
            request.data.get('role')
        )

        if res > 0:
            ser = getSerializer(Role)
            serializer = ser(sr.get_by_id(id))
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
# ---------------------Operation-----------------------
class OperationDetailAPIView(APIView):
    def get(self, request, id):
        sr = OperationRepository()
        ser = getSerializer(Operation)

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
        
        sr = OperationRepository()
        try:
            res = sr.delete_by_id(id)
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        if res == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


class OperationListCreateUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        sr = OperationRepository()
        ser = getSerializer(Operation)
        serializer = ser(sr.get_all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        ser = getSerializer(Operation)
        serializer = ser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        sr = OperationRepository()
        id = request.data.get('id')
        if not id:
            return Response({"Error": "ID is required for update"}, status=status.HTTP_400_BAD_REQUEST)
        
        res = sr.update_by_id(
            id,
            request.data.get('operation')
        )

        if res > 0:
            ser = getSerializer(Operation)
            serializer = ser(sr.get_by_id(id))
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
# ---------------------Client-----------------------
class ClientDetailAPIView(APIView):
    def get(self, request, id):
        sr = WorkerRepository()
        ser = getSerializer(Client)

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
        
        sr = ClientRepository()
        try:
            res = sr.delete_by_id(id)
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        if res == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClientListCreateUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        sr = ClientRepository()
        ser = getSerializer(Client)
        serializer = ser(sr.get_all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        ser = getSerializer(Client)
        serializer = ser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        sr = ClientRepository()
        id = request.data.get('id')
        if not id:
            return Response({"Error": "ID is required for update"}, status=status.HTTP_400_BAD_REQUEST)
        
        res = sr.update_by_id(
            id,
            request.data.get('last_name'),
            request.data.get('first_name'),
            request.data.get('email'),
            request.data.get('birth_date'),
            request.data.get('phone_number')
        )

        if res > 0:
            ser = getSerializer(Client)
            serializer = ser(sr.get_by_id(id))
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
# ---------------------Item-----------------------
class ItemDetailAPIView(APIView):
    def get(self, request, id):
        sr = ItemRepository()
        ser = getSerializer(Item)

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
        
        sr = ItemRepository()
        try:
            res = sr.delete_by_id(id)
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        if res == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemListCreateUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        sr = ItemRepository()
        ser = getSerializer(Item)
        serializer = ser(sr.get_all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        ser = getSerializer(Item)
        serializer = ser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        sr = ItemRepository()
        id = request.data.get('id')
        if not id:
            return Response({"Error": "ID is required for update"}, status=status.HTTP_400_BAD_REQUEST)
        
        res = sr.update_by_id(
            id,
            request.data.get('description'),
            request.data.get('name')
        )

        if res > 0:
            ser = getSerializer(Item)
            serializer = ser(sr.get_by_id(id))
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
# ---------------------Estimate-----------------------
class EstimateDetailAPIView(APIView):
    def get(self, request, id):
        sr = EstimateRepository()
        ser = getSerializer(Estimate)

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
        
        sr = EstimateRepository()
        try:
            res = sr.delete_by_id(id)
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        if res == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


class EstimateListCreateUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        sr = EstimateRepository()
        ser = getSerializer(Estimate)
        serializer = ser(sr.get_all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        ser = getSerializer(Estimate)
        serializer = ser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        sr = EstimateRepository()
        id = request.data.get('id')
        if not id:
            return Response({"Error": "ID is required for update"}, status=status.HTTP_400_BAD_REQUEST)
        
        res = sr.update_by_id(
            id,
            request.data.get('item'),
            request.data.get('worker'),
            request.data.get('reasoning'),
            request.data.get('date'),
        )

        if res > 0:
            ser = getSerializer(Estimate)
            serializer = ser(sr.get_by_id(id))
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
# ---------------------OperationHistory-----------------------
class OperationHistoryDetailAPIView(APIView):
    def get(self, request, id):
        sr = OperationHistoryRepository()
        ser = getSerializer(OperationHistory)

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
        
        sr = OperationHistoryRepository()
        try:
            res = sr.delete_by_id(id)
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        if res == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


class OperationHistoryListCreateUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        sr = OperationHistoryRepository()
        ser = getSerializer(OperationHistory)
        serializer = ser(sr.get_all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        ser = getSerializer(OperationHistory)
        serializer = ser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        sr = OperationHistoryRepository()
        id = request.data.get('id')
        if not id:
            return Response({"Error": "ID is required for update"}, status=status.HTTP_400_BAD_REQUEST)
        
        res = sr.update_by_id(
            id,
            request.data.get('client'),
            request.data.get('item'),
            request.data.get('operation'),
            request.data.get('store'),
            request.data.get('date'),
            request.data.get('price'),
            request.data.get('info')
        )

        if res > 0:
            ser = getSerializer(OperationHistory)
            serializer = ser(sr.get_by_id(id))
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)