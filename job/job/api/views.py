import imp
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ApplicantSerializer
from .models import *

# Create your views here.

@api_view(['GET'])
def apiOverview(request): 
    api_urls = {
        'List':'/applicant-list/',
        'Detail View': '/applicant-detail/<str:pk>/',
        'Create':'/applicant-create/',
        'Update':'/applicant-update/<str:pk>/',
        'Delete':'/applicant-delete/<str:pk>/',
    }
    
    return Response(api_urls)


@api_view(['GET'])
def applicantList(request):
    
    applicants= Applicant.objects.all()
    serializer = ApplicantSerializer(applicants, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def applicantDetail(request,pk):
    applicants= Applicant.objects.get(id=pk)
    serializer = ApplicantSerializer(applicants, many= False)
    return Response(serializer.data)


@api_view(['POST'])
def applicantCreate(request):
    serializer = ApplicantSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def applicantUpdate(request, pk):
    applicant= Applicant.objects.get(id=pk)
    serializer = ApplicantSerializer(instance= applicant, data=request.data, many= False)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def applicantDelete(request, pk):
    applicant = Applicant.objects.get(id=pk)
    applicant.delete()
    return Response("Applicant Deleted!")
