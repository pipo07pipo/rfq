from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from .models import RFQ, Part_Header, Burden_Rate, Active_Rate, Forecast, Material, MSUT, CTPP, Part_Costing, Hardware, Output, Roles, ExtendUser, SP_Master, SP_Set, MC_Master
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
import json, re

@login_required(login_url='/login')
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
    for tracker in active_project:
        active_rate = Active_Rate(tracker_no=RFQ.objects.get(tracker_no=tracker))
        active_rate.save()
    return render(request, 'rfqsite/index.html', context)

@login_required(login_url='/login')
def parts(request, tracker_no):
    project = RFQ.objects.get(pk=tracker_no)
    if(len(project.file_path.split('/')) == 3 ):
        file_name = project.file_path.split('/')[2]
    else:
        file_name = ''
    parts = [part for part in Part_Header.objects.filter(tracker_no=tracker_no,level=0)]

    context = {
        'project': project,
        'parts': parts,
        'file_name': file_name
    }
    return render(request, 'rfqsite/part_table.html', context)

@login_required(login_url='/login')
def rfq_summary(request, tracker_no):
    project = RFQ.objects.get(pk=tracker_no)
    total_cost_td = 0
    mtl_cost_td = 0
    spl_process_cost_td = 0
    total_hardware_cost_td = 0
    total_machine_cost_td = 0
    mcrftp_cla_t = 0
    mcrftp_bta_t = 0
    mcrftp_tma_t = 0
    mcrftp_mca3axis_t = 0
    mcrftp_mca4axis_t = 0
    mcrftp_hmc_t = 0
    mcrftp_5axis_t = 0
    mcrftp_edm_t = 0
    mcrftp_grinding_t = 0
    all_part = Part_Header.objects.filter(tracker_no=project)
    for item in all_part:
        op = Output.objects.get(sl_no=item)
        total_cost_td += op.total_cost
        mtl_cost_td += op.mtl_cost
        spl_process_cost_td += op.spl_process_cost
        total_hardware_cost_td += op.total_hardware_cost
        total_machine_cost_td += op.total_machine_cost
        mcrftp_cla_t += op.mcrftp_cla
        mcrftp_bta_t += op.mcrftp_bta
        mcrftp_tma_t += op.mcrftp_tma
        mcrftp_mca3axis_t += op.mcrftp_mca3axis
        mcrftp_mca4axis_t += op.mcrftp_mca4axis
        mcrftp_hmc_t += op.mcrftp_hmc
        mcrftp_5axis_t += op.mcrftp_5axis
        mcrftp_edm_t += op.mcrftp_edm
        mcrftp_grinding_t += op.mcrftp_grinding
    context = {
        'project': project,
        'total_cost_td': total_cost_td,
        'mtl_cost_td': mtl_cost_td,
        'spl_process_cost_td': spl_process_cost_td,
        'total_hardware_cost_td': total_hardware_cost_td,
        'total_machine_cost_td': total_machine_cost_td,
        'mcrftp_cla_t': mcrftp_cla_t,
        'mcrftp_bta_t': mcrftp_bta_t,
        'mcrftp_tma_t': mcrftp_tma_t,
        'mcrftp_mca3axis_t': mcrftp_mca3axis_t,
        'mcrftp_mca4axis_t': mcrftp_mca4axis_t,
        'mcrftp_hmc_t': mcrftp_hmc_t,
        'mcrftp_5axis_t': mcrftp_5axis_t,
        'mcrftp_edm_t': mcrftp_edm_t,
        'mcrftp_grinding_t': mcrftp_grinding_t
    }
    return render(request, 'rfqsite/rfq_summary.html', context)

@login_required(login_url='/login')
def add_part(request, tracker_no):
    if(get_perm(request.user) > 1):
        return HttpResponseNotFound("Access Denied")
    project = RFQ.objects.get(pk=tracker_no)
    context = {
        'project': project
    }
    return render(request, 'rfqsite/add_part.html', context)


@login_required(login_url='/login')
def add_part_multi(request, tracker_no):
    if(get_perm(request.user) > 1):
        return HttpResponseNotFound("Access Denied")
    project = RFQ.objects.get(pk=tracker_no)
    context = {
        'project': project
    }
    return render(request, 'rfqsite/add_part_multi.html', context)


#725Z2463-101	FCL_CLEVIS_OIL-TANK-ACCESS-DOOR ASSY.	101	101	101	101	101
#725Z2463-111	FCL_CLEVIS_OIL-TANK-ACCESS-DOOR	101	101	101	101	101
#NAS77C4-014	BUSH	101	101	101	101	101
@login_required(login_url='/login')
def add_part_multi_confirm(request):
    if request.method == 'POST':
        tracker_no = request.POST.get('tracker-no')
        part_level = request.POST.get('part-level')
        excel = request.POST.get('excel-data')
        trans = re.split('	|\r\n',excel)
        if(len(trans)%7 != 0):
            return redirect('/part_table/'+request.POST.get('tracker-no')+"?message=0")
        for i in range(0, len(trans), 7):
            try:
                trans[i] = str(trans[i])
                trans[i+1] = str(trans[i+1])
                trans[i+2] = int(trans[i+2].replace(',',''))
                trans[i+3] = int(trans[i+3].replace(',',''))
                trans[i+4] = int(trans[i+4].replace(',',''))
                trans[i+5] = int(trans[i+5].replace(',',''))
                trans[i+6] = int(trans[i+6].replace(',',''))
            except:
                return redirect('/part_table/'+request.POST.get('tracker-no')+"?message=0")
        for i in range(0, len(trans), 7):
            newPart = Part_Header(tracker_no=RFQ.objects.get(tracker_no=tracker_no),level=part_level,no=trans[i],name=trans[i+1])
            newForecast = Forecast(sl_no=newPart)
            newForecast.forecast_year1 = trans[i+2]
            newForecast.forecast_year2 = trans[i+3]
            newForecast.forecast_year3 = trans[i+4]
            newForecast.forecast_year4 = trans[i+5]
            newForecast.forecast_year5 = trans[i+6]
            newMaterial = Material(sl_no=newPart)
            newMSUT = MSUT(sl_no=newPart)
            newCTPP = CTPP(sl_no=newPart)
            newPart_Costing = Part_Costing(sl_no=newPart)
            newBR = Burden_Rate(sl_no=newPart)
            newHW = Hardware(sl_no=newPart)
            newO = Output(sl_no=newPart)
            newPart.save()
            newForecast.save()
            newMaterial.save()
            newMSUT.save()
            newCTPP.save()
            newPart_Costing.save()
            newBR.save()
            newHW.save()
            newO.save()
        return redirect('/part_table/'+request.POST.get('tracker-no')+"?message=1")

@login_required(login_url='/login')
def add_part_confirm(request):
    if request.method == 'POST':
        tracker_no = request.POST.get('tracker-no')
        part_level = request.POST.get('part-level')
        part_no = request.POST.get('part-no')
        part_name = request.POST.get('part-name')
        program = request.POST.get('program')
        newPart = Part_Header(tracker_no=RFQ.objects.get(tracker_no=tracker_no),level=part_level,no=part_no,name=part_name,program=program)
        newForecast = Forecast(sl_no=newPart)
        newMaterial = Material(sl_no=newPart)
        newMSUT = MSUT(sl_no=newPart)
        newCTPP = CTPP(sl_no=newPart)
        newPart_Costing = Part_Costing(sl_no=newPart)
        newBR = Burden_Rate(sl_no=newPart)
        newHW = Hardware(sl_no=newPart)
        newO = Output(sl_no=newPart)
        newPart.save()
        newForecast.save()
        newMaterial.save()
        newMSUT.save()
        newCTPP.save()
        newPart_Costing.save()
        newBR.save()
        newHW.save()
        newO.save()
        return redirect('/part_table/'+tracker_no+"?message=1")

@login_required(login_url='/login')
def edit_rfq(request, tracker_no):
    if(get_perm(request.user) > 1):
        return HttpResponseNotFound("Access Denied")
    project = RFQ.objects.get(pk=tracker_no)
    if(len(project.file_path.split('/')) == 3 ):
        file_name = project.file_path.split('/')[2]
    else:
        file_name = ''
    context = {
            'project': project,
            'file_name': file_name
    }
    return render(request, 'rfqsite/edit_rfq.html', context)

@login_required(login_url='/login')
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
        project.usd_thb = request.POST.get('usd-thb')
        project.current_year = request.POST.get('current-year')
        project.save()
        return redirect('/part_table/'+tracker_no+"?message=1")
    elif request.method == 'POST':
        tracker_no = request.POST.get('tracker-no')
        project = RFQ.objects.get(pk=tracker_no)
        project.customer_name = request.POST.get('customer-name')
        project.usd_thb = request.POST.get('usd-thb')
        project.current_year = request.POST.get('current-year')
        project.save()
        return redirect('/part_table/'+tracker_no+"?message=1")

@login_required(login_url='/login')
def edit_active_rate(request, tracker_no):
    if(get_perm(request.user) > 1):
        return HttpResponseNotFound("Access Denied")
    tracker_no = RFQ.objects.get(pk=tracker_no).tracker_no
    active_rate = Active_Rate.objects.get(tracker_no=RFQ.objects.get(tracker_no=tracker_no))
    print(active_rate.cla)
    context = {
            'tracker_no': tracker_no,
            'active_rate': active_rate
    }
    return render(request, 'rfqsite/edit_active_rate.html', context)

@login_required(login_url='/login')
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
        return redirect('/part_table/'+tracker_no+"?message=1")




@login_required(login_url='/login')
def part_info(request, sl_no):
    part = Part_Header.objects.get(pk=sl_no)
    current_year = part.tracker_no.current_year
    base_level = Part_Header.objects.get(pk=sl_no)
    while(base_level.level > 0):
        base_level = base_level.parent_sl_no
    tree = Part_Tree(base_level,part)
    tree.set_tree()
    tree.set_open()
    parts = [tree]
    forecast = Forecast.objects.get(sl_no=part)
    material = Material.objects.get(sl_no=part)
    msut = MSUT.objects.get(sl_no=part)
    ctpp = CTPP.objects.get(sl_no=part)
    part_costing = Part_Costing.objects.get(sl_no=part)
    active_rate = Active_Rate.objects.get(tracker_no=part.tracker_no)
    burden_rate = Burden_Rate.objects.get(sl_no=part)
    hardware = Hardware.objects.get(sl_no=part)
    sp_set = SP_Set.objects.filter(sl_no=part).order_by('sp_id')
    sum_child = 0
    fchild = Part_Header.objects.filter(parent_sl_no=part)
    child = [x for x in fchild]
    while(len(child) > 0):
        newChild = []
        for item in child:
            op = Output.objects.get(sl_no=item)
            sum_child += op.ccs_ewp
            addChild = [x for x in Part_Header.objects.filter(parent_sl_no=item)]
            for c in addChild:
                 newChild.append(c)
        child = newChild
    if(len(part.file_path.split('/')) == 3 ):
        file_name = part.file_path.split('/')[2]
    else:
        file_name = ''
    context = {
        'sp_set': sp_set,
        'current_year': current_year,
        'part': part,
        'parts': parts,
        'forecast': forecast,
        'material': material,
        'msut': msut,
        'ctpp': ctpp,
        'part_costing': part_costing,
        'active_rate': active_rate,
        'burden_rate': burden_rate,
        'hardware': hardware,
        'sum_child': sum_child,
        'file_name': file_name
    }
    return render(request, 'rfqsite/part_info.html', context)

@login_required(login_url='/login')
def edit_part_info(request, sl_no):
    if(get_perm(request.user) > 1):
        return HttpResponseNotFound("Access Denied")
    part = Part_Header.objects.get(sl_no=sl_no)
    if(len(part.image_path.split('/')) == 3 ):
        image_name = part.image_path.split('/')[2]
    else:
        image_name = ''
    if(len(part.file_path.split('/')) == 3 ):
        file_name = part.file_path.split('/')[2]
    else:
        file_name = ''
    context = {
            'part': part,
            'file_name': file_name,
            'image_name': image_name,
    }
    return render(request, 'rfqsite/edit_part_info.html', context)

@login_required(login_url='/login')
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
    return redirect('/part_info/'+str(sl_no)+"?message=1")

@login_required(login_url='/login')
def edit_forecast(request, sl_no):
    if(get_perm(request.user) > 1):
        return HttpResponseNotFound("Access Denied")
    forecast = Forecast.objects.get(sl_no=Part_Header.objects.get(pk=sl_no))
    part = Part_Header.objects.get(pk=sl_no)
    current_year = part.tracker_no.current_year
    context = {
        'current_year': current_year,
        'part': part,
        'forecast': forecast
    }
    return render(request, 'rfqsite/edit_forecast.html', context)

@login_required(login_url='/login')
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
        editForecast.aeqfc = request.POST.get('aeqfc')
        editForecast.save()
    return redirect('/part_info/'+sl_no+"?message=1")

@login_required(login_url='/login')
def edit_ctpp(request, sl_no):
    if(get_perm(request.user) > 1):
        return HttpResponseNotFound("Access Denied")
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

@login_required(login_url='/login')
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
    return redirect('/part_info/'+sl_no+"?message=1")


@login_required(login_url='/login')
def edit_msut(request, sl_no):
    if(get_perm(request.user) > 1):
        return HttpResponseNotFound("Access Denied")
    msut = MSUT.objects.get(sl_no=Part_Header.objects.get(pk=sl_no))
    part = Part_Header.objects.get(pk=sl_no)
    context = {
        'part': part,
        'msut': msut
    }
    return render(request, 'rfqsite/edit_msut.html', context)

@login_required(login_url='/login')
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
        return redirect('/part_info/'+sl_no+"?message=1")


@login_required(login_url='/login')
def edit_hardware(request, sl_no):
    if(get_perm(request.user) > 1):
        return HttpResponseNotFound("Access Denied")
    hardware = Hardware.objects.get(sl_no=Part_Header.objects.get(pk=sl_no))
    part = Part_Header.objects.get(pk=sl_no)
    context = {
        'part': part,
        'hardware': hardware
    }
    return render(request, 'rfqsite/edit_hardware.html', context)

@login_required(login_url='/login')
def edit_hardware_confirm(request):
    sl_no = request.POST.get('sl-no')
    if request.method == 'POST':
        edithw = Hardware.objects.get(sl_no=Part_Header.objects.get(pk=sl_no))
        edithw.description = request.POST.get('hardware-description')
        edithw.supplier = request.POST.get('hardware-supplier')
        edithw.price = to_float(request.POST.get('hardware-price'))
        edithw.qty = to_float(request.POST.get('hardware-qty'))
        edithw.save()
        return redirect('/part_info/'+sl_no+"?message=1")

@login_required(login_url='/login')
def edit_part_costing(request, sl_no):
    if(get_perm(request.user) > 1):
        return HttpResponseNotFound("Access Denied")
    part_costing = Part_Costing.objects.get(sl_no=Part_Header.objects.get(pk=sl_no))
    part = Part_Header.objects.get(pk=sl_no)
    context = {
        'part': part,
        'part_costing': part_costing
    }
    return render(request, 'rfqsite/edit_part_costing.html', context)

@login_required(login_url='/login')
def edit_part_costing_confirm(request):
    sl_no = request.POST.get('sl-no')
    if request.method == 'POST':
        editpc = Part_Costing.objects.get(sl_no=Part_Header.objects.get(pk=sl_no))
        editpc.total_nre_cost = to_float(request.POST.get('total-nre-cost'))
        editpc.target_price = to_float(request.POST.get('target-price'))
        editpc.ebq_customer_qty = to_float(request.POST.get('ebq-customer-qty'))
        editpc.otspsuc = to_float(request.POST.get('otspsuc'))
        editpc.otrmac = to_float(request.POST.get('otrmac'))
        editpc.ottc = to_float(request.POST.get('ottc'))
        editpc.ccs_quote_assumptions = request.POST.get('ccs-quote-assumptions')
        editpc.dltiw_fai = request.POST.get('dltiw-fai')
        editpc.dltiw_serial_production = request.POST.get('dltiw-serial-production')
        editpc.dltiw_production = request.POST.get('dltiw-production')
        editpc.base_subcontract = to_float(request.POST.get('base-subcontract'))
        editpc.shipping_cost = to_float(request.POST.get('shipping-cost'))
        editpc.ebq_ccs_qty = to_float(request.POST.get('ebq-ccs-qty'))
        editpc.save()
        return redirect('/part_info/'+sl_no+"?message=1")

@login_required(login_url='/login')
def add_child(request, sl_no):
    if(get_perm(request.user) > 1):
        return HttpResponseNotFound("Access Denied")
    part = Part_Header.objects.get(pk=sl_no)
    project = part.tracker_no
    child_level = part.level + 1
    context = {
            'project': project,
            'part': part,
            'child_level': child_level
    }
    return render(request, 'rfqsite/add_child.html', context)

@login_required(login_url='/login')
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
        type = request.POST.get('type')
        newPart = Part_Header(type=type,tracker_no=RFQ.objects.get(tracker_no=tracker_no),level=part_level,no=part_no,name=part_name,program=program, parent_sl_no=Part_Header.objects.get(pk=sl_no))
        newForecast = Forecast(sl_no=newPart, forecast_year1=fco.forecast_year1, forecast_year2=fco.forecast_year2, forecast_year3=fco.forecast_year3, forecast_year4=fco.forecast_year4, forecast_year5=fco.forecast_year5)
        newMaterial = Material(sl_no=newPart)
        newMSUT = MSUT(sl_no=newPart)
        newCTPP = CTPP(sl_no=newPart)
        newPart_Costing = Part_Costing(sl_no=newPart)
        newBR = Burden_Rate(sl_no=newPart)
        newHW = Hardware(sl_no=newPart)
        newO = Output(sl_no=newPart)
        newPart.save()
        newForecast.save()
        newMaterial.save()
        newMSUT.save()
        newCTPP.save()
        newPart_Costing.save()
        newBR.save()
        newHW.save()
        newO.save()
        return redirect('/part_info/'+sl_no+"?message=1")

@login_required(login_url='/login')
def edit_material(request, sl_no):
    if(get_perm(request.user) > 1):
        return HttpResponseNotFound("Access Denied")
    material = Material.objects.get(sl_no=Part_Header.objects.get(pk=sl_no))
    part = Part_Header.objects.get(pk=sl_no)
    context = {
        'part': part,
        'material': material
    }
    return render(request, 'rfqsite/edit_material.html', context)

def clean_material(material):
    material.description = ''
    material.cross_section = ''
    material.type = ''
    material.quantity = 1
    material.rm_density = 0
    material.rm_density_unit = ''
    material.rm_d1 = 0
    material.rm_d1_unit = ''
    material.rm_d2 = 0
    material.rm_d2_unit = ''
    material.rm_t = 0
    material.rm_t_unit = ''
    material.rm_w = 0
    material.rm_w_unit = ''
    material.rm_l = 0
    material.rm_l_unit = ''
    material.rm_total_weight = 0
    material.supplier = ''
    material.base_material_price = 0
    material.shipping_cost = 0
    material.fpwp = 0
    material.armwpp = 0
    material.save()

def to_str(str):
    if str == None:
        return ''
    else:
        return str

@login_required(login_url='/login')
def edit_material_confirm(request):
    sl_no = request.POST.get('sl-no')
    if request.method == 'POST':
        editmat = Material.objects.get(sl_no=Part_Header.objects.get(pk=sl_no))
        clean_material(editmat)
        type = request.POST.get('cross-section')
        editmat.description = to_str(request.POST.get('description'))
        if(request.POST.get('check-armwpp') == None):
            editmat.cross_section = to_str(request.POST.get('cross-section'))
            editmat.type = to_str(request.POST.get('type'))
            editmat.quantity = to_float(request.POST.get('quantity'))
            editmat.rm_density = to_float(request.POST.get('density'))
            editmat.rm_density_unit = request.POST.get('density-unit')
            editmat.rm_total_weight = request.POST.get('rm-total-weight')
        if(request.POST.get('check-armwpp') != None):
            editmat.armwpp = to_float(request.POST.get('armwpp'))
        elif(type == "Round Bar Shape"):
            #D1,L
            editmat.rm_d1 = to_float(request.POST.get('rm-d1'))
            editmat.rm_d1_unit = request.POST.get('rm-d1-unit')
            editmat.rm_l = to_float(request.POST.get('rm-l'))
            editmat.rm_l_unit = request.POST.get('rm-l-unit')
        elif(type == "Tube Shape"):
            #D1,D2,L
            editmat.rm_d1 = to_float(request.POST.get('rm-d1'))
            editmat.rm_d1_unit = request.POST.get('rm-d1-unit')
            editmat.rm_d2 = to_float(request.POST.get('rm-d2'))
            editmat.rm_d2_unit = request.POST.get('rm-d2-unit')
            editmat.rm_l = to_float(request.POST.get('rm-l'))
            editmat.rm_l_unit = request.POST.get('rm-l-unit')
        elif(type == "Flat Bar / Plate / Sheet"):
            #T,W,L
            editmat.rm_t = to_float(request.POST.get('rm-t'))
            editmat.rm_t_unit = request.POST.get('rm-t-unit')
            editmat.rm_w = to_float(request.POST.get('rm-w'))
            editmat.rm_w_unit = request.POST.get('rm-w-unit')
            editmat.rm_l = to_float(request.POST.get('rm-l'))
            editmat.rm_l_unit = request.POST.get('rm-l-unit')
        editmat.supplier = request.POST.get('material-supplier')
        editmat.base_material_price = to_float(request.POST.get('base-material-price'))
        editmat.shipping_cost = to_float(request.POST.get('material-shipping-cost'))
        editmat.fpwp = to_float(request.POST.get('fpwp'))
        editmat.save()

        editmat.armwpp = to_float(request.POST.get('armwpp'))
    return redirect('/part_info/'+sl_no+"?message=1")

@login_required(login_url='/login')
def edit_material_remove(request, sl_no):
    if(get_perm(request.user) > 1):
        return HttpResponseNotFound("Access Denied")
    delmat = Material.objects.get(sl_no=Part_Header.objects.get(pk=sl_no))
    clean_material(delmat)
    delmat.save()
    return redirect('/part_info/'+str(sl_no))

@login_required(login_url='/login')
def edit_burden_rate(request, sl_no):
    if(get_perm(request.user) > 1):
        return HttpResponseNotFound("Access Denied")
    burden_rate = Burden_Rate.objects.get(sl_no=Part_Header.objects.get(pk=sl_no))
    part = Part_Header.objects.get(pk=sl_no)
    context = {
            'part': part,
            'burden_rate': burden_rate
    }
    return render(request, 'rfqsite/edit_burden_rate.html', context)

@login_required(login_url='/login')
def edit_burden_rate_confirm(request):
    sl_no = request.POST.get('sl-no')
    if request.method == 'POST':
        editbd = Burden_Rate.objects.get(sl_no=Part_Header.objects.get(pk=sl_no))
        editbd.material = to_float(request.POST.get('rate-material'))
        editbd.hardware = to_float(request.POST.get('rate-hardware'))
        editbd.subcontract = to_float(request.POST.get('rate-subcontract'))
        editbd.sp = to_float(request.POST.get('rate-sp'))
        editbd.save()
    return redirect('/part_info/'+sl_no+"?message=1")

def unNan(data):
    if(data == 'NaN' or data == ''):
        return 0
    else:
        return data

@login_required(login_url='/login')
def data_collect(request):
    if request.method == 'GET':
        sl_no = request.GET.get('sl_no')
        editO = Output.objects.get(sl_no=Part_Header.objects.get(pk=sl_no))
        editO.ccs_ewp = unNan(request.GET.get('ccs_ewp'))
        editO.total_cost = unNan(request.GET.get('total_cost'))
        editO.mtl_cost = unNan(request.GET.get('mtl_cost'))
        editO.spl_process_cost = unNan(request.GET.get('spl_process_cost'))
        editO.total_hardware_cost = unNan(request.GET.get('total_hardware_cost'))
        editO.total_machine_cost = unNan(request.GET.get('total_machine_cost'))
        editO.mcrftp_cla = unNan(request.GET.get('mcrftp_cla'))
        editO.mcrftp_bta = unNan(request.GET.get('mcrftp_bta'))
        editO.mcrftp_tma = unNan(request.GET.get('mcrftp_tma'))
        editO.mcrftp_mca3axis = unNan(request.GET.get('mcrftp_mca3axis'))
        editO.mcrftp_mca4axis = unNan(request.GET.get('mcrftp_mca4axis'))
        editO.mcrftp_hmc = unNan(request.GET.get('mcrftp_hmc'))
        editO.mcrftp_5axis = unNan(request.GET.get('mcrftp_5axis'))
        editO.mcrftp_edm = unNan(request.GET.get('mcrftp_edm'))
        editO.mcrftp_grinding = unNan(request.GET.get('mcrftp_grinding'))
        editO.save()
    return HttpResponse("OK")

class Part_Tree:
    def __init__(self, base_level, current_level):
        self.base_level = base_level
        self.current_level = current_level
        self.sl_no = self.base_level.sl_no
        self.no = self.base_level.no
        self.name = self.base_level.name
        self.type = self.base_level.type
        self.isOpen = False
        self.children = []
    def set_tree(self):
        children = Part_Header.objects.filter(parent_sl_no=self.base_level)
        for child in children:
            pt = Part_Tree(child,self.current_level)
            self.children.append(pt)
        for child in self.children:
            child.set_tree()
    def set_open(self):
        self.isOpen = True
        poc = []
        lcl = self.current_level
        level = self.current_level.level
        while(level > 0):
            poc.append(lcl)
            lcl = lcl.parent_sl_no
            level = lcl.level
        path = self.children
        while(level < self.current_level.level):
            for child in path:
                if child.base_level in poc:
                    child.isOpen = True
                    level = child.base_level.level
                    path = child.children
                    break



#################################################################################
def get_perm(user):
    return user.extenduser.role.permission

def user_table(request):
    if(get_perm(request.user) != 0):
        return HttpResponseNotFound("Access Denied")
    users = User.objects.all()
    context = {
            'users': users
    }
    return render(request, 'rfqsite/user_table.html', context)

def add_user(request):
    if(get_perm(request.user) != 0):
        return HttpResponseNotFound("Access Denied")
    roles = Roles.objects.all()
    if request.method == 'POST':
        alluser = User.objects.all()
        for user in alluser:
            if(request.POST.get('username') == user.username):
                message = "username already exist"
                context = {
                'message': message,
                'roles': roles
                }
                return redirect('/user_table/?message=0')
            else:
                newUser = User.objects.create_user(request.POST.get('username'), '', request.POST.get('password'))
                newUser.first_name = request.POST.get('first-name')
                newUser.last_name = request.POST.get('last-name')
                role = Roles.objects.get(permission=request.POST.get('role'))
                ext = ExtendUser(user=newUser,role=role)
                ext.save()
                newUser.save()
                return redirect('/user_table/?message=1')
    else:
        context = {
                'roles': roles
        }
    return render(request, 'rfqsite/add_user.html', context)

def edit_user(request,username):
    if(get_perm(request.user) != 0):
        return HttpResponseNotFound("Access Denied")
    roles = Roles.objects.all()
    user = User.objects.get(username=username)
    context = {
        'fuser': user,
        'roles': roles
    }
    return render(request, 'rfqsite/edit_user.html', context)

def edit_user_confirm(request):
    if(get_perm(request.user) != 0):
        return HttpResponseNotFound("Access Denied")
    if request.method == 'POST':
        user = User.objects.get(username=request.POST.get('username'))
        user.first_name = username=request.POST.get('first-name')
        user.last_name = username=request.POST.get('last-name')
        if(request.POST.get('reset-password') != None):
            user.set_password(request.POST.get('password'))
        ext = ExtendUser.objects.get(user=user)
        ext.role = Roles.objects.get(permission=request.POST.get('role'))
        user.save()
        ext.save()
        return redirect('/user_table/?message=1')

def validate_user(request):
    alluser = User.objects.all()
    for user in alluser:
        if(request.GET.get('username') == user.username):
            data = {'isUsed': True}
            return JsonResponse(data)
    data = {'isUsed': False}
    return JsonResponse(data)

def remove_user(request,username):
    if(get_perm(request.user) != 0):
        return HttpResponseNotFound("Access Denied")
    duser = User.objects.get(username=username)
    duser.delete()
    return redirect('/user_table/?message=1')

def remove_part(request, sl_no):
    if(get_perm(request.user) > 1):
        return HttpResponseNotFound("Access Denied")
    dpart = Part_Header.objects.get(sl_no=sl_no)
    rfq = dpart.tracker_no
    dpart.delete()
    return redirect('/part_table/'+str(rfq.tracker_no)+'?message=1')

def master_table(request):
    sp_table = SP_Master.objects.all()
    mc_table = MC_Master.objects.all()
    context = {
        'sp_masters': sp_table,
        'mc_tables': mc_table
    }
    return render(request, 'rfqsite/master_table.html', context)

def add_mc_master(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        for obj in MC_Master.objects.filter(name=name):
            return redirect('/master_table/?message=0')
        sm = MC_Master(name=name)
        sm.save()
        return redirect('/master_table/?message=1')
    context = {
    }
    return render(request, 'rfqsite/add_mc_master.html', context)

def add_sp_master(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        for obj in SP_Master.objects.filter(name=name):
            return redirect('/master_table/?message=0')
        sm = SP_Master(name=name)
        sm.save()
        return redirect('/master_table/?message=1')
    context = {
    }
    return render(request, 'rfqsite/add_sp_master.html', context)

def set_sp(part,master):
    pass

def edit_sp_set(request,sl_no):
    part = Part_Header.objects.get(sl_no=sl_no)
    sp_set = SP_Set.objects.filter(sl_no=part).order_by('sp_id')
    context = {
            'part': part,
            'sp_set': sp_set
    }
    return render(request, 'rfqsite/edit_sp_set.html', context)

def edit_sp_set_confirm(request):
    if request.method == 'POST':
        sl_no = request.POST.get('sl-no')
        sp = SP_Set.objects.filter(sl_no=sl_no)
        for item in request.POST:
            if('sp-rate' in item):
                id = int(item.replace('sp-rate-',''))
                esp1 = SP_Set.objects.get(sl_no=sl_no,sp_id=SP_Master.objects.get(id=id))
                esp1.rate = request.POST.get(item)
                esp1.save()
            elif('sp-spec' in item):
                id = int(item.replace('sp-spec-',''))
                esp2 = SP_Set.objects.get(sl_no=sl_no,sp_id=SP_Master.objects.get(id=id))
                esp2.spec = request.POST.get(item)
                esp2.save()
        return redirect('/part_info/'+str(sl_no)+'/?message=1')

def select_sp_set(request,sl_no):
    part = Part_Header.objects.get(sl_no=sl_no)
    sp_set = SP_Set.objects.filter(sl_no=sl_no)
    sp_master = SP_Master.objects.all()
    select_id = [x.sp_id.id for x in sp_set]
    context = {
            'part': part,
            'sp_set': sp_set,
            'sp_master': sp_master,
            'select_id': select_id
    }
    return render(request, 'rfqsite/select_sp_set.html', context)

def select_sp_set_confirm(request):
    if request.method == 'POST':
        sl_no = request.POST.get('sl-no')
        sp_master = SP_Master.objects.all()
        edit = 0
        for sp in sp_master:
            id = sp.id
            if(request.POST.get(str(id)) == None):
                delsp = SP_Set.objects.filter(sl_no=sl_no,sp_id=sp)
                delsp.delete()
            elif(request.POST.get(str(id)) == 'on'):
                if(SP_Set.objects.filter(sp_id=sp,sl_no=sl_no)):
                    pass
                else:
                    newsp = SP_Set(sl_no=Part_Header.objects.get(sl_no=sl_no),sp_id=sp)
                    newsp.save()
                    edit = 1
        if(edit == 1):
            return redirect('/edit_sp_set/'+str(sl_no)+'/?message=1')
        return redirect('/part_info/'+str(sl_no)+'/?message=1')
