import json
from datetime import date, timedelta, datetime

from django.contrib.auth.decorators import login_required
from django.db.models.functions import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string, get_template
from django.views.decorators.csrf import csrf_exempt

from django.template import Context, loader

from app.models import *

def index(request):

    try:
        lTemp = TemperatureCount()
        lTemp.temp_value = request.POST.get('temp_value')
        lTemp.save()

        dataset = TemperatureCount.objects.all().order_by('modified_at')

        categories = []
        series = []

        for singleRecord in dataset:
            categories.append(singleRecord.modified_at.strftime('%Y-%m-%d %H:%M'))
            series.append(singleRecord.temp_value)

        print('categories',categories)
        print('series',series)


    except Exception as e:
        print(e)

    return render(request, 'highchart_temp.html', {'categories': json.dumps(categories), 'series': json.dumps(series),})