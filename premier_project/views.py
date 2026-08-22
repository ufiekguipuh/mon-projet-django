from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render
from .models import Station

@csrf_exempt
def index(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            station_liste = data.get("Station_liste")
            return JsonResponse({
                "status": "success",
                "Station_liste": station_liste
            })
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "JSON invalide"}, status=400)
    else: 
        return render(request, 'index.html')

@csrf_exempt
def stations_en_garde(request):
    # Récupération de toutes les stations
    stations = Station.objects.all()
    data = [
        {
            "nom": s.nom,
            "lat": float(s.latitude),
            "lng": float(s.longitude),
            "en_garde": s.en_garde
        }
        for s in stations
    ]
    return JsonResponse({"stations": data})
