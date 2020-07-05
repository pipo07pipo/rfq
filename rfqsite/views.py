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
        text = 'No Part Founds'

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

def add_child(request):
    projects = []   
    context = {
        'projects': projects
    }
    return render(request, 'rfqsite/add_child.html', context)

def add_part(request):
    projects = []   
    context = {
        'projects': projects
    }
    return render(request, 'rfqsite/add_part.html', context)

def edit_active_rate(request):
    projects = []   
    context = {
        'projects': projects
    }
    return render(request, 'rfqsite/edit_active_rate.html', context)

def edit_ctp(request):
    projects = []   
    context = {
        'projects': projects
    }
    return render(request, 'rfqsite/edit_ctp.html', context)

def edit_forecast(request):
    projects = []   
    context = {
        'projects': projects
    }
    return render(request, 'rfqsite/edit_forecast.html', context)

def edit_material(request):
    projects = []   
    context = {
        'projects': projects
    }
    return render(request, 'rfqsite/edit_material.html', context)

def edit_mst(request):
    projects = []   
    context = {
        'projects': projects
    }
    return render(request, 'rfqsite/edit_mst.html', context)

def edit_part_costing(request):
    projects = []   
    context = {
        'projects': projects
    }
    return render(request, 'rfqsite/edit_part_costing.html', context)

def edit_part_info(request):
    projects = []   
    context = {
        'projects': projects
    }
    return render(request, 'rfqsite/edit_part_info.html', context)

def edit_rfq(request):
    projects = []   
    context = {
        'projects': projects
    }
    return render(request, 'rfqsite/edit_rfq.html', context)

def edit_special_process_rate(request):
    projects = []   
    context = {
        'projects': projects
    }
    return render(request, 'rfqsite/edit_special_process_rate.html', context)

def edit_sps(request):
    projects = []   
    context = {
        'projects': projects
    }
    return render(request, 'rfqsite/edit_sps.html', context)

def part_info(request):
    projects = []   
    context = {
        'projects': projects
    }
    return render(request, 'rfqsite/part_info.html', context)

def part_table(request):
    projects = []   
    context = {
        'projects': projects
    }
    return render(request, 'rfqsite/part_table.html', context)

