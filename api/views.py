from .models import Employee
import io
from rest_framework.parsers import JSONParser
# from django.shortcuts import render
from .serializers import EmployeeSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def employee_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = EmployeeSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            msg = 'Data Created Successfully'
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'PATCH':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        emp = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(emp, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            msg = 'Data Updated Successfully'
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        emp = Employee.objects.get(id=id)
        emp.delete()
        msg = 'Data Deleted !!'
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data, content_type='application/json')
