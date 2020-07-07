from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import RFQ, Part_Header, Active_Rate, SP_Rate, Forecast, SPS, Material, MSUT, CTPP, Part_Costing
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
        newForecast = Forecast(sl_no=newPart,forecast_current_year=timezone.now())
        newSPS = SPS(sl_no=newPart)
        newMaterial = Material(sl_no=newPart)
        newMSUT = MSUT(sl_no=newPart)
        newCTPP = CTPP(sl_no=newPart)
        newPart_Costing = Part_Costing(sl_no=newPart)
        newPart.save()
        newForecast.save()
        newSPS.save()
        newMaterial.save()
        newMSUT.save()
        newCTPP.save()
        newPart_Costing.save()
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
        folder = "rfq/"+tracker_no+"/"
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
    tracker_no = RFQ.objects.get(pk=tracker_no).tracker_no
    active_rate = Active_Rate.objects.get(tracker_no=RFQ.objects.get(tracker_no=tracker_no))
    print(active_rate.cla)
    context = {
            'tracker_no': tracker_no,
            'active_rate': active_rate
    }
    return render(request, 'rfqsite/edit_active_rate.html', context)

def edit_active_rate_confirm(request):
    if request.method == 'POST':
        tracker_no = request.POST.get('tracker-no')
        editAR = Active_Rate.objects.get(tracker_no=RFQ.objects.get(tracker_no=tracker_no))
        editAR.cla = request.POST.get('rate-cla')
        editAR.bta = request.POST.get('rate-bta')
        editAR.tma = request.POST.get('rate-tma')
        editAR.mca3axis = request.POST.get('rate-mca3axis')
        editAR.mca4axis = request.POST.get('rate-mca4axis')
        editAR.hmc = request.POST.get('rate-hmc')
        editAR.axis5 = request.POST.get('rate-5axis')
        editAR.edm = request.POST.get('rate-edm')
        editAR.grinding = request.POST.get('rate-grinding')
        editAR.deburring = request.POST.get('rate-deburring')
        editAR.inspection = request.POST.get('rate-inspection')
        editAR.save()
        return redirect('/part_table/'+tracker_no)

def edit_sp_rate(request, tracker_no):
    tracker_no = RFQ.objects.get(pk=tracker_no).tracker_no
    sp_rate = SP_Rate.objects.get(tracker_no=RFQ.objects.get(tracker_no=tracker_no))
    context = {
            'tracker_no': tracker_no,
            'sp_rate': sp_rate
    }
    return render(request, 'rfqsite/edit_sp_rate.html', context)

def edit_sp_rate_confirm(request):
    if request.method == 'POST':
        tracker_no = request.POST.get('tracker-no')
        editSPR = SP_Rate.objects.get(tracker_no=RFQ.objects.get(tracker_no=tracker_no))
        editSPR.fpi = request.POST.get('rate-fpi')
        editSPR.mpi = request.POST.get('rate-mpi')
        editSPR.passivation = request.POST.get('rate-passivation')
        editSPR.caa = request.POST.get('rate-caa')
        editSPR.saa = request.POST.get('rate-saa')
        editSPR.hard_anodizing = request.POST.get('rate-hard-anodizing')
        editSPR.dfl = request.POST.get('rate-dfl')
        editSPR.paint = request.POST.get('rate-paint')
        editSPR.cadmium_plating = request.POST.get('rate-cadmium-plating')
        editSPR.chrome_plating = request.POST.get('rate-chrome-plating')
        editSPR.heat_treatment = request.POST.get('rate-heat-treatment')
        editSPR.save()
        return redirect('/part_table/'+tracker_no)

def part_info(request, sl_no):
    part = Part_Header.objects.get(pk=sl_no)
    forecast = Forecast.objects.get(sl_no=part)
    material = Material.objects.get(sl_no=part)
    sps = SPS.objects.get(sl_no=part)
    msut = MSUT.objects.get(sl_no=part)
    ctpp = CTPP.objects.get(sl_no=part)
    part_costing = Part_Costing.objects.get(sl_no=part)
    active_rate = Active_Rate.objects.get(tracker_no=part.tracker_no)
    sp_rate = SP_Rate.objects.get(tracker_no=part.tracker_no)
    context = {
        'part': part,
        'forecast': forecast,
        'material': material,
        'sps': sps,
        'msut': msut,
        'ctpp': ctpp,
        'part_costing': part_costing,
        'active_rate': active_rate,
        'sp_rate': sp_rate
    }
    return render(request, 'rfqsite/part_info.html', context)

def edit_part_info(request, sl_no):
    part = Part_Header.objects.get(sl_no=sl_no)
    context = {
            'part': part
    }
    return render(request, 'rfqsite/edit_part_info.html', context)


def edit_part_info_confirm(request):
    sl_no = request.POST.get('sl-no')
    if request.method == 'POST':
        editPart = Part_Header.objects.get(sl_no=sl_no)
        editPart.no = request.POST.get('part-no')
        editPart.name = request.POST.get('part-name')
        editPart.program = request.POST.get('program')
        editPart.save()
    if request.FILES:
        files = []
        for key in request.FILES:
            files.append(key)
        if 'file' in files:
            file = request.FILES['file']
            fs = FileSystemStorage()
            folder = "part/"+sl_no+"/"
            path = folder+file.name
            filename = fs.save(path, file)
            editPart = Part_Header.objects.get(sl_no=sl_no)
            editPart.file_path = path
            editPart.save()
        if 'image' in files:
            file = request.FILES['image']
            fs = FileSystemStorage()
            folder = "image/"+sl_no+"/"
            path = folder+file.name
            filename = fs.save(path, file)
            editPart = Part_Header.objects.get(sl_no=sl_no)
            editPart.image_path = path
            editPart.save()
    return redirect('/part_info/'+str(sl_no))

def edit_forecast(request, sl_no):
    forecast = Forecast.objects.get(sl_no=Part_Header.objects.get(pk=sl_no))
    part = Part_Header.objects.get(pk=sl_no)
    context = {
        'part': part,
        'forecast': forecast
    }
    return render(request, 'rfqsite/edit_forecast.html', context)

def edit_forecast_confirm(request):
    sl_no = request.POST.get('sl-no')
    if request.method == 'POST':
        editForecast = Forecast.objects.get(sl_no=Part_Header.objects.get(pk=sl_no))
        editForecast.qty_per_unit = request.POST.get('qty-per-unit')
        editForecast.forecast_year1 = request.POST.get('forecast-year1')
        editForecast.forecast_year2 = request.POST.get('forecast-year2')
        editForecast.forecast_year3 = request.POST.get('forecast-year3')
        editForecast.forecast_year4 = request.POST.get('forecast-year4')
        editForecast.forecast_year5 = request.POST.get('forecast-year5')
        editForecast.save()
    return redirect('/part_info/'+sl_no)

def edit_ctpp(request, sl_no):
    ctpp = CTPP.objects.get(sl_no=Part_Header.objects.get(pk=sl_no))
    part = Part_Header.objects.get(pk=sl_no)
    context = {
        'part': part,
        'ctpp': ctpp
    }
    return render(request, 'rfqsite/edit_ctpp.html', context)

def to_float(s):
    s = s.strip()
    return float(s) if s else None

def edit_ctpp_confirm(request):
    sl_no = request.POST.get('sl-no')
    if request.method == 'POST':
        editCtpp = CTPP.objects.get(sl_no=Part_Header.objects.get(pk=sl_no))
        editCtpp.cla = to_float(request.POST.get('ctpp-cla'))
        editCtpp.bta = to_float(request.POST.get('ctpp-bta'))
        editCtpp.tma = to_float(request.POST.get('ctpp-tma'))
        editCtpp.mca3axis = to_float(request.POST.get('ctpp-mca3axis'))
        editCtpp.mca4axis = to_float(request.POST.get('ctpp-mca4axis'))
        editCtpp.hmc = to_float(request.POST.get('ctpp-hmc'))
        editCtpp.axis5 = to_float(request.POST.get('ctpp-5axis'))
        editCtpp.edm = to_float(request.POST.get('ctpp-edm'))
        editCtpp.grinding = to_float(request.POST.get('ctpp-grinding'))
        editCtpp.inspection = to_float(request.POST.get('ctpp-inspection'))
        editCtpp.deburring = to_float(request.POST.get('ctpp-deburring'))
        editCtpp.assembly = to_float(request.POST.get('ctpp-assembly'))
        editCtpp.lapping = to_float(request.POST.get('ctpp-lapping'))
        editCtpp.save()
    return redirect('/part_info/'+sl_no)

def edit_sps(request, sl_no):
    sps = SPS.objects.get(sl_no=Part_Header.objects.get(pk=sl_no))
    part = Part_Header.objects.get(pk=sl_no)
    context = {
        'part': part,
        'sps': sps
    }
    return render(request, 'rfqsite/edit_sps.html', context)

def edit_sps_confirm(request):
    sl_no = request.POST.get('sl-no')
    if request.method == 'POST':
        editsps = SPS.objects.get(sl_no=Part_Header.objects.get(pk=sl_no))
        editsps.surface_treatment = request.POST.get('sps-surface-treatment')
        editsps.ht = request.POST.get('sps-ht')
        editsps.fpi = request.POST.get('sps-fpi')
        editsps.mpi = request.POST.get('sps-mpi')
        editsps.primer = request.POST.get('sps-primer')
        editsps.solid_film = request.POST.get('sps-solid-film')
        editsps.pmr = request.POST.get('sps-pmr')
        editsps.save()
    return redirect('/part_info/'+sl_no)

def edit_msut(request, sl_no):
    msut = MSUT.objects.get(sl_no=Part_Header.objects.get(pk=sl_no))
    part = Part_Header.objects.get(pk=sl_no)
    context = {
        'part': part,
        'msut': msut
    }
    return render(request, 'rfqsite/edit_msut.html', context)

def edit_msut_confirm(request):
    sl_no = request.POST.get('sl-no')
    if request.method == 'POST':
        editmsut = MSUT.objects.get(sl_no=Part_Header.objects.get(pk=sl_no))
        editmsut.cla = to_float(request.POST.get('msut-cla'))
        editmsut.bta = to_float(request.POST.get('msut-bta'))
        editmsut.tma = to_float(request.POST.get('msut-tma'))
        editmsut.mca3axis = to_float(request.POST.get('msut-mca3axis'))
        editmsut.mca4axis = to_float(request.POST.get('msut-mca4axis'))
        editmsut.hmc = to_float(request.POST.get('msut-hmc'))
        editmsut.axis5 = to_float(request.POST.get('msut-5axis'))
        editmsut.edm = to_float(request.POST.get('msut-edm'))
        editmsut.grinding = to_float(request.POST.get('msut-grinding'))
        editmsut.save()
    return redirect('/part_info/'+sl_no)


def edit_part_costing(request, sl_no):
    part_costing = Part_Costing.objects.get(sl_no=Part_Header.objects.get(pk=sl_no))
    part = Part_Header.objects.get(pk=sl_no)
    context = {
        'part': part,
        'part_costing': part_costing
    }
    return render(request, 'rfqsite/edit_part_costing.html', context)

def edit_part_costing_confirm(request):
    sl_no = request.POST.get('sl-no')
    if request.method == 'POST':
        editpc = Part_Costing.objects.get(sl_no=Part_Header.objects.get(pk=sl_no))
        editpc.base_material_price = to_float(request.POST.get('base-material-price'))
        editpc.material_shipping_cost = to_float(request.POST.get('material-shipping-cost'))
        editpc.nre_amortizing_cost = to_float(request.POST.get('nre-amortizing-cost'))
        editpc.target_price = to_float(request.POST.get('target-price'))
        editpc.ebq_customer_qty = to_float(request.POST.get('ebq-customer-qty'))
        editpc.otspsuc = to_float(request.POST.get('otspsuc'))
        editpc.otrmac = to_float(request.POST.get('otrmac'))
        editpc.ottc = to_float(request.POST.get('ottc'))
        editpc.hardware_supplier = request.POST.get('hardware-supplier')
        editpc.material_supplier = request.POST.get('material-supplier')
        editpc.ccs_quote_assumptions = request.POST.get('ccs-quote-assumptions')
        editpc.dltiw_fai = request.POST.get('dltiw-fai')
        editpc.dltiw_serial_production = request.POST.get('dltiw-serial-production')
        editpc.dltiw_production = request.POST.get('dltiw-production')
        editpc.save()
    return redirect('/part_info/'+sl_no)

def add_child(request, sl_no):
    part = Part_Header.objects.get(pk=sl_no)
    project = part.tracker_no
    child_level = part.level + 1
    context = {
            'project': project,
            'part': part,
            'child_level': child_level
    }
    return render(request, 'rfqsite/add_child.html', context)

def add_child_confirm(request):
    if request.method == 'POST':
        sl_no = request.POST.get('sl-no')
        tracker_no = request.POST.get('tracker-no')
        parent_sl_no = request.POST.get('parent-sl-no')
        part_level = request.POST.get('part-level')
        part_no = request.POST.get('part-no')
        part_name = request.POST.get('part-name')
        program = request.POST.get('program')
        fco = Forecast.objects.get(sl_no=Part_Header.objects.get(pk=sl_no))
        newPart = Part_Header(tracker_no=RFQ.objects.get(tracker_no=tracker_no),level=part_level,no=part_no,name=part_name,program=program, parent_sl_no=Part_Header.objects.get(pk=sl_no))
        newForecast = Forecast(sl_no=newPart,forecast_current_year=timezone.now(), forecast_year1=fco.forecast_year1, forecast_year2=fco.forecast_year2, forecast_year3=fco.forecast_year3, forecast_year4=fco.forecast_year4, forecast_year5=fco.forecast_year5)
        newSPS = SPS(sl_no=newPart)
        newMaterial = Material(sl_no=newPart)
        newMSUT = MSUT(sl_no=newPart)
        newCTPP = CTPP(sl_no=newPart)
        newPart_Costing = Part_Costing(sl_no=newPart)
        newPart.save()
        newForecast.save()
        newSPS.save()
        newMaterial.save()
        newMSUT.save()
        newCTPP.save()
        newPart_Costing.save()
        return redirect('/part_table/'+tracker_no)

















def edit_material(request):
    projects = []
    context = {
        'projects': projects
    }
    return render(request, 'rfqsite/edit_material.html', context)
