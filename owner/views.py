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

    def get(self, request):
        owners = Owner.objects.all()
        result = []
    
        for owner in owners:
            owner_dog = []

            dogs = owner.dog_set.all()
            
            

            for dog in dogs:
                owner_dog.append(
                    {
                        'name':dog.name,
                        'age':dog.age,
                        'owner':dog.owner.name,
                    }
                )

            result.append(
                {
                    'name':owner.name,
                    'age':owner.age,
                    'email':owner.email,
                    'owner_dog':owner_dog
                }
            )
        return JsonResponse({'result':result}, status=200)
        
class DogListView(View):
    def post(self, request):
        data = json.loads(request.body)
        Dog.objects.create(name=data['name'],
                           age=data['age'],
                           owner=Owner.objects.get(name=data['owner'])
                           )
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)

    def get(self, request):
        dogs = Dog.objects.all()
        
        result = []
        for dog in dogs:
            result.append(
            {
              'name': dog.name,
              'age': dog.age,
              'owner': dog.owner.name
            }
          )
        return JsonResponse({'result': result}, status=200)
