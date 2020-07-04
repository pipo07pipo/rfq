from django.shortcuts import render
from django.http import HttpResponse
from .models import RFQ, Part_Header
from django.utils import timezone

def index(request):
    # text = "This is index page"
    # rfq = RFQ(tracker_no=111,description='Desc',customer_name='sample', update_date=timezone.now())
    # rfq.save()
    projects = []   
    for item in RFQ.objects.all():
        projects.append([item.tracker_no,item.description,item.customer_name])
    context = {
        'projects': projects
    }
    return render(request, 'rfqsite/index.html', context)

def projects(request):
    projects = []   
    for item in RFQ.objects.all():
        projects.append([item.tracker_no,item.description,item.customer_name])
    context = {
        'projects': projects
    }
    return render(request, 'rfqsite/projects.html', context)

def parts(request, tracker_no):
    projects = []
    text = ''
    try:
        part_header = Part_Header.objects.get(tracker_no=tracker_no)
    except:
        text = 'No Part Found'

    try:
        rfq = RFQ.objects.get(pk=tracker_no)
        projects.append([rfq.tracker_no,rfq.description,rfq.customer_name])
    except:
        text = 'No Project at this tracker no'
    context = {
        'projects': projects,
        'text': text
    }

    return render(request, 'rfqsite/part_table.html', context)

