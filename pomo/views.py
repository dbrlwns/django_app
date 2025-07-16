from django.shortcuts import render, redirect
from django.utils.dateparse import parse_datetime

from pomo.models import Pomo
import json

# Create your views here.
def pomo(request):
    return render(request, 'pomo/pomo.html')

def pomo_complete(request):
    if request.method == 'POST':
        print("타이머 완료, ", json.loads(request.body))
        total_minutes = json.loads(request.body).get('total_time')
        finished_at = parse_datetime(json.loads(request.body).get('finished_at'))

        Pomo.objects.create(
            time=total_minutes,
            created=finished_at,
        )

        return render(request, 'pomo/pomo_complete.html')
    return render(request, 'pomo/pomo_complete.html')