from django.http import JsonResponse
from django.views import View
from owners.models import Owner

import json


class OwnerListView(View):
    def post(self, request):
        data = json.loads(request.body)
        Owner.objects.create(name=data["name"], email=data["email"], age=data["age"])
        return JsonResponse({"MESSAGE": "CREATED"}, status=201)
