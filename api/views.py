import imp
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.
# model object -- single student data
def Student_detail(request,pk):
    #this stu is model object which stores complex dataa and shows the data according to the primary key
    stu = Student.objects.get(id = pk)
    # print('############', stu)
    # this serializer is the variable which convert complex data to python data
    serializer = StudentSerializer(stu)
    # print('************',serializer)
    # print('!!!!!!!!!!!!',serializer.data)
    # json_data is the variable which convert python data to json and provide it to the client
    json_data = JSONRenderer().render(serializer.data)
    # print('------------->',json_data)
    return HttpResponse(json_data,content_type = 'application/json')
#Query set
def Student_list(request):
    stu = Student.objects.all()
    # print('############', stu)
    serializer = StudentSerializer(stu,many = True)
    # print('************',serializer)
    # print('!!!!!!!!!!!!',serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    # print('------------->',json_data)
    return HttpResponse(json_data,content_type = 'application/json')



