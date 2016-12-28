from django.shortcuts import render
from django.http import JsonResponse
from hplan_app.models import District

def districts_for_country(request):
#    if request.is_ajax() and request.GET and 'country_id' in request.GET:
    if 'country_id' in request.GET:
        districtlist = list(District.objects.filter(country=request.GET['country_id']).values('id', 'name'))
        districts = {'districts': districtlist}
        return JsonResponse(districts)
    else:
        return JsonResponse({'error': 'Not Ajax or no GET'})
