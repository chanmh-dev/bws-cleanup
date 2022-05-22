from django.http import HttpResponseRedirect
from vdeed_app.models import paper
from vdeed_app.forms import sutraRecitationForm


def handle_mahaprajnaparamita_sutra(request, user_id):
    print('---Mahaprajnaparamita Sutra---')
    form_sutra = sutraRecitationForm(request.POST)
    if form_sutra.is_valid():
        print('---form_sutra valid---')
        print(form_sutra.cleaned_data)
        all_paper = paper.objects.all()
        print('all_paper', all_paper)
        if (all_paper):
            if all_paper.filter(user=user_id).exists():
                print('username already exist')
                print('total records', all_paper.filter(
                    user=user_id).count())
                obj = all_paper.filter(user=user_id).first()
                current_paper_tissue_counter = obj.paper_tissue_counter
                print('current_paper_tissue_counter',
                      current_paper_tissue_counter)

                new_paper_tissue_counter = current_paper_tissue_counter + \
                    form_sutra.cleaned_data['paper_tissue_counter']
                print('new paper_tissue_counter',
                      new_paper_tissue_counter)

                print('update mahaprajnaparamita sutra record')
                all_paper.filter(user=user_id).update(
                    paper_tissue_counter=new_paper_tissue_counter)
            else:
                print('create mahaprajnaparamita sutra record')
                instance = form_sutra.save(commit=False)
                instance.user = request.user
                instance.save()
        else:
            print('create first mahaprajnaparamita sutra record')
            instance = form_sutra.save(commit=False)
            instance.user = request.user
            instance.save()
    else:
        print('form_sutra is not valid')
        print(form_sutra.errors)


def handle_heart_sutra(request, user_id):
    print('---Heart Sutra---')
    form_sutra = sutraRecitationForm(request.POST)
    if form_sutra.is_valid():
        print('---form_sutra valid---')
        print(form_sutra.cleaned_data)
        all_paper = paper.objects.all()
        print('all_paper', all_paper)
        if (all_paper):
            if all_paper.filter(user=user_id).exists():
                print('username already exist')
                print('total records', all_paper.filter(
                    user=user_id).count())
                obj = all_paper.filter(user=user_id).first()
                current_paper_counter = obj.paper_counter
                print('current_paper_counter',
                      current_paper_counter)

                new_paper_counter = current_paper_counter + \
                    form_sutra.cleaned_data['paper_counter']
                print('new paper_counter',
                      new_paper_counter)

                print('update heart sutra record')
                all_paper.filter(user=user_id).update(
                    paper_counter=new_paper_counter)
            else:
                print('create heart sutra record')
                instance = form_sutra.save(commit=False)
                instance.user = request.user
                instance.save()
        else:
            print('create first heart sutra record')
            instance = form_sutra.save(commit=False)
            instance.user = request.user
            instance.save()
    else:
        print('form_sutra is not valid')
        print(form_sutra.errors)


def handle_medicine_buddha_sutra(request, user_id):
    print('---Medicine Buddha Sutra---')
    form_sutra = sutraRecitationForm(request.POST)
    if form_sutra.is_valid():
        print('---form sutra valid---')
        print(form_sutra.cleaned_data)
        all_paper = paper.objects.all()
        print('all_paper', all_paper)
        if (all_paper):
            if all_paper.filter(user=user_id).exists():
                print('username already exist')
                print('total records', all_paper.filter(
                    user=user_id).count())
                obj = all_paper.filter(user=user_id).first()
                current_paper_cup_counter = obj.paper_cup_counter
                print('current_paper_cup_counter',
                      current_paper_cup_counter)

                new_paper_cup_counter = current_paper_cup_counter + \
                    form_sutra.cleaned_data['paper_cup_counter']
                print('new paper_cup_counter',
                      new_paper_cup_counter)

                print('update medicine buddha sutra record')
                all_paper.filter(user=user_id).update(
                    paper_cup_counter=new_paper_cup_counter)
            else:
                print('create medicine buddha sutra record')
                instance = form_sutra.save(commit=False)
                instance.user = request.user
                instance.save()
        else:
            print('create first medicine buddha sutra record')
            instance = form_sutra.save(commit=False)
            instance.user = request.user
            instance.save()
    else:
        print('form_sutra is not valid')
        print(form_sutra.errors)


def handle_golden_light_sutra(request, user_id):
    print('---Golden Light Sutra---')
    form_sutra = sutraRecitationForm(request.POST)
    if form_sutra.is_valid():
        print('---form_sutra valid---')
        print(form_sutra.cleaned_data)
        all_paper = paper.objects.all()
        print('all_paper', all_paper)
        if (all_paper):
            if all_paper.filter(user=user_id).exists():
                print('username already exist')
                print('total records', all_paper.filter(
                    user=user_id).count())
                obj = all_paper.filter(user=user_id).first()
                current_paper_cigarette_butt_counter = obj.paper_cigarette_butt_counter
                print('current_paper_cigarette_butt_counter',
                      current_paper_cigarette_butt_counter)

                new_paper_cigarette_butt_counter = current_paper_cigarette_butt_counter + \
                    form_sutra.cleaned_data['paper_cigarette_butt_counter']
                print('new current_paper_cigarette_butt_counter',
                      new_paper_cigarette_butt_counter)

                print('update recitation record')
                all_paper.filter(user=user_id).update(
                    paper_cigarette_butt_counter=new_paper_cigarette_butt_counter)
            else:
                print('create golden light sutra record')
                instance = form_sutra.save(commit=False)
                instance.user = request.user
                instance.save()
        else:
            print('create first golden light sutra record')
            instance = form_sutra.save(commit=False)
            instance.user = request.user
            instance.save()
    else:
        print('form_sutra is not valid')
        print(form_sutra.errors)
