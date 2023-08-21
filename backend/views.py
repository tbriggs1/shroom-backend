from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from backend.models import Mushrooms
from backend.serializers import MushroomsSerializer

@csrf_exempt
def mushrooms_list(request):
    """
    List all mushrooms or create a new mushroom
    """
    if request.method == 'GET':
        mushrooms = Mushrooms.objects.all()
        serializer = MushroomsSerializer(mushrooms, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MushroomsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def mushroom_detail(request, pk):
    """
    Retrieve, update or delete a mushroom
    """
    try:
        mushroom = Mushrooms.objects.get(pk=pk)
    except Mushrooms.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MushroomsSerializer(mushroom)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MushroomsSerializer(mushroom, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=404)

    if request == 'DELETE':
        mushroom.delete()
        return HttpResponse(status=204)