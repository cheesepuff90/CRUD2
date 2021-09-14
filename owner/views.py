from django.shortcuts import render
import json

from django.http import JsonResponse
from django.views import View
from owner.models import Owner, Dog

class OwnerListView(View):
    def post(self, request):
        data = json.loads(request.body)
        Owner.objects.create(name=data['name'],
                             email=data['email'],
                             age=data['age'])
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)

class DogListView(View):
    def post(self, request):
        data = json.loads(request.body)
        Dog.objects.create(name=data['name'],
                           age=data['age'],
                           owner=Owner.objects.get(name=data['owner'])
                           )
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)
