from django.http import JsonResponse
from django.views import View
from dogs.models import Dog
from owners.models import Owner

import json


class DogListView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            name = data["name"]
            age = data["age"]
            owner = Owner.objects.get(name=data["owner"])

            dog = Dog(name=name, age=age, owner=owner)
            dog.save()
            return JsonResponse({"MESSAGE": "CREATED"}, status=201)
        except ValueError:
            return JsonResponse({"MESSAGE": "VALUE ERROR"}, status=400)
        except KeyError:
            return JsonResponse({"MESSAGE": "KEY ERROR"}, status=400)
