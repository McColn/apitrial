from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer,SMSSerializer,ReceivedSMSSerializer
from .models import Student,SMS,ReceivedSMS
import json
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics

# Create your views here.

class SMSListView(generics.ListCreateAPIView):
    queryset = ReceivedSMS.objects.all()
    serializer_class = ReceivedSMSSerializer

class StudentDetail(APIView):
    @csrf_exempt
    def get(self,request):
        obj = Student.objects.all()
        serializer = StudentSerializer(obj,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self,request):
#         serializer = StudentSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk):
#         try:
#             student = Student.objects.get(pk=pk)
#         except Student.DoesNotExist:
#             return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
# @api_view(['POST'])
# def add_data(request):
#     if request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)


# @api_view(['POST','GET'])
# def get_data(request):
#     # Handle GET request logic here
#     if request.method == 'POST':
#         return Response({'message': 'POST request handled successfully'})
#     if request.method == 'GET':
#         return Response({'message': 'GET request handled successfully'})

# def home(request):
#     return render(request,'app/home.html')


    
# class StudentViewSet(viewsets.ModelViewSet):
#     serializer_class = StudentSerializer
#     queryset = Student.objects.all()

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)
    #     # Serialize the data and join the dictionaries as a JSON-formatted string
    #     response_data = ",".join(json.dumps(item) for item in serializer.data)
    #     # Return the JSON-formatted string as an HTTP response
    #     return HttpResponse(response_data, content_type="application/json")



# @api_view(['GET'])
# def getData(request):
#     student = Student.objects.all()
#     serializer = StudentSerializer(student,many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def addData(request):
#     serializer = StudentSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)  # Return a 201 Created status code for successful POST requests
#     return Response(serializer.errors, status=400) 



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from rest_framework.parsers import JSONParser
from .models import ReceivedSMS
from .serializers import ReceivedSMSSerializer

@csrf_exempt
@require_POST
def received_sms(request):
    try:
        data = JSONParser().parse(request)
        serializer = ReceivedSMSSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
    except Exception as e:
        print("Error processing received SMS data:", e)
        return JsonResponse({'status': 'error'}, status=500)



