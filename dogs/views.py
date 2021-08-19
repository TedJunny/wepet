import json

from django.http import JsonResponse
from django.views import View

from dogs.models import Dog
from owners.models import Owner


class DogListView(View):
    def post(self, request):
        data = json.loads(request.body)

        if not Owner.objects.filter(id=data["owner_id"]).exists():
            return JsonResponse({"message": "Does Not Exist"}, status=400)

        Dog.objects.create(
            name=data["name"],
            age=data["age"],
            owner_id=data["owner_id"],
        )

        return JsonResponse({"MESSAGE": "CREATED"}, status=201)

    def get(self, request):
        result = []
        dogs = Dog.objects.all()
        for dog in dogs:
            result.append({"name": dog.name, "age": dog.age, "owner": dog.owner.name})

        return JsonResponse({"results": result}, status=200)
