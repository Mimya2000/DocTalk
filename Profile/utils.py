from .models import Doctor, Degree
from django.db.models import Q


def searchDoctors(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    degrees = Degree.objects.filter(Q(name__icontains=search_query) | Q(institute__icontains=search_query))
    doctorObj = Doctor.objects.distinct().filter(Q(name__icontains=search_query) | Q(specialization__icontains=search_query)
                                                 | Q(c_address__icontains=search_query) | Q(degree__in=degrees))
    return doctorObj, search_query
