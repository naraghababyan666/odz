import json

from django.shortcuts import render

# Create your views here.
from django.template.context_processors import request
from rest_framework.generics import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView

from todo.models import Todo
from todo.serializers import TodoSerializer


class getTasks(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        data = TodoSerializer(todos, many=True)
        return Response(data.data)


class removeTask(APIView):
    def post(self, request):
        obj = get_object_or_404(Todo, id=request.data['id'])
        obj.delete()
        return Response({'success': 'Successfully deleted'})
        # idd = request.data['id']
        # todos = Todo.objects.all()
        # current = []
        # data = DeleteTodoSerializer(todos, many=True)
        # for item in data.data:
        #
        #     if item['id'] == request.data['id']:
        #         current = item
        # return Response(current)


class createTask(APIView):
    def post(self, request):
        todo = Todo.objects.create(description=request.data['description'])
        return Response({'success': 'Successfully created'})
