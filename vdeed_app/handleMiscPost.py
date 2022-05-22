from django.http import HttpResponseRedirect
from vdeed_app.models import misc
from vdeed_app.forms import mantraRecitationForm


def handle_om_mani_padme_hum(request, user_id):
    print('---Om Mani Padme Hum---')
    form_mantra = mantraRecitationForm(request.POST)
    if form_mantra.is_valid():
        print('---form_mantra valid---')
        print(form_mantra.cleaned_data)
        all_misc = misc.objects.all()
        print('all_misc', all_misc)
        if (all_misc):
            if all_misc.filter(user=user_id).exists():
                print('username already exist')
                print('total records', all_misc.filter(
                    user=user_id).count())
                obj = all_misc.filter(user=user_id).first()
                current_misc_glass_bottle_counter = obj.misc_glass_bottle_counter
                print('current_misc_glass_bottle_counter',
                      current_misc_glass_bottle_counter)

                new_misc_glass_bottle_counter = current_misc_glass_bottle_counter + \
                    form_mantra.cleaned_data['misc_glass_bottle_counter']
                print('new misc_glass_bottle_counter',
                      new_misc_glass_bottle_counter)

                print('update om mani padme hum sutra record')
                all_misc.filter(user=user_id).update(
                    misc_glass_bottle_counter=new_misc_glass_bottle_counter)
            else:
                print('create om mani padme hum record')
                instance = form_mantra.save(commit=False)
                instance.user = request.user
                instance.save()
        else:
            print('create first om mani padme hum record')
            instance = form_mantra.save(commit=False)
            instance.user = request.user
            instance.save()
    else:
        print('form_mantra is not valid')
        print(form_mantra.errors)


def handle_manjushri_mantra(request, user_id):
    print('---Manjushri Mantra---')
    form_mantra = mantraRecitationForm(request.POST)
    if form_mantra.is_valid():
        print('---form_mantra valid---')
        print(form_mantra.cleaned_data)
        all_misc = misc.objects.all()
        print('all_misc', all_misc)
        if (all_misc):
            if all_misc.filter(user=user_id).exists():
                print('username already exist')
                print('total records', all_misc.filter(
                    user=user_id).count())
                obj = all_misc.filter(user=user_id).first()
                current_misc_mask_counter = obj.misc_mask_counter
                print('current_misc_mask_counter',
                      current_misc_mask_counter)

                new_misc_mask_counter = current_misc_mask_counter + \
                    form_mantra.cleaned_data['misc_mask_counter']
                print('new misc_mask_counter',
                      new_misc_mask_counter)

                print('update manjushri mantra record')
                all_misc.filter(user=user_id).update(
                    misc_mask_counter=new_misc_mask_counter)
            else:
                print('create manjushri mantra record')
                instance = form_mantra.save(commit=False)
                instance.user = request.user
                instance.save()
        else:
            print('create first manjushri mantra record')
            instance = form_mantra.save(commit=False)
            instance.user = request.user
            instance.save()
    else:
        print('form_mantra is not valid')
        print(form_mantra.errors)


def handle_green_tara_mantra(request, user_id):
    print('---Green Tara Sutra---')
    form_mantra = mantraRecitationForm(request.POST)
    if form_mantra.is_valid():
        print('---form mantra valid---')
        print(form_mantra.cleaned_data)
        all_misc = misc.objects.all()
        print('all_misc', all_misc)
        if (all_misc):
            if all_misc.filter(user=user_id).exists():
                print('username already exist')
                print('total records', all_misc.filter(
                    user=user_id).count())
                obj = all_misc.filter(user=user_id).first()
                current_misc_others_counter = obj.misc_others_counter
                print('current_misc_others_counter',
                      current_misc_others_counter)

                new_misc_others_counter = current_misc_others_counter + \
                    form_mantra.cleaned_data['misc_others_counter']
                print('new misc_others_counter',
                      new_misc_others_counter)

                print('update green tara mantra record')
                all_misc.filter(user=user_id).update(
                    misc_others_counter=new_misc_others_counter)
            else:
                print('create green tara mantra  record')
                instance = form_mantra.save(commit=False)
                instance.user = request.user
                instance.save()
        else:
            print('create first green tara mantra  record')
            instance = form_mantra.save(commit=False)
            instance.user = request.user
            instance.save()
    else:
        print('form_mantra is not valid')
        print(form_mantra.errors)


def handle_migtsema(request, user_id):
    print('---Migtsema Sutra---')
    form_mantra = mantraRecitationForm(request.POST)
    if form_mantra.is_valid():
        print('---form_mantra valid---')
        print(form_mantra.cleaned_data)
        all_misc = misc.objects.all()
        print('all_misc', all_misc)
        if (all_misc):
            if all_misc.filter(user=user_id).exists():
                print('username already exist')
                print('total records', all_misc.filter(
                    user=user_id).count())
                obj = all_misc.filter(user=user_id).first()
                current_misc_can_counter = obj.misc_can_counter
                print('current_misc_can_counter',
                      current_misc_can_counter)

                new_misc_can_counter = current_misc_can_counter + \
                    form_mantra.cleaned_data['misc_can_counter']
                print('new current_misc_can_counter',
                      new_misc_can_counter)

                print('update migtsema record')
                all_misc.filter(user=user_id).update(
                    misc_can_counter=new_misc_can_counter)
            else:
                print('create migtsema record')
                instance = form_mantra.save(commit=False)
                instance.user = request.user
                instance.save()
        else:
            print('create first migtsema record')
            instance = form_mantra.save(commit=False)
            instance.user = request.user
            instance.save()
    else:
        print('form_mantra is not valid')
        print(form_mantra.errors)
