from django.http import HttpResponseRedirect
from vdeed_app.models import plastic
from vdeed_app.forms import plasticForm


def handle_plastic_bag(request, user_id):
    print('---Plastic Bag---')
    form_plastic = plasticForm(request.POST)
    if form_plastic.is_valid():
        print('---plastic valid---')
        print(form_plastic.cleaned_data)
        all_plastic = plastic.objects.all()
        print('all_plastic', all_plastic)
        if (all_plastic):
            if all_plastic.filter(user=user_id).exists():
                print('username already exist')
                print('total records', all_plastic.filter(
                    user=user_id).count())
                obj = all_plastic.filter(user=user_id).first()
                current_plastic_bag_counter = obj.plastic_bag_counter
                print('current_plastic_bag_counter',
                      current_plastic_bag_counter)

                new_plastic_bag_counter = current_plastic_bag_counter + \
                    form_plastic.cleaned_data['plastic_bag_counter']
                print('new plastic_bag_counter',
                      new_plastic_bag_counter)

                print('update full prostration record')
                all_plastic.filter(user=user_id).update(
                    plastic_bag_counter=new_plastic_bag_counter)
            else:
                print('create full prostration record')
                instance = form_plastic.save(commit=False)
                instance.user = request.user
                instance.save()
        else:
            print('create first full prostration record')
            instance = form_plastic.save(commit=False)
            instance.user = request.user
            instance.save()
    else:
        print('form_plastic is not valid')
        print(form_plastic.errors)


def handle_plastic_bottle(request, user_id):
    print('---Plastic Bottle---')
    form_plastic = plasticForm(request.POST)
    if form_plastic.is_valid():
        print('---plastic valid---')
        print(form_plastic.cleaned_data)
        all_plastic = plastic.objects.all()
        print('all_plastic', all_plastic)
        if (all_plastic):
            if all_plastic.filter(user=user_id).exists():
                print('username already exist')
                print('total records', all_plastic.filter(
                    user=user_id).count())
                obj = all_plastic.filter(user=user_id).first()
                current_plastic_bottle_counter = obj.plastic_bottle_counter
                print('current_plastic_bottle_counter',
                      current_plastic_bottle_counter)

                new_plastic_bottle_counter = current_plastic_bottle_counter + \
                    form_plastic.cleaned_data['plastic_bottle_counter']
                print('new plastic_bottle_counter',
                      new_plastic_bottle_counter)

                print('update half prostration record')
                all_plastic.filter(user=user_id).update(
                    plastic_bottle_counter=new_plastic_bottle_counter)
            else:
                print('create half prostration record')
                instance = form_plastic.save(commit=False)
                instance.user = request.user
                instance.save()
        else:
            print('create first half prostration record')
            instance = form_plastic.save(commit=False)
            instance.user = request.user
            instance.save()
    else:
        print('form_plastic is not valid')
        print(form_plastic.errors)


def handle_plastic_wrapper(request, user_id):
    print('---Plastic Wrapper---')
    form_plastic = plasticForm(request.POST)
    if form_plastic.is_valid():
        print('---plastic valid---')
        print(form_plastic.cleaned_data)
        all_plastic = plastic.objects.all()
        print('all_plastic', all_plastic)
        if (all_plastic):
            if all_plastic.filter(user=user_id).exists():
                print('username already exist')
                print('total records', all_plastic.filter(
                    user=user_id).count())
                obj = all_plastic.filter(user=user_id).first()
                current_plastic_wrapper_counter = obj.plastic_wrapper_counter
                print('current_plastic_wrapper_counter',
                      current_plastic_wrapper_counter)

                new_plastic_wrapper_counter = current_plastic_wrapper_counter + \
                    form_plastic.cleaned_data['plastic_wrapper_counter']
                print('new plastic_wrapper_counter',
                      new_plastic_wrapper_counter)

                print('update bow record')
                all_plastic.filter(user=user_id).update(
                    plastic_wrapper_counter=new_plastic_wrapper_counter)
            else:
                print('create bow prostration record')
                instance = form_plastic.save(commit=False)
                instance.user = request.user
                instance.save()
        else:
            print('create first bow record')
            instance = form_plastic.save(commit=False)
            instance.user = request.user
            instance.save()
    else:
        print('form_plastic is not valid')
        print(form_plastic.errors)


def handle_plastic_cup_straw(request, user_id):
    print('---Plastic Cup and Straw---')
    form_plastic = plasticForm(request.POST)
    if form_plastic.is_valid():
        print('---plastic valid---')
        print(form_plastic.cleaned_data)
        all_plastic = plastic.objects.all()
        print('all_plastic', all_plastic)
        if (all_plastic):
            if all_plastic.filter(user=user_id).exists():
                print('username already exist')
                print('total records', all_plastic.filter(
                    user=user_id).count())
                obj = all_plastic.filter(user=user_id).first()
                current_plastic_cup_straw_counter = obj.plastic_cup_straw_counter
                print('current_plastic_cup_straw_counter',
                      current_plastic_cup_straw_counter)

                new_plastic_cup_straw_counter = current_plastic_cup_straw_counter + \
                    form_plastic.cleaned_data['plastic_cup_straw_counter']
                print('new plastic_cup_straw_counter',
                      new_plastic_cup_straw_counter)

                print('update recitation record')
                all_plastic.filter(user=user_id).update(
                    plastic_cup_straw_counter=new_plastic_cup_straw_counter)
            else:
                print('create recitation prostration record')
                instance = form_plastic.save(commit=False)
                instance.user = request.user
                instance.save()
        else:
            print('create first recitation record')
            instance = form_plastic.save(commit=False)
            instance.user = request.user
            instance.save()
    else:
        print('form_plastic is not valid')
        print(form_plastic.errors)
