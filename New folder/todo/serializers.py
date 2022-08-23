from rest_framework import serializers
from rest_framework.response import Response

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


#
#
# class DeleteTodoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Todo
#         fields = '__all__'
#
#     def delete_todo(self, data):
#         return data
#

