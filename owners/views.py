from django.http import JsonResponse
from django.views import View
from owners.models import Owner
from dogs.models import Dog

import json


class OwnerListView(View):
    def post(self, request):
        data = json.loads(request.body)
        Owner.objects.create(name=data["name"], email=data["email"], age=data["age"])
        return JsonResponse({"MESSAGE": "CREATED"}, status=201)

    def get(self, request):
        result = []
        owners = Owner.objects.all()

        for owner in owners:
            dogs = Dog.objects.filter(owner=owner.id)
            result.append(
                {
                    "name": owner.name,
                    "email": owner.email,
                    "age": owner.age,
                    "dog_list": list(dogs.values()),
                }
            )
        return JsonResponse({"results": result}, status=200)
