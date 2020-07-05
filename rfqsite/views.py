from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import RFQ, Part_Header
from django.utils import timezone

def rfq_table(request):
    # text = "This is index page"
    # rfq = RFQ(tracker_no=111,description='Desc',customer_name='sample', update_date=timezone.now())
    # rfq.save()
    projects = RFQ.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'rfqsite/index.html', context)

def projects(request):
    projects = RFQ.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'rfqsite/projects.html', context)

def parts(request, tracker_no):
    project = RFQ.objects.get(pk=tracker_no)
    parts = [part for part in Part_Header.objects.filter(tracker_no=tracker_no)]
    context = {
        'project': project,
        'parts': parts
    }
    return render(request, 'rfqsite/part_table.html', context)

def add_part(request, tracker_no):
    project = RFQ.objects.get(pk=tracker_no)   
    context = {
        'project': project
    }
    return render(request, 'rfqsite/add_part.html', context)

def add_part_confirm(request):
    tracker_no = request.POST.get('tracker-no')
    part_level = request.POST.get('part-level')
    part_no = request.POST.get('part-no')
    part_name = request.POST.get('part-name')
    program = request.POST.get('program')
    newPart = Part_Header(tracker_no=RFQ.objects.get(tracker_no=tracker_no),level=part_level,no=part_no,name=part_name,program=program)
    newPart.save()
    return redirect('/part_table/'+tracker_no)

def add_child(request):
    project = []
    context = {
        'project': project
    }
    return render(request, 'rfqsite/add_child.html', context)

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

