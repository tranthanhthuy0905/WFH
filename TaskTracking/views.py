#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
#from django.shortcuts import render
from rest_framework.parsers import JSONParser
from taskTracking.models import reportTracking
from taskTracking.serializers import reportTrackingSerializers

@csrf_exempt
def report_list(request):
    """
    List of all reports available inside the scope of team
    """
    if request.method == 'GET':
        report = reportTracking.objects.all()
        serializer = reportTrackingSerializers(report, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = reportTrackingSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def report_detail(request, pk):
    """
    Retrieve, update or delete a task report
    """
    try:
        report = reportTracking.objects.get(pk=pk)
    # Make sure the QuerySet returned exists
    except reportTracking.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = reportTrackingSerializers(report)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = reportTrackingSerializers(report, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        report.delete()
        return HttpResponse(satus=204)

