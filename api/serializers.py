from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    department = serializers.CharField(max_length=100)
    post = serializers.CharField(max_length=100)
    cnic = serializers.IntegerField()
    contact = serializers.IntegerField()
    city = serializers.CharField(max_length=70)

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.department = validated_data.get('department', instance.department)
        instance.post = validated_data.get('post', instance.post)
        instance.cnic = validated_data.get('cnic', instance.cnic)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance