from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import RFQ, Part_Header, Active_Rate, SP_Rate
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

def rfq_table(request):
    # text = "This is index page"
    # rfq = RFQ(tracker_no=111,description='Desc',customer_name='sample', update_date=timezone.now())
    # rfq.save()
    projects = RFQ.objects.all()
    context = {
        'projects': projects
    }
    active_project = []
    for project in projects:
        active_project.append(project.tracker_no)
    active_to_rfq = []
    for active in Active_Rate.objects.all():
        active_to_rfq.append(active.tracker_no.tracker_no)
    for tracker in active_to_rfq:
        if tracker in active_project:
            active_project.remove(tracker)
    print(active_project)
    for tracker in active_project:
        active_rate = Active_Rate(tracker_no=RFQ.objects.get(tracker_no=tracker))
        sps = SP_Rate(tracker_no=RFQ.objects.get(tracker_no=tracker))
        active_rate.save()
        sps.save()
    return render(request, 'rfqsite/index.html', context)

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
    if request.method == 'POST':
        tracker_no = request.POST.get('tracker-no')
        part_level = request.POST.get('part-level')
        part_no = request.POST.get('part-no')
        part_name = request.POST.get('part-name')
        program = request.POST.get('program')
        newPart = Part_Header(tracker_no=RFQ.objects.get(tracker_no=tracker_no),level=part_level,no=part_no,name=part_name,program=program)
        newPart.save()
        return redirect('/part_table/'+tracker_no)

def edit_rfq(request, tracker_no):
    project = RFQ.objects.get(pk=tracker_no)
    context = {
            'project': project
    }
    return render(request, 'rfqsite/edit_rfq.html', context)

def edit_rfq_confirm(request):
    if request.method == 'POST' and request.FILES:
        file = request.FILES['file']
        fs = FileSystemStorage()
        tracker_no = request.POST.get('tracker-no')
        folder = tracker_no+"/"
        path = folder+file.name
        filename = fs.save(path, file)
        project = RFQ.objects.get(pk=tracker_no)
        project.customer_name = request.POST.get('customer-name')
        project.file_path = path
        project.save()
        return redirect('/part_table/'+tracker_no)
    elif request.method == 'POST':
        tracker_no = request.POST.get('tracker-no')
        project = RFQ.objects.get(pk=tracker_no)
        project.customer_name = request.POST.get('customer-name')
        project.save()
        return redirect('/part_table/'+tracker_no)


def edit_active_rate(request, tracker_no):
    project = RFQ.objects.get(pk=tracker_no)
    context = {
            'project': project
    }
    return render(request, 'rfqsite/edit_active_rate.html', context)

def edit_active_rate_confirm(request):
    if request.method == 'POST':
        editAR = Active_Rate.objects.get(pk=RFQ.objects.get(pk=tracker_no))
        edit.save()
        return redirect('/part_table/'+tracker_no)







































def add_child(request):
    project = []
    context = {
        'project': project
    }
    return render(request, 'rfqsite/add_child.html', context)

def edit_ctpp(request):
    projects = []
    context = {
        'projects': projects
    }
    return render(request, 'rfqsite/edit_ctpp.html', context)

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

def edit_msut(request):
    projects = []
    context = {
        'projects': projects
    }
    return render(request, 'rfqsite/edit_msut.html', context)

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



def edit_sp_rate(request):
    projects = []
    context = {
        'projects': projects
    }
    return render(request, 'rfqsite/edit_sp_rate.html', context)

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
