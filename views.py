from django.shortcuts import render

from django.http import JsonResponse
from django.utils.encoding import smart_unicode

from hplan_app.models import District

def districts_for_country(request):
    if request.is_ajax() and request.GET and 'country_id' in request.GET:
        districts = list(District.objects.filter(country=request.GET['country_id']).values('id', 'name'))
        return JsonResponse(districts, safe=False)
    else:
        return JsonResponse({'error': 'Not Ajax or no GET'})
