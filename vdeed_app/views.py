from base64 import urlsafe_b64encode
import email
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.db.models import Sum
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from vdeed_app.models import deeds1, deeds2, deeds3, globalLamrim2, plastic, paper, misc, counter_target
from vdeed_app.forms import deeds1Form, deeds2Form, deeds3Form, globalLamrim2Form, DateForm, Date2Form, Date3Form, Date4Form
from vdeed_app.forms import plasticForm, sutraRecitationForm, mantraRecitationForm
from django.utils import timezone
from django.forms.models import model_to_dict
from datetime import datetime, time
from . import config
from .handlePlasticPost import handle_plastic_bag, handle_plastic_bottle, handle_plastic_wrapper, handle_plastic_cup_straw
from .handlePaperPost import handle_mahaprajnaparamita_sutra, handle_heart_sutra, handle_medicine_buddha_sutra, handle_golden_light_sutra
from .handleMiscPost import handle_om_mani_padme_hum, handle_manjushri_mantra, handle_green_tara_mantra, handle_migtsema

from .totalMerits import total_plastic, total_sutra, total_mantra
import re


def mobile(request):

    MOBILE_AGENT_RE = re.compile(
        r".*(iphone|mobile|androidtouch)", re.IGNORECASE)

    if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
        return True
    else:
        return False


def is_time_between(begin_time, end_time, check_time=None):
    # If check time is not given, default to current time
    check_time = check_time or datetime.now().time()
    print('current time', check_time)
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else:  # crosses midnight
        return check_time >= begin_time or check_time <= end_time


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

# Create your views here.


def index(request):
    message1 = ''
    message2 = ''
    message3 = ''

    txt1 = ""
    txt2 = ""
    txt3 = ""

    print('config', config.post_success)

    submitted = False
    if request.method == 'POST':
        if 'btnform1' in request.POST:
            print('---btnform1---')
            form1 = deeds1Form(request.POST)
            if form1.is_valid():
                print('---form1 valid---')
                # print('final deed', form1.cleaned_data['deed'])
                cd1 = form1.cleaned_data
                form1.save()
                config.post_success = 1
                # assert False
                return HttpResponseRedirect('/index?submitted=True')
        elif 'btnform2' in request.POST:
            print('---btnform2---')
            form2 = deeds2Form(request.POST)
            if form2.is_valid():
                print('---form2 valid---')
                cd2 = form2.cleaned_data
                form2.save()
                config.post_success = 1
                # assert False
                return HttpResponseRedirect('/index?submitted=True')
        elif 'btnform3' in request.POST:
            print('---btnform3---')
            form3 = deeds3Form(request.POST)
            if form3.is_valid():
                print('---form3 valid---')
                cd3 = form3.cleaned_data
                form3.save()
                config.post_success = 1
                # assert False
                return HttpResponseRedirect('/index?submitted=True')

        print('empty post')
        form1 = deeds1Form()
        form2 = deeds2Form()
        form3 = deeds3Form()
    else:
        print('---GET---')
        form1 = deeds1Form()
        form2 = deeds2Form()
        form3 = deeds3Form()
        if 'submitted' in request.GET:
            submitted = True

    all_deeds1 = deeds1.objects.all().order_by('-date_time')
    # print(all_deeds1)
    if (all_deeds1):
        date_time1 = deeds1.objects.values_list(
            'date_time', flat=True).distinct()
        # print(date_time)
        all_messages = deeds1.objects.values_list(
            'deed', flat=True).distinct().order_by('-date_time')
        for message in all_messages:
            message1 = message1 + message
            txt = cleanhtml(message) + "\r\r"
            txt1 = txt1 + txt
        # print('message1', message1)

    # form1 = deeds1Form(hide_condition=True)

    all_deeds2 = deeds2.objects.all().order_by('-date_time')
    # print(all_deeds2)
    if (all_deeds2):
        date_time2 = deeds2.objects.values_list(
            'date_time', flat=True).distinct()
        # print(date_time)
        all_messages = deeds2.objects.values_list(
            'deed', flat=True).distinct().order_by('-date_time')
        for message in all_messages:
            message2 = message2 + message
            txt = cleanhtml(message) + "\r\r"
            txt2 = txt2 + txt
        # print('message2', message2)

    # form2 = deeds2Form(hide_condition=True)

    all_deeds3 = deeds3.objects.all().order_by('-date_time')
    # print(all_deeds3)
    if (all_deeds3):
        date_time3 = deeds3.objects.values_list(
            'date_time', flat=True).distinct()
        # print(date_time)
        all_messages = deeds3.objects.values_list(
            'deed', flat=True).distinct().order_by('-date_time')
        for message in all_messages:
            message3 = message3 + message
            txt = cleanhtml(message) + "\r\r"
            txt3 = txt3 + txt
        # print('message1', message1)

    # form3 = deeds3Form(hide_condition=True)

    context = {}

    context['text1'] = '<textarea readonly rows="10" class="v-border" id="txt1area" style="width:100%">' + txt1 + '</textarea>'
    context['text2'] = '<textarea readonly rows="10" class="v-border" id="txt2area" style="width:100%">' + txt2 + '</textarea>'
    context['text3'] = '<textarea readonly rows="10" class="v-border" id="txt3area" style="width:100%">' + txt3 + '</textarea>'

    context['deed1'] = '<div class="mqcontainer">' + \
        '<div class="marquee">' + message1 + '</div>' + '</div>'
    context['deed2'] = '<div class="mqcontainer">' + \
        '<div class="marquee">' + message2 + '</div>' + '</div>'
    context['deed3'] = '<div class="mqcontainer">' + \
        '<div class="marquee">' + message3 + '</div>' + '</div>'

    context['form1'] = form1
    context['form2'] = form2
    context['form3'] = form3

    now = timezone.now().strftime('%H:%M:%S')
    now1 = datetime.now().time().strftime('%H:%M:%S')
    day = datetime.today().weekday() + 1
    print('day', day)
    show = is_time_between(time(22, 00), time(22, 45))
    print('show', show)
    print('time now ', now)
    context['now'] = now
    if show:
        context['hide'] = False
    else:
        context['hide'] = False

    context['now1'] = now1

    if mobile(request):
        context['mobile'] = True
    else:
        context['mobile'] = False

    if config.post_success == 1:
        print('post success')
        context['post_success'] = True
        config.post_success = 0
    else:
        print('post failed')
        context['post_success'] = False

    return render(request, 'index.html', context)


def view_offerings(request):
    message1 = ""
    message2 = ""
    message3 = ""

    txt1 = ""
    txt2 = ""
    txt3 = ""

    submitted = False

    total_deeds1_count = 0
    total_deeds2_count = 0
    total_deeds3_count = 0

    filtered_from_date1 = ""
    filtered_to_date1 = ""
    filtered_from_date2 = ""
    filtered_to_date2 = ""
    filtered_from_date3 = ""
    filtered_to_date3 = ""

    all_deeds1 = deeds1.objects.all().order_by('-date_time')
    all_deeds2 = deeds1.objects.all().order_by('-date_time')
    all_deeds3 = deeds1.objects.all().order_by('-date_time')

    nameCount = deeds1.objects.order_by('name').values(
        'name').annotate(count=Count('id'))
    sortedName = sorted(nameCount, key=lambda k: k['count'], reverse=True)
    deeds1_top_five = list(sortedName)[:5]
    print(deeds1_top_five)

    nameCount = deeds2.objects.order_by('name').values(
        'name').annotate(count=Count('id'))
    sortedName = sorted(nameCount, key=lambda k: k['count'], reverse=True)
    deeds2_top_five = list(sortedName)[:5]
    print(deeds2_top_five)

    nameCount = deeds3.objects.order_by('name').values(
        'name').annotate(count=Count('id'))
    sortedName = sorted(nameCount, key=lambda k: k['count'], reverse=True)
    deeds3_top_five = list(sortedName)[:5]
    print(deeds3_top_five)

    if request.method == 'POST':
        if 'btnform' in request.POST:
            print('---date form---')
            form = DateForm(request.POST)
            if form.is_valid():
                print('---date form valid---')
                filtered_from_date1 = form.cleaned_data.get('date1_from')
                filtered_to_date1 = form.cleaned_data.get('date1_to')
                # assert False
                # return HttpResponseRedirect('/past_offerings?submitted=True')

        if 'btnform2' in request.POST:
            form2 = Date2Form(request.POST)
            if form2.is_valid():
                print('---date2 form valid---')
                filtered_from_date2 = form2.cleaned_data.get('date2_from')
                filtered_to_date2 = form2.cleaned_data.get('date2_to')

        if 'btnform3' in request.POST:
            form3 = Date3Form(request.POST)
            if form3.is_valid():
                print('---date3 form valid---')
                filtered_from_date3 = form3.cleaned_data.get('date3_from')
                filtered_to_date3 = form3.cleaned_data.get('date3_to')
    else:
        print('---GET---')
        form = DateForm()
        form2 = Date2Form()
        form3 = Date3Form()
        if 'submitted' in request.GET:
            submitted = True

    if filtered_from_date1 != "":
        print('filtered_from_date not None')
        print("from date ", filtered_from_date1)
        print("to date ", filtered_to_date1)
        all_deeds1 = deeds1.objects.all().filter(
            date_time__range=[filtered_from_date1, filtered_to_date1]).order_by('-date_time')
    else:
        print('filtered_from_date None')
        all_deeds1 = deeds1.objects.all().order_by('-date_time')

    # print(all_deeds1)
    if (all_deeds1):
        # date_time1 = all_deeds1.values_list('date_time', flat=True).distinct()
        deed1_first_obj_date = deeds1.objects.first().date_time.strftime("%d/%m/%Y")
        deed1_last_obj_date = deeds1.objects.last().date_time.strftime("%d/%m/%Y")
        print('deed1_first_obj_date', deed1_first_obj_date)
        print('deed1_last_obj_date', deed1_last_obj_date)

        total_deeds1_count = all_deeds1.count()
        messages = all_deeds1.values_list(
            'deed', flat=True).distinct().order_by('-date_time')
        for message in messages:
            message1 = message1 + message
            txt = cleanhtml(message) + "\r\r"
            txt1 = txt1 + txt

        # print('message1', message1)

    # form1 = deeds1Form(hide_condition=True)

    if filtered_from_date2 != "":
        print('filtered_from_date2 not None')
        print("from date ", filtered_from_date2)
        print("to date ", filtered_to_date2)
        all_deeds2 = deeds2.objects.all().filter(
            date_time__range=[filtered_from_date2, filtered_to_date2]).order_by('-date_time')
    else:
        print('filtered_from_date2 None')
        all_deeds2 = deeds2.objects.all().order_by('-date_time')

    # print(all_deeds1)
    if (all_deeds2):
        # date_time2 = all_deeds2.values_list('date_time', flat=True).distinct()
        # print(date_time)
        deed2_first_obj_date = deeds2.objects.first().date_time.strftime("%d/%m/%Y")
        deed2_last_obj_date = deeds2.objects.last().date_time.strftime("%d/%m/%Y")
        print('deed2_first_obj_date', deed2_first_obj_date)
        print('deed2_last_obj_date', deed2_last_obj_date)

        total_deeds2_count = all_deeds2.count()
        messages = all_deeds2.values_list(
            'deed', flat=True).distinct().order_by('-date_time')
        for message in messages:
            message2 = message2 + message
            txt = cleanhtml(message) + "\r\r"
            txt2 = txt2 + txt

        # print('message2', message2)

    # form2 = deeds2Form(hide_condition=True)

    if filtered_from_date3 != "":
        print('filtered_from_date3 not None')
        print("from date ", filtered_from_date2)
        print("to date ", filtered_to_date2)
        all_deeds3 = deeds3.objects.all().filter(
            date_time__range=[filtered_from_date3, filtered_to_date3]).order_by('-date_time')
    else:
        print('filtered_from_date3 None')
        all_deeds3 = deeds3.objects.all().order_by('-date_time')

    # print(all_deeds1)
    if (all_deeds3):
        # date_time3 = all_deeds3.values_list('date_time', flat=True).distinct()
        # print(date_time)
        deed3_first_obj_date = deeds3.objects.first().date_time.strftime("%d/%m/%Y")
        deed3_last_obj_date = deeds3.objects.last().date_time.strftime("%d/%m/%Y")
        print('deed3_first_obj_date', deed3_first_obj_date)
        print('deed3_last_obj_date', deed3_last_obj_date)

        total_deeds3_count = all_deeds3.count()
        messages = all_deeds3.values_list(
            'deed', flat=True).distinct().order_by('-date_time')
        for message in messages:
            message3 = message3 + message
            txt = cleanhtml(message) + "\r\r"
            txt3 = txt3 + txt

        # print('message1', message1)

    # form3 = deeds3Form(hide_condition=True)

    context = {}

    form = DateForm
    form2 = Date2Form
    form3 = Date3Form

    if filtered_from_date1 != "":
        context['filtered_from_date1'] = filtered_from_date1
        context['filtered_to_date1'] = filtered_to_date1
    else:
        context['filtered_from_date1'] = deed1_first_obj_date
        context['filtered_to_date1'] = deed1_last_obj_date

    if filtered_from_date2 != "":
        context['filtered_from_date2'] = filtered_from_date2
        context['filtered_to_date2'] = filtered_to_date2
    else:
        context['filtered_from_date2'] = deed2_first_obj_date
        context['filtered_to_date2'] = deed2_last_obj_date

    if filtered_from_date3 != "":
        context['filtered_from_date3'] = filtered_from_date3
        context['filtered_to_date3'] = filtered_to_date3
    else:
        context['filtered_from_date3'] = deed3_first_obj_date
        context['filtered_to_date3'] = deed3_last_obj_date

    context['total_deeds1_count'] = total_deeds1_count

    context['total_deeds2_count'] = total_deeds2_count

    context['total_deeds3_count'] = total_deeds3_count

    print('context_filtered_from_date1', context['filtered_from_date1'])

    context['form'] = form
    context['form2'] = form2
    context['form3'] = form3

    context['text1'] = '<textarea readonly rows="10" class="v-border" id="txt1area" style="width:100%">' + txt1 + '</textarea>'
    context['text2'] = '<textarea readonly rows="10" class="v-border" id="txt2area" style="width:100%">' + txt2 + '</textarea>'
    context['text3'] = '<textarea readonly rows="10" class="v-border" id="txt3area" style="width:100%">' + txt3 + '</textarea>'

    context['deeds1_top_five'] = deeds1_top_five
    context['deeds2_top_five'] = deeds2_top_five
    context['deeds3_top_five'] = deeds3_top_five

    return render(request, 'view_offerings.html', context)


def view_merits(request):
    plastic_bag_target = 0
    plastic_bottle_target = 0
    plastic_wrapper_target = 0
    plastic_cup_straw_target = 0

    paper_tissue_target = 0
    paper_target = 0
    paper_cup_target = 0
    paper_cigarette_butt_target = 0

    misc_glass_bottle_target = 0
    misc_mask_target = 0
    misc_others_target = 0
    misc_can_target = 0

    context = {}
    first_counter_target_record = counter_target.objects.first()
    if(first_counter_target_record):
        plastic_bag_target = first_counter_target_record.plastic_bag_target
        plastic_bottle_target = first_counter_target_record.plastic_bottle_target
        plastic_wrapper_target = first_counter_target_record.plastic_wrapper_target
        plastic_cup_straw_target = first_counter_target_record.plastic_cup_straw_target

        paper_tissue_target = first_counter_target_record.paper_tissue_target
        paper_target = first_counter_target_record.paper_target
        paper_cup_target = first_counter_target_record.paper_cup_target
        paper_cigarette_butt_target = first_counter_target_record.paper_cigarette_butt_target

        misc_glass_bottle_target = first_counter_target_record.misc_glass_bottle_target
        misc_mask_target = first_counter_target_record.misc_mask_target
        misc_others_target = first_counter_target_record.misc_others_target
        misc_can_target = first_counter_target_record.misc_can_target

    total_plastic(context)
    total_sutra(context)
    total_mantra(context)

    context['plastic_bag_target'] = plastic_bag_target
    context['plastic_bottle_target'] = plastic_bottle_target
    context['plastic_wrapper_target'] = plastic_wrapper_target
    context['plastic_cup_straw_target'] = plastic_cup_straw_target

    context['paper_tissue_target'] = paper_tissue_target
    context['paper_target'] = paper_target
    context['paper_cup_target'] = paper_cup_target
    context['paper_cigarette_butt_target'] = paper_cigarette_butt_target

    context['misc_glass_bottle_target'] = misc_glass_bottle_target
    context['misc_mask_target'] = misc_mask_target
    context['misc_others_target'] = misc_others_target
    context['misc_can_target'] = misc_can_target

    print('view_merits')

    return render(request, 'view_merits.html', context)


@ login_required(login_url="/accounts/login")
def view_merits_detail(request, id=None):
    user_id = request.user.id
    print(request.user)
    print('page id =', id)
    print('user id =', user_id)

    if request.method == 'POST':
        print('request.POST', request.POST)
        print('---anchor tag---', request.POST.get('anchor-tag'))

        redirect_path = '/view_merits_detail/view_merits_detail/' + \
            str(user_id) + request.POST.get('anchor-tag')
        print(redirect_path)

        if 'btnFullProstration' in request.POST:
            handle_plastic_bag(request, user_id)
        elif 'btnHalfProstration' in request.POST:
            handle_plastic_bottle(request, user_id)
        elif 'btnBow' in request.POST:
            handle_plastic_wrapper(request, user_id)
        elif 'btnRecitation' in request.POST:
            handle_plastic_cup_straw(request, user_id)
        elif 'btnMahaprajnaparamita' in request.POST:
            handle_mahaprajnaparamita_sutra(request, user_id)
        elif 'btnHeartSutra' in request.POST:
            handle_heart_sutra(request, user_id)
        elif 'btnMedicineBuddhaSutra' in request.POST:
            handle_medicine_buddha_sutra(request, user_id)
        elif 'btnGoldenLightSutra' in request.POST:
            handle_golden_light_sutra(request, user_id)
        elif 'btnOmManiPadmeHum' in request.POST:
            handle_om_mani_padme_hum(request, user_id)
        elif 'btnManjushriMantra' in request.POST:
            handle_manjushri_mantra(request, user_id)
        elif 'btnGreenTaraMantra' in request.POST:
            handle_green_tara_mantra(request, user_id)
        elif 'btnMigtsema' in request.POST:
            handle_migtsema(request, user_id)
        else:
            print('empty post')

        return HttpResponseRedirect(redirect_path)
    else:
        print('---GET---')
        if 'submitted' in request.GET:
            submitted = True

    context = {}

    new_plastic_bag_counter = 0
    new_plastic_bottle_counter = 0
    new_plastic_wrapper_counter = 0
    new_plastic_cup_straw_counter = 0
    form_plastic = plasticForm()
    all_plastic = plastic.objects.all()
    if (all_plastic):
        if all_plastic.filter(user=user_id).exists():
            obj = all_plastic.filter(user=user_id).first()
            new_plastic_bag_counter = obj.plastic_bag_counter
            new_plastic_bottle_counter = obj.plastic_bottle_counter
            new_plastic_wrapper_counter = obj.plastic_wrapper_counter
            new_plastic_cup_straw_counter = obj.plastic_cup_straw_counter

    print('plastic_bag_counter', new_plastic_bag_counter)
    context['plastic_bag_counter'] = new_plastic_bag_counter
    context['plastic_bottle_counter'] = new_plastic_bottle_counter
    context['plastic_wrapper_counter'] = new_plastic_wrapper_counter
    context['plastic_cup_straw_counter'] = new_plastic_cup_straw_counter

    context['form_plastic'] = form_plastic

    new_paper_tissue_counter = 0
    new_paper_counter = 0
    new_paper_cup_counter = 0
    new_paper_cigarette_butt_counter = 0
    form_paper = sutraRecitationForm()
    all_paper = paper.objects.all()
    if (all_paper):
        if all_paper.filter(user=user_id).exists():
            obj = all_paper.filter(user=user_id).first()
            new_paper_tissue_counter = obj.paper_tissue_counter
            new_paper_counter = obj.paper_counter
            new_paper_cup_counter = obj.paper_cup_counter
            new_paper_cigarette_butt_counter = obj.paper_cigarette_butt_counter

    print('paper_tissue_counter',
          new_paper_tissue_counter)
    context['paper_tissue_counter'] = new_paper_tissue_counter
    context['paper_counter'] = new_paper_counter
    context['paper_cup_counter'] = new_paper_cup_counter
    context['paper_cigarette_butt_counter'] = new_paper_cigarette_butt_counter

    context['form_paper'] = form_paper

    new_misc_glass_bottle_counter = 0
    new_misc_mask_counter = 0
    new_misc_others_counter = 0
    new_misc_can_counter = 0
    form_misc = mantraRecitationForm()
    all_misc = misc.objects.all()
    #print('all_misc', all_misc)
    if (all_misc):
        if all_misc.filter(user=user_id).exists():
            obj = all_misc.filter(user=user_id).first()
            new_misc_glass_bottle_counter = obj.misc_glass_bottle_counter
            new_misc_mask_counter = obj.misc_mask_counter
            new_misc_others_counter = obj.misc_others_counter
            new_misc_can_counter = obj.misc_can_counter

    print('misc_glass_bottle_counter',
          new_misc_glass_bottle_counter)
    context['misc_glass_bottle_counter'] = new_misc_glass_bottle_counter
    context['misc_mask_counter'] = new_misc_mask_counter
    context['misc_others_counter'] = new_misc_others_counter
    context['misc_can_counter'] = new_misc_can_counter

    context['form_misc'] = form_misc

    if user_id is not None:
        print('view_merits_detail')
        return render(request, 'view_merits_detail.html', context)
    else:
        print('view_merits')
        return render(request, 'view_merits.html', context)


@ login_required(login_url="/accounts/login")
def view_add_counter(request, id=None):
    user_id = request.user.id
    print(request.user)
    print('page id =', id)
    print('user id =', user_id)

    if request.method == 'POST':
        print('request.POST', request.POST)
        print('---anchor tag---', request.POST.get('anchor-tag'))

        redirect_path = '/view_add_counter/view_add_counter/' + \
            str(user_id) + request.POST.get('anchor-tag')
        print(redirect_path)

        if 'btnMigtsema' in request.POST:
            handle_migtsema(request, user_id)
        else:
            print('empty post')

        return HttpResponseRedirect(redirect_path)
    else:
        print('---GET---')
        if 'submitted' in request.GET:
            submitted = True

    context = {}

    new_misc_glass_bottle_counter = 0
    new_misc_mask_counter = 0
    new_misc_others_counter = 0
    new_misc_can_counter = 0
    form_misc = mantraRecitationForm()
    all_misc = misc.objects.all()
    #print('all_misc', all_misc)
    if (all_misc):
        if all_misc.filter(user=user_id).exists():
            obj = all_misc.filter(user=user_id).first()
            new_misc_glass_bottle_counter = obj.misc_glass_bottle_counter
            new_misc_mask_counter = obj.misc_mask_counter
            new_misc_others_counter = obj.misc_others_counter
            new_misc_can_counter = obj.misc_can_counter

    print('misc_glass_bottle_counter',
          new_misc_glass_bottle_counter)
    context['misc_glass_bottle_counter'] = new_misc_glass_bottle_counter
    context['misc_mask_counter'] = new_misc_mask_counter
    context['misc_others_counter'] = new_misc_others_counter
    context['misc_can_counter'] = new_misc_can_counter

    context['form_misc'] = form_misc

#############
    total_misc_can_counter = 0

    all_misc = misc.objects.all()
    if (all_misc):
        total_misc_can_counter = misc.objects.aggregate(
            Sum('misc_can_counter'))['misc_can_counter__sum']

    context['total_misc_can_counter'] = total_misc_can_counter

#############

    if user_id is not None:
        print('view_add_counter')
        return render(request, 'view_add_counter.html', context)
    else:
        print('view_merits')
        return render(request, 'view_merits.html', context)


def view_home(request):
    current_target = 10000
    completed_targets = {}
    context = {}

    total_misc_can_counter = 0

    all_misc = misc.objects.all()
    if (all_misc):
        total_misc_can_counter = misc.objects.aggregate(
            Sum('misc_can_counter'))['misc_can_counter__sum']

        int_part = total_misc_can_counter // 10000
        print("----int_part----", int_part)
        counter_target_count = counter_target.objects.count()
        print('counter_target_count', counter_target_count)
        if int_part > counter_target_count:
            loop_counter = int_part - counter_target_count + 1
            print("----loop_counter----", loop_counter)
            for x in range(counter_target_count+1, counter_target_count+loop_counter):
                target_record = counter_target.objects.create(
                    misc_can_target=x*10000)
                #print("update target counter", target_record)

    targets = counter_target.objects.values('misc_can_target', 'date_time')
    completed_targets = list(targets)
    reverse_target_list = reversed(completed_targets)
    #print('reverse_target_list', reverse_target_list)

    last_target = counter_target.objects.last()
    if (last_target):
        current_target = last_target.misc_can_target + 10000

    context['completed_targets'] = reverse_target_list
    #print('completed_targets', context['completed_targets'])

    context['current_target'] = current_target
    print('current_target', current_target)

    context['total_misc_can_counter'] = total_misc_can_counter

    print('view_home')

    return render(request, 'view_home.html', context)


def password_reset_request(request):
    if request.method == 'POST':
        password_form = PasswordResetForm(request.POST)
        if password_form.is_valid():
            data = password_form.cleaned_data['email']
            user_email = User.objects.filter(Q(email=data))
            if user_email.exists():
                for user in user_email:
                    subject = 'Password_Request'
                    email_template_name = 'password_message.txt'
                    parameters = {
                        'email': user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Blossom World Society',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, parameters)
                    try:
                        send_mail(subject, email, '', [
                            user.email], fail_silently=False)
                    except:
                        return HttpResponse('Invalid Header')

                    return redirect('password_reset_done')

    else:
        password_form = PasswordResetForm()

    context = {
        'password_form': password_form,
    }
    return render(request, 'password_reset.html', context)
